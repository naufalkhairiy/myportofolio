import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from main.models import Education


class Tugas5BackendTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="tugas5_owner",
            password="testpass123",
            is_superuser=True,
            is_staff=True,
        )

        self.member = User.objects.create_user(
            username="tugas5_member",
            password="testpass123",
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            program="S1 Ilmu Komputer",
            start_year=2025,
            website="https://www.ui.ac.id/",
            description="Computer Science.",
        )

        self.ajax_create_url = reverse(
            "main:create_education_ajax"
        )

    def test_education_json_contains_ajax_and_star_data(self):
        response = self.client.get(
            reverse("main:get_education_json")
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertIn("pk", data[0])

        fields = data[0]["fields"]

        self.assertEqual(
            fields["institution"],
            "Universitas Indonesia",
        )

        self.assertIn("star_count", fields)
        self.assertIn("is_starred", fields)

    def test_ajax_create_rejects_unauthorized_user(self):
        response = self.client.post(
            self.ajax_create_url,
            {
                "institution": "Test University",
                "program": "Computer Science",
                "start_year": 2026,
            },
        )

        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.member)

        response = self.client.post(
            self.ajax_create_url,
            {
                "institution": "Test University",
                "program": "Computer Science",
                "start_year": 2026,
            },
        )

        self.assertEqual(response.status_code, 403)

    def test_ajax_create_returns_201_for_valid_data(self):
        self.client.force_login(self.owner)

        response = self.client.post(
            self.ajax_create_url,
            {
                "institution": "Test University",
                "program": "Computer Science",
                "start_year": 2026,
                "end_year": "",
                "website": "https://example.com/",
                "description": "Test education.",
            },
        )

        self.assertEqual(response.status_code, 201)

        self.assertTrue(
            Education.objects.filter(
                institution="Test University"
            ).exists()
        )

    def test_ajax_create_returns_400_for_xss_only_name(self):
        self.client.force_login(self.owner)

        response = self.client.post(
            self.ajax_create_url,
            {
                "institution": (
                    '<img src="x" '
                    'onerror="alert(\'XSS!\')">'
                ),
                "program": "Computer Science",
                "start_year": 2026,
                "end_year": "",
                "website": "",
                "description": "Test",
            },
        )

        self.assertEqual(response.status_code, 400)

        self.assertIn(
            "institution",
            response.json()["errors"],
        )


