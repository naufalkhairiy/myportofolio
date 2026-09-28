import json
import uuid
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education

from django.contrib.auth.models import Group, User
from django.test import Client


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class EducationPageTests(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            program="S1 Ilmu Komputer",
            start_year=2025,
            end_year=None,
            website="https://www.ui.ac.id/",
            description="",
        )

    def test_education_url_is_accessible_and_uses_correct_template(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_data_is_displayed(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "S1 Ilmu Komputer")
        self.assertContains(response, "2025")
        self.assertContains(response, "Present")

    def test_education_empty_state_is_displayed(self):
        Education.objects.all().delete()

        response = self.client.get(reverse("main:show_education"))

        self.assertContains(
            response,
            "Belum ada riwayat pendidikan yang ditambahkan."
        )

    def test_education_is_current_property(self):
        self.assertTrue(self.education.is_current)

        self.education.end_year = 2029
        self.education.save()

        self.assertFalse(self.education.is_current)

    def test_education_detail_page_is_accessible(self):
        response = self.client.get(
            reverse(
                "main:show_education_detail",
                args=[self.education.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education_detail.html")


    def test_education_detail_displays_correct_data(self):
        response = self.client.get(
            reverse(
                "main:show_education_detail",
                args=[self.education.id]
            )
        )

        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "S1 Ilmu Komputer")
        self.assertContains(response, "2025")
        self.assertContains(response, "Present")


    def test_nonexistent_education_detail_returns_404(self):
        nonexistent_id = uuid.uuid4()

        response = self.client.get(
            reverse(
                "main:show_education_detail",
                args=[nonexistent_id]
            )
        )

        self.assertEqual(response.status_code, 404)

class EducationCRUDTests(TestCase):
    def setUp(self):
        owner = User.objects.create_user(
            username="crud_owner",
            is_superuser=True,
            is_staff=True,
        )
        self.client.force_login(owner)
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            program="S1 Ilmu Komputer",
            start_year = 2025,
            end_year = None,
            website ="https://www.ui.ac.id/",
            description="Computer Science student.",
        )

    def test_create_education(self):
        response = self.client.post(
            reverse("main:create_education"),
            {
                "institution":"Test University",
                "program":"Computer Science",
                "start_year": 2026,
                "end_year":"",
                "website": "https://example.com/",
                "description":"Test education",
            }
        )

        self.assertRedirects(
            response,
            reverse("main:show_education")
        )

        self.assertTrue(
            Education.objects.filter(
                institution="Test University"
            ).exists()
        )

    def test_update_education(self):
        response = self.client.post(
            reverse(
                "main:update_education",
                args=[self.education.id]
            ),
            {
                "institution": "Universitas Indonesia",
                "program":"S1 Ilmu Komputer",
                "start_year": "2025",
                "end_year": "2029",
                "website": "https://www.ui.ac.id/",
                "description": "Updated description.",
            }
        )

        self.education.refresh_from_db()

        self.assertEqual(
            self.education.description,
            "Updated description."
        )

        self.assertEqual(
            self.education.end_year,
            2029
        )

        self.assertRedirects(
            response,
            reverse(
                "main:show_education_detail",
                args=[self.education.id]
            )
        )

    def test_delete_education(self):
        response =self.client.post(
            reverse(
                "main:delete_education",
                args=[self.education.id]
            )
        )

        self.assertFalse(
            Education.objects.filter(
                id=self.education.id
            ).exists()
        )

        self.assertRedirects(
            response,
            reverse("main:show_education")
        )

    def test_education_json_search(self):
        Education.objects.create(
            institution="MAN Insan Cendekia OKI",
            program="Science",
            start_year="2022",
        )

        response = self.client.get(
            reverse("main:get_education_json"),
            {
                "institution":"Indonesia"
            }
        )

        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["institution"], "Universitas Indonesia")


    def test_education_page_search(self):
        Education.objects.create(
            institution="MAN Insan Cendekia OKI",
            program="Science",
            start_year=2022,
        )

        response = self.client.get(
            reverse("main:show_education"),
            {
                "institution": "MAN"
            }
        )

        institutions = [
            education.institution
            for education in response.context["education_list"]
        ]

        self.assertEqual(
            institutions,
            ["MAN Insan Cendekia OKI"]
        )

class EducationAuthorizationTests(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Test University",
            program="Computer Science",
            start_year=2025,
        )
        self.member = User.objects.create_user(username="member")
        self.editor = User.objects.create_user(username="editor")
        self.owner = User.objects.create_user(
            username="owner",
            is_superuser=True,
            is_staff=True,
        )
        group = Group.objects.create(name="Editor")
        self.editor.groups.add(group)

        self.list_url = reverse("main:show_education")
        self.detail_url = reverse(
            "main:show_education_detail", args=[self.education.pk]
        )
        self.create_url = reverse("main:create_education")
        self.edit_url = reverse(
            "main:update_education", args=[self.education.pk]
        )
        self.delete_url = reverse(
            "main:delete_education", args=[self.education.pk]
        )
        self.star_url = reverse(
            "main:toggle_education_star", args=[self.education.pk]
        )
        self.payload = {
            "institution": "Updated University",
            "program": "Computer Science",
            "start_year": 2025,
            "end_year": "",
            "website": "",
            "description": "Updated by an authorized user.",
        }

    def test_public_reads_and_anonymous_actions(self):
        for url in (
            self.list_url,
            self.detail_url,
            reverse("main:get_education_json"),
        ):
            self.assertEqual(self.client.get(url).status_code, 200)

        for url in (
            self.create_url,
            self.edit_url,
            self.delete_url,
            self.star_url,
        ):
            for method in ("get", "post"):
                response = getattr(self.client, method)(url)
                self.assertRedirects(
                    response,
                    f"{reverse('main:login')}?next={url}",
                    fetch_redirect_response=False,
                )

        self.education.refresh_from_db()
        self.assertEqual(self.education.institution, "Test University")
        self.assertEqual(self.education.starred_by.count(), 0)

    def test_member_cannot_write(self):
        self.client.force_login(self.member)
        for url in (self.create_url, self.edit_url, self.delete_url):
            for method in ("get", "post"):
                response = getattr(self.client, method)(
                    url, self.payload if method == "post" else {}
                )
                self.assertEqual(response.status_code, 403)

        self.education.refresh_from_db()
        self.assertEqual(self.education.institution, "Test University")
        self.assertEqual(Education.objects.count(), 1)

    def test_editor_can_only_update(self):
        self.client.force_login(self.editor)
        self.assertEqual(self.client.get(self.edit_url).status_code, 200)
        self.assertRedirects(
            self.client.post(self.edit_url, self.payload),
            self.detail_url,
        )
        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution, "Updated University"
        )

        for url in (self.create_url, self.delete_url):
            for method in ("get", "post"):
                response = getattr(self.client, method)(
                    url, self.payload if method == "post" else {}
                )
                self.assertEqual(response.status_code, 403)

        self.assertEqual(Education.objects.count(), 1)

    def test_controls_match_roles(self):
        for user, can_edit, can_manage in (
            (None, False, False),
            (self.member, False, False),
            (self.editor, True, False),
            (self.owner, True, True),
        ):
            self.client.logout()
            if user:
                self.client.force_login(user)

            listing = self.client.get(self.list_url)
            detail = self.client.get(self.detail_url)
            self.assertEqual(
                f'href="{self.create_url}"' in listing.content.decode(),
                can_manage,
            )
            self.assertEqual(
                f'href="{self.edit_url}"' in detail.content.decode(),
                can_edit,
            )
            self.assertEqual(
                f'action="{self.delete_url}"' in detail.content.decode(),
                can_manage,
            )

    def test_all_authenticated_roles_can_toggle_star(self):
        for user in (self.member, self.editor, self.owner):
            self.client.force_login(user)
            self.assertEqual(
                self.client.get(self.star_url).status_code, 405
            )
            self.assertRedirects(
                self.client.post(self.star_url), self.list_url
            )
            self.assertEqual(self.education.starred_by.count(), 1)

            # The relation itself also prevents duplicate membership.
            self.education.starred_by.add(user)
            self.assertEqual(self.education.starred_by.count(), 1)

            item = self.client.get(
                self.list_url
            ).context["education_list"][0]
            self.assertEqual(item.star_count, 1)
            self.assertTrue(item.is_starred)

            self.client.post(self.star_url)
            self.assertEqual(self.education.starred_by.count(), 0)

    def test_star_requires_csrf_token(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.member)
        self.assertEqual(client.post(self.star_url).status_code, 403)
        self.assertEqual(self.education.starred_by.count(), 0)

    def test_owner_get_cannot_delete(self):
        self.client.force_login(self.owner)
        self.assertEqual(self.client.get(self.delete_url).status_code, 405)
        self.assertTrue(
            Education.objects.filter(pk=self.education.pk).exists()
        )

    def test_json_excludes_star_users(self):
        self.education.starred_by.add(self.member)
        response = self.client.get(reverse("main:get_education_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            set(response.json()[0]["fields"]),
            {
                "institution", "program", "start_year",
                "end_year", "website", "description",
            },
        )

    def test_sort_by_stars(self):
        other = Education.objects.create(
            institution="Older Popular University",
            start_year=2020,
        )
        other.starred_by.add(self.member)
        response = self.client.get(self.list_url, {"sort": "stars"})
        items = response.context["education_list"]
        self.assertEqual(items[0].pk, other.pk)
        self.assertEqual(items[0].star_count, 1)

    def test_projects_json_still_works(self):
        from main.models import Project

        project = Project.objects.create(
            title="Test Project",
            description="Test",
            tech_stack="Django",
        )
        project.starred_by.add(self.member)
        response = self.client.get(reverse("main:get_projects_json"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("starred_by", response.json()[0]["fields"])