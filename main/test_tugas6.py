import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from main.models import Education

class EducationAPITests(APITestCase):

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner6",
            email="owner6@example.com",
            password="testpass123",
        )
        self.member = User.objects.create_user(
            username="member6",
            password="testpass123",
        )
        self.editor = User.objects.create_user(
            username="editor6",
            password="testpass123",
        )

        group = Group.objects.create(name="Editor")
        self.editor.groups.add(group)

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            program="Ilmu Komputer",
            start_year=2025,
            end_year=None,
            website="https://www.ui.ac.id/",
            description="Pendidikan Utama",
        )

        self.list_url = reverse("api:education-list")
        self.detail_url = reverse("api:education-detail", args=[self.education.pk])
        self.star_url = reverse("api:education-star", args=[self.education.pk])

        self.payload = {
            "institution": "Universitas Percobaan",
            "program": "Sistem Informasi",
            "start_year": 2026,
            "end_year": None,
            "website": "https://example.com/",
            "description": "Data uji API",
        }

    def test_guest_can_read_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data[0]["institution"],
            "Universitas Indonesia"
        )
        self.assertEqual(response.data[0]["star_count"], 0)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("email", response.data[0])

        detail = self.client.get(self.detail_url)
        self.assertEqual(detail.status_code, 200)

    def test_search_and_sort(self):
        other = Education.objects.create(
            institution="Sekolah Lain",
            start_year=2026,
        )

        self.education.starred_by.add(
            self.member, self.editor
        )
        other.starred_by.add(self.owner)

        response = self.client.get(
            self.list_url,
            {"institution": "universitas"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["institution"],
            "Universitas Indonesia",
        )

        empty = self.client.get(
            self.list_url,
            {"institution": "tidakada"},
        )
        self.assertEqual(empty.data, [])

        sorted_response = self.client.get(
            self.list_url,
            {"sort": "stars"},
        )
        self.assertEqual(sorted_response.status_code, 200)
        self.assertEqual(
            sorted_response.data[0]["institution"],
            "Universitas Indonesia"
        )

    def test_unknown_education_is_404(self):
        missing_url = reverse(
            "api:education-detail",
            args=[uuid.uuid4()],
        )

        response = self.client.get(missing_url)
        self.assertEqual(response.status_code, 404)

    def test_guest_and_member_cannot_write(self):
        for user in (None, self.member):
            with self.subTest(
                user=user.username if user else "guest"
            ):
                self.client.force_authenticate(user=user)

                created = self.client.post(
                    self.list_url,
                    self.payload,
                    format="json",

                )
                self.assertEqual(created.status_code, 403)

                updated= self.client.patch(
                    self.detail_url,
                    {"institution":"Diubah"},
                    format="json",
                )
                self.assertEqual(updated.status_code, 403)

                replaced = self.client.put(
                    self.detail_url,
                    self.payload,
                    format="json",
                )
                self.assertEqual(replaced.status_code, 403)

                deleted = self.client.delete(self.detail_url)
                self.assertEqual(deleted.status_code, 403)

                self.education.refresh_from_db()
                self.assertEqual(
                    self.education.institution,
                    "Universitas Indonesia",
                )
                self.assertEqual(Education.objects.count(), 1)

    def test_editor_permissions(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"institution": "Institut Baru"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution,
            "Institut Baru",
        )
        self.assertEqual(self.education.start_year, 2025)

        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution,
            "Universitas Percobaan",
        )

        created = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        deleted = self.client.delete(self.detail_url)

        self.assertEqual(created.status_code, 403)
        self.assertEqual(deleted.status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution,
            "Universitas Percobaan",
        )

    def test_owner_can_create_update_delete(self):
        self.client.force_authenticate(user=self.owner)

        created = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(created.status_code, 201)

        new_id = created.data["id"]
        self.assertTrue(
            Education.objects.filter(pk=new_id).exists()
        )

        new_detail_url = reverse(
            "api:education-detail",
            args=[new_id],
        )

        updated = self.client.patch(
            new_detail_url,
            {"program": "Teknik Informatika"},
            format="json",
        )
        self.assertEqual(updated.status_code, 200)

        self.assertEqual(
            Education.objects.get(pk=new_id).program,
            "Teknik Informatika",
        )

        deleted = self.client.delete(new_detail_url)
        self.assertEqual(deleted.status_code, 204)
        self.assertFalse(
            Education.objects.filter(pk=new_id).exists()
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        invalid_cases = [
            ({"institution": "  "}, "institution"),
            ({
                "institution":
                '<img src="x" onerror="alert(1)">'
            }, "institution"),
            ({
                "website":"javascript:alert(1)"
            }, "website"),
        ]

        for changes, field in invalid_cases:
            with self.subTest(field=field, changes= changes):
                response = self.client.post(
                    self.list_url,
                    {**self.payload, **changes},
                    format="json",
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn(field, response.data)
                self.assertEqual(Education.objects.count(), 1)

    def test_strip_tags(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "institution": "  <b>Kampus Baru </b> ",
                "description" : "  <b>Pengalaman</b>"
            },
            format="json"
        )

        self.assertEqual(response.status_code,201)
        self.assertEqual(
            response.data["institution"],
            "Kampus Baru",
        )
        self.assertEqual(
            response.data["description"],
            "Pengalaman",
        )

    def test_star_requires_login_and_toggles(self):
        guest = self.client.post(self.star_url)
        self.assertEqual(guest.status_code, 403)
        self.assertEqual(self.education.starred_by.count(), 0)

        self.client.force_authenticate(user=self.member)

        first = self.client.post(
            self.star_url,
            {"user_id": self.owner.pk},
            format= "json",
        )
        self.assertEqual(first.status_code, 200)
        self.assertTrue(first.data["is_starred"])
        self.assertEqual(first.data["star_count"], 1)

        self.assertTrue(
            self.education.starred_by.filter(
                pk=self.member.pk
            ).exists()
        )
        self.assertFalse(
            self.education.starred_by.filter(
                pk=self.owner.pk
            ).exists()
        )

        second = self.client.post(self.star_url)
        self.assertEqual(second.status_code, 200)
        self.assertFalse(second.data["is_starred"])
        self.assertEqual(second.data["star_count"], 0)

    def test_computed_fields_read_only(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "star_count":999,
                "is_starred": True,
                "starred_by": [self.member.pk],
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

        created = Education.objects.get(
            pk = response.data["id"]

        )
        self.assertEqual(created.starred_by.count(), 0)

    def test_csrf_without_token(self):
        client = APIClient(enforce_csrf_checks=True)

        self.assertTrue(client.login(
            username = "owner6",
            password="testpass123"
        ))

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution,
            "Universitas Indonesia",
        )

    
    def test_csrf_with_token(self):
        client = APIClient(enforce_csrf_checks=True)

        self.assertTrue(client.login(
            username="owner6",
            password="testpass123",
        ))

        # Buka halaman untuk mendapatkan CSRF cookie
        page = client.get(reverse("main:show_education"))
        self.assertEqual(page.status_code, 200)

        # Ambil token dari cookie
        self.assertIn("csrftoken", client.cookies)
        token = client.cookies["csrftoken"].value

        # Kirim POST dengan token CSRF
        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            headers={"X-CSRFToken": token},
        )

        # Tampilkan respons kalau gagal
        if response.status_code != 201:
            print("CSRF DEBUG:", response.status_code, response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Education.objects.count(), 2)