class Tugas5BrowserTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        cls.driver = webdriver.Chrome(
            options=options
        )

        cls.wait = WebDriverWait(
            cls.driver,
            10,
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        self.owner = User.objects.create_user(
            username="browser_owner",
            password="testpass123",
            is_superuser=True,
            is_staff=True,
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            program="S1 Ilmu Komputer",
            start_year=2025,
            website="https://www.ui.ac.id/",
            description="Computer Science.",
        )

        # Buka domain dulu agar cookie browser bisa dibersihkan.
        self.driver.get(self.live_server_url)
        self.driver.delete_all_cookies()

    def open_education(self):
        self.driver.get(
            f"{self.live_server_url}/education/"
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "education-list"),
                "Universitas Indonesia",
            )
        )

    def login_owner(self):
        self.driver.get(
            f"{self.live_server_url}/login/"
        )

        self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "username")
            )
        ).send_keys("browser_owner")

        self.driver.find_element(
            By.NAME,
            "password",
        ).send_keys("testpass123")

        self.driver.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]',
        ).click()

        self.wait.until(
            EC.url_to_be(
                f"{self.live_server_url}/"
            )
        )

    def test_guest_ajax_search_debounce_and_sort(self):
        self.open_education()

        page_url = self.driver.current_url

        # Guest harus tetap bisa membaca Education.
        self.assertIn(
            "Universitas Indonesia",
            self.driver.find_element(
                By.ID,
                "education-list",
            ).text,
        )

        # Guest tidak boleh mendapat tombol Add Education.
        self.assertEqual(
            len(
                self.driver.find_elements(
                    By.CSS_SELECTOR,
                    '[popovertarget="add-education-modal"]',
                )
            ),
            0,
        )

        # Guest mendapat link login untuk star.
        self.assertIn(
            "Login untuk memberi star",
            self.driver.find_element(
                By.ID,
                "education-list",
            ).text,
        )

        # Bungkus fetch untuk menghitung request ke endpoint Education.
        self.driver.execute_script(
            """
            window.__educationFetchCount = 0;
            window.__originalFetch = window.fetch;

            window.fetch = function(...args) {
                const url = String(args[0]);

                if (url.includes('/api/education/')) {
                    window.__educationFetchCount++;
                }

                return window.__originalFetch.apply(
                    this,
                    args
                );
            };
            """
        )

        search_input = self.driver.find_element(
            By.ID,
            "education-search-input",
        )

        search_input.send_keys(
            "Universitas"
        )

        # Sebelum 300ms, debounce seharusnya
        # belum mengirim request.
        time.sleep(0.1)

        self.assertEqual(
            self.driver.execute_script(
                "return window.__educationFetchCount;"
            ),
            0,
        )

        # Setelah debounce selesai, harus ada request.
        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return window.__educationFetchCount;"
            ) == 1
        )

        # AJAX search tidak boleh reload/navigasi halaman.
        self.assertEqual(
            self.driver.current_url,
            page_url,
        )

        # Sorting juga harus melakukan fetch AJAX.
        Select(
            self.driver.find_element(
                By.ID,
                "education-sort",
            )
        ).select_by_value("stars")

        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return window.__educationFetchCount;"
            ) >= 2
        )

        self.assertEqual(
            self.driver.current_url,
            page_url,
        )

    def test_superuser_modal_ajax_toast_and_xss(self):
        self.login_owner()
        self.open_education()

        page_url = self.driver.current_url

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[popovertarget="add-education-modal"]',
                )
            )
        )

        add_button.click()

        modal = self.driver.find_element(
            By.ID,
            "add-education-modal",
        )

        self.wait.until(
            lambda driver:
            driver.execute_script(
                """
                return arguments[0]
                    .matches(':popover-open');
                """,
                modal,
            )
        )

        form = self.driver.find_element(
            By.ID,
            "education-form",
        )

        form.find_element(
            By.NAME,
            "institution",
        ).send_keys(
            "Test University"
        )

        form.find_element(
            By.NAME,
            "program",
        ).send_keys(
            "Computer Science"
        )

        form.find_element(
            By.NAME,
            "start_year",
        ).send_keys(
            "2026"
        )

        form.find_element(
            By.NAME,
            "website",
        ).send_keys(
            "https://example.com/"
        )

        form.find_element(
            By.NAME,
            "description",
        ).send_keys(
            "Created through AJAX."
        )

        form.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]',
        ).click()

        # Data baru harus muncul tanpa reload.
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "education-list"),
                "Test University",
            )
        )

        self.assertEqual(
            self.driver.current_url,
            page_url,
        )

        # Toast success.
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "toast-message"),
                "Education berhasil ditambahkan!",
            )
        )

        # Modal harus tertutup setelah sukses.
        self.wait.until(
            lambda driver:
            not driver.execute_script(
                """
                return arguments[0]
                    .matches(':popover-open');
                """,
                modal,
            )
        )

        # Buka lagi untuk test invalid/XSS.
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[popovertarget="add-education-modal"]',
                )
            )
        )

        add_button.click()

        form = self.driver.find_element(
            By.ID,
            "education-form",
        )

        form.find_element(
            By.NAME,
            "institution",
        ).send_keys(
            '<img src="x" '
            'onerror="alert(\'XSS!\')">'
        )

        form.find_element(
            By.NAME,
            "start_year",
        ).send_keys(
            "2026"
        )

        form.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]',
        ).click()

        # Server-side validation error harus muncul
        # lewat toast merah.
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "toast-message"),
                "Institution tidak boleh hanya "
                "berisi tag HTML",
            )
        )

        # Tetap di halaman Education.
        self.assertEqual(
            self.driver.current_url,
            page_url,
        )

        # Payload tidak boleh memunculkan alert JavaScript.
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            pass
        else:
            self.fail(
                "XSS alert muncul di browser."
            )