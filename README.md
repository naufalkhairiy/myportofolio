# My Portfolio

Situs web portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia.

## Author

- Name: Naufal Khairiy Zulkarnain Sormin
- NPM: 2506621850
- Class: PBP D

## Project Description

Project ini merupakan website portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia. Website ini dibangun menggunakan Django, HTML, CSS, dan JavaScript serta dikembangkan secara bertahap mengikuti materi tutorial dan tugas mingguan.

Pada tahap awal, website berisi halaman profil statis dengan informasi pribadi, social links, dan riwayat pendidikan. Pada pengembangan berikutnya, website mulai menerapkan arsitektur Model-View-Template (MVT) Django untuk mengelola data secara dinamis melalui database.

Saat ini, data Experience, Education, dan Project dikelola menggunakan Django Model. Halaman Education menggunakan AJAX untuk mengambil data dari endpoint JSON `/api/education/` melalui Fetch API sehingga pencarian, pengurutan, penambahan data, serta Star dan Unstar dapat dilakukan tanpa full page reload. Education juga memiliki halaman detail untuk setiap riwayat pendidikan.

Website dilengkapi autentikasi dan otorisasi berbasis role, responsive design, navigation bar, feedback menggunakan toast, loading/error/empty state, proteksi CSRF, serta perlindungan XSS pada data yang dirender melalui JavaScript.

## Main Features

- Informasi profil pribadi dan foto.
- Informasi NPM dan program studi.
- Social links menuju GitHub, LinkedIn, dan email.
- Halaman Experience yang mengambil data dari database menggunakan Django Model.
- Halaman Education dinamis yang menampilkan seluruh riwayat pendidikan dari database.
- Halaman detail untuk setiap Education menggunakan UUID.
- Empty state ketika belum terdapat data Education atau Experience.
- External link menuju website institusi pendidikan.
- Django Admin untuk mengelola data Experience dan Education.
- Navigation bar menggunakan named URL Django.
- Hover effect dan transition pada beberapa elemen.
- Responsive layout untuk desktop dan perangkat mobile.
- Unit test untuk memverifikasi URL, template, data model, empty state, serta logic model.
- Project management menggunakan Django `ModelForm`.
- Create dan Delete Project melalui antarmuka web.
- Data Project tersedia melalui endpoint JSON dan ditampilkan secara dinamis menggunakan AJAX.
- Education dapat dibuat, diperbarui, dan dihapus melalui antarmuka web.
- `EducationForm` menggunakan Django `ModelForm`.
- Data Education tersedia melalui endpoint JSON.
- Halaman Education mengambil data dari endpoint `/api/education/` menggunakan Fetch API dan merendernya secara dinamis tanpa full page reload.
- Pencarian Education berdasarkan nama institusi.
- Reusable form template untuk Create dan Update Education.
- Confirmation modal sebelum menghapus Education.
- Success feedback menggunakan Django Messages.
- Unit test untuk CRUD, JSON data delivery, filtering, dan search Education.
- Pencarian Education menggunakan AJAX dengan debouncing 300 ms.
- Pengurutan Education berdasarkan tahun terbaru atau jumlah Star tanpa reload halaman.
- Loading state, error state, dan empty state pada daftar Education.
- Form Add Education ditampilkan melalui modal dan dikirim menggunakan AJAX.
- Feedback keberhasilan dan kegagalan AJAX ditampilkan menggunakan reusable toast.
- Request POST AJAX dilindungi menggunakan CSRF token melalui header `X-CSRFToken`.
- Data yang dimasukkan ke `innerHTML` di-escape menggunakan `escapeHtml()`.
- Input teks Education juga dibersihkan pada server melalui method `clean_<field>()` dan `strip_tags()`.
- Star dan Unstar Education dapat dilakukan melalui AJAX tanpa full page reload sebagai fitur interaktivitas tambahan.
- Automated test menggunakan Django TestCase dan Selenium headless untuk memverifikasi backend serta perilaku AJAX pada browser.

## Technologies Used

- Python
- Django
- Django Template Language (DTL)
- HTML5
- JavaScript
- Fetch API
- CSS3
- CSS Grid
- Flexbox
- SQLite untuk development lokal
- PostgreSQL pada deployment PWS
- Git dan GitHub
- Selenium WebDriver untuk automated browser testing

## How to Run Locally

1. Clone repository ini.

```bash
git clone https://github.com/naufalkhairiy/myportofolio.git
```

2. Masuk ke direktori project.

```bash
cd myportofolio
```

3. Buat virtual environment.

```bash
python -m venv env
```

4. Aktifkan virtual environment.

### Windows

```bash
env\Scripts\activate
```

### Linux/macOS

```bash
source env/bin/activate
```

5. Install dependency yang diperlukan.

```bash
pip install -r requirements.txt
```

6. Terapkan database migration.

```bash
python manage.py migrate
```

7. Jalankan automated test aktif untuk Tugas 5.

```bash
python manage.py test main.test_tugas5 -v 2
```

8. Jalankan Django development server.

```bash
python manage.py runserver
```

9. Buka alamat berikut melalui browser:

```text
http://localhost:8000/
```

Halaman utama dapat diakses melalui URL tersebut, sedangkan halaman lain dapat diakses melalui:

```text
http://localhost:8000/experience/
http://localhost:8000/education/
```

## Weekly Progress

### Project Setup

- Membuat project Django dan struktur dasar project.
- Mengatur Git dan GitHub repository.
- Mengatur deployment project ke PWS.
- Menambahkan static files dan konfigurasi yang diperlukan.
- Memastikan project dapat dijalankan melalui Django development server.

### Tutorial 1

- Membuat halaman utama portfolio.
- Menambahkan informasi profil pribadi dan foto.
- Menambahkan NPM dan program studi.
- Menambahkan social links seperti GitHub, LinkedIn, dan email.
- Menggunakan CSS Grid dan Flexbox untuk mengatur layout.
- Menambahkan responsive design agar tampilan dapat menyesuaikan perangkat mobile.

### Tugas 1

- Menambahkan section Education yang berisi riwayat pendidikan.
- Menampilkan nama institusi, jenjang atau program pendidikan, dan periode pendidikan.
- Menggunakan CSS Grid untuk menampilkan informasi Education dalam tiga kolom pada desktop.
- Mengubah layout Education menjadi satu kolom pada layar mobile menggunakan media query.
- Menambahkan hover effect dan transition pada Education item.
- Menambahkan smooth scrolling pada navigation bar.
- Menambahkan external link pada institusi pendidikan.
- Membuat indikator external link berbentuk panah yang hanya muncul ketika Education item di-hover.
- Menguji tampilan website melalui localhost pada ukuran desktop dan mobile.
- Melakukan perubahan secara bertahap menggunakan Git branch dan commit yang terpisah.

### Tutorial 2

- Membuat aplikasi `main` dan menerapkan pola Model-View-Template (MVT) pada Django.
- Membuat model `Experience` untuk menyimpan data pengalaman pada database.
- Membuat dan menjalankan migration untuk model Experience.
- Membuat view untuk mengambil data Experience dari database.
- Membuat halaman Experience menggunakan Django Template Language.
- Menggunakan perulangan template untuk menampilkan seluruh data Experience.
- Menambahkan empty state ketika belum terdapat data Experience.
- Membuat named URL untuk halaman Experience.
- Menambahkan unit test untuk memastikan halaman dan model Experience bekerja dengan benar.
- Menguji pembuatan dan pengelolaan data melalui Django shell.
- Mendaftarkan model Experience pada Django Admin untuk mempermudah pengelolaan data.

### Tugas 2

- Membuat model `Education` untuk menyimpan riwayat pendidikan pada database.
- Menggunakan UUID sebagai primary key pada model Education.
- Menambahkan field `institution`, `program`, `start_year`, `end_year`, `website`, dan `description`.
- Menambahkan method `__str__()` agar object Education ditampilkan menggunakan nama institusi.
- Membuat property `is_current` untuk menentukan apakah pendidikan masih berlangsung berdasarkan nilai `end_year`.
- Membuat dan menerapkan migration untuk model Education.
- Membuat view untuk mengambil seluruh data Education dari database.
- Mengurutkan data Education berdasarkan `start_year` dari yang terbaru menggunakan `order_by("-start_year")`.
- Membuat halaman `/education/` yang menampilkan seluruh data Education menggunakan Django Template Language.
- Menggunakan `{% for %}` untuk melakukan perulangan terhadap data Education.
- Menambahkan `{% empty %}` untuk menampilkan pesan ketika belum terdapat data Education.
- Menggunakan `{% if %}` untuk menampilkan `Present` apabila Education masih berlangsung.
- Menambahkan external link menuju website institusi apabila field `website` tersedia.
- Menghubungkan halaman Education melalui navigation bar menggunakan named URL Django.
- Menghapus riwayat Education yang sebelumnya ditulis secara hard-coded pada halaman Profile.
- Mendaftarkan model Education pada Django Admin.
- Menambahkan data Education melalui Django shell.
- Menambahkan unit test untuk menguji URL, template, data Education, empty state, dan property `is_current`.
- Membuat halaman detail untuk setiap Education sebagai fitur tambahan.
- Menggunakan UUID Education pada URL halaman detail.
- Menggunakan `get_object_or_404()` untuk mengambil object Education dan menangani data yang tidak ditemukan.
- Menambahkan deskripsi singkat dan external link pada halaman detail Education.
- Menambahkan unit test tambahan untuk halaman detail Education dan response 404.
- Melakukan pengembangan melalui branch `tugas-2-education` dengan commit yang dipisahkan berdasarkan fungsi perubahan.

### Tugas 3

- Melakukan refactoring template dengan menggunakan `base.html` sebagai root template dan template inheritance Django.
- Membuat model `Project` dan `ProjectForm` sebagai bagian dari Tutorial 3.
- Membuat fitur Create dan Delete untuk data Project.
- Membuat endpoint JSON untuk Project dan menampilkan data Project setelah proses deserialisasi JSON.
- Membuat `EducationForm` menggunakan `ModelForm` untuk mengelola data Education.
- Mengimplementasikan fitur Create Education menggunakan form.
- Mengimplementasikan fitur Update Education dengan menggunakan instance dari object Education yang dipilih.
- Mengimplementasikan fitur Delete Education dengan HTTP POST dan CSRF protection.
- Menggunakan kembali satu template `education_form.html` untuk kebutuhan Create dan Update agar tidak terjadi duplikasi template.
- Membuat endpoint `/api/education/` untuk menyediakan data Education dalam format JSON.
- Menggunakan Django serializer untuk melakukan serialization dari QuerySet Education menjadi JSON.
- Melakukan deserialisasi JSON sebelum data Education ditampilkan kembali pada halaman `/education/`.
- Menambahkan fitur pencarian Education berdasarkan nama institusi menggunakan query parameter dan `institution__icontains`.
- Membuat empty state khusus ketika hasil pencarian Education tidak ditemukan.
- Menambahkan tombol Add Education, Edit Education, dan Delete Education pada antarmuka.
- Menambahkan confirmation modal untuk Delete Education agar pengguna tidak menghapus data secara tidak sengaja.
- Menambahkan Django Messages untuk memberikan feedback setelah proses Create, Update, dan Delete berhasil.
- Menambahkan unit test untuk Create, Update, Delete, JSON endpoint, JSON filtering, dan fitur pencarian Education.
- Menjalankan seluruh unit test dan memperbaiki error berdasarkan traceback hingga seluruh test berhasil.
- Mengembangkan Tugas 3 melalui branch `tugas-3-education` dan memisahkan perubahan menjadi beberapa commit berdasarkan fitur.

## Reflections

### Tugas 1

#### 1. Apakah saya menggunakan semantic HTML5 dan bagaimana elemen tersebut membantu struktur static web?

Ya, saya menggunakan semantic HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<footer>`.

Elemen tersebut membantu saya membedakan fungsi dari setiap bagian halaman sehingga struktur website menjadi lebih jelas dan terorganisir. Contohnya, bagian Education menggunakan `<section>` karena merupakan satu topik utama, sedangkan setiap riwayat pendidikan menggunakan `<article>` karena masing-masing merupakan satu unit konten tersendiri.

Struktur semantik juga membuat kode lebih mudah dibaca dan dikembangkan dibandingkan jika seluruh bagian hanya menggunakan `<div>`. Selain itu, elemen semantik dapat menjelaskan fungsi suatu bagian halaman tanpa hanya bergantung pada nama class CSS yang digunakan.

#### 2. Apa tantangan dalam membuat responsive layout dan bagaimana saya menentukan elemen yang perlu berubah?

Tantangan yang saya temukan adalah bagaimana menampilkan informasi agar tetap nyaman dilihat pada berbagai ukuran perangkat. Saya menentukan elemen yang perlu berubah dengan melihat ruang yang tersedia serta apakah informasi masih mudah dibaca ketika ukuran layar semakin kecil.

Contohnya, bagian Education menggunakan tiga kolom pada desktop untuk menampilkan institusi, program pendidikan, dan periode pendidikan dalam satu baris. Namun, ketika ditampilkan pada layar HP, tiga kolom tersebut menjadi terlalu sempit.

Karena itu, menggunakan media query saya mengubah Education menjadi satu kolom pada layar yang lebih kecil. Saya tidak hanya mengecilkan ukuran elemen, tetapi juga mengubah susunan layout agar informasi tetap memiliki ruang yang cukup dan mudah dibaca.

#### 3. Apa keterbatasan static web dan bagaimana saya ingin mengembangkannya menjadi web dinamis?

Saya merasakan keterbatasan pada static web karena untuk mengubah atau menambahkan data saya masih harus mengedit kode HTML secara manual.

Cara tersebut masih cukup mudah ketika jumlah data masih sedikit, tetapi akan semakin sulit dikelola apabila isi portfolio terus bertambah. Contohnya, untuk menambahkan riwayat pendidikan atau informasi baru, saya harus kembali membuka source code dan menambahkan elemen HTML secara manual.

Jika dikembangkan menjadi web dinamis, saya ingin data-data tersebut dapat disimpan di database dan dikelola melalui Django. Dengan demikian, saya dapat menambahkan, mengubah, atau menghapus data tanpa harus mengedit HTML secara manual setiap kali terdapat perubahan.

### Tugas 2

#### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Jelaskan peran `urls.py` proyek, `urls.py` aplikasi, view, model, dan template.

Ketika pengguna membuka halaman Education, browser mengirim HTTP request menuju URL `/education/`. Request tersebut pertama kali diterima oleh konfigurasi URL pada project Django di `portofolio/urls.py`. File tersebut meneruskan routing menuju URL milik aplikasi `main` menggunakan `include()`.

Selanjutnya, `main/urls.py` mencocokkan URL `/education/` dengan named route `show_education`. Route tersebut kemudian memanggil fungsi `show_education` yang terdapat pada `main/views.py`.

Di dalam view, data diambil dari model `Education` menggunakan Django ORM dengan `Education.objects.all().order_by("-start_year")`. Model `Education` menjadi representasi struktur data pada database, sehingga view tidak perlu berinteraksi langsung dengan SQL.

Data hasil query kemudian dimasukkan ke dalam dictionary `context` dengan nama `education_list`. View meneruskan context tersebut ke `education.html` menggunakan fungsi `render()`.

Template `education.html` menggunakan Django Template Language untuk melakukan perulangan terhadap `education_list`. Untuk setiap object Education, template mengambil field seperti `institution`, `program`, `start_year`, `end_year`, dan `website`. Template juga menggunakan property `is_current` dari model untuk menentukan apakah periode pendidikan harus ditampilkan sebagai `Present` atau menggunakan tahun selesai.

Setelah template selesai dirender oleh Django menjadi HTML, response dikirim kembali ke browser dan hasil akhirnya ditampilkan kepada pengguna.

Secara ringkas, alurnya adalah:

`Browser Request → project urls.py → application urls.py → View → Model/Database → Context → Template → HTTP Response → Browser`.

#### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Menyimpan data pada model membuat data dan tampilan memiliki tanggung jawab yang berbeda. Model bertugas menyimpan dan merepresentasikan data, sedangkan template bertugas menentukan bagaimana data tersebut ditampilkan kepada pengguna.

Pada Tugas 1, riwayat Education masih ditulis secara langsung di dalam `index.html`. Cara tersebut dapat digunakan untuk website statis yang sangat sederhana, tetapi setiap perubahan data mengharuskan saya membuka dan mengubah source code HTML.

Pada Tugas 2, Education dipindahkan ke model dan database. Template hanya melakukan perulangan terhadap data yang diberikan oleh view. Dengan cara ini, menambahkan atau mengubah Education tidak memerlukan perubahan struktur HTML.

Pendekatan ini juga mengurangi duplikasi data dan membuat aplikasi lebih mudah dikembangkan. Data yang sama dapat digunakan oleh lebih dari satu view atau template tanpa harus menulis ulang informasi tersebut. Sebagai contoh, object Education yang sama dapat digunakan pada halaman daftar `/education/` dan halaman detail setiap Education.

Model juga memungkinkan penggunaan fitur Django ORM, validation, Django Admin, migration, dan unit test. Karena itu, menyimpan data di model membuat aplikasi lebih mudah dipelihara, dikembangkan, dan diuji dibandingkan menulis data secara hard-coded di template.

#### 3. Apa perbedaan fungsi `makemigrations` dan `migrate` pada Django? Berikan contoh perubahan model yang mengharuskan menjalankan kedua perintah tersebut.

`makemigrations` dan `migrate` memiliki fungsi yang berbeda.

`python manage.py makemigrations` digunakan untuk mendeteksi perubahan pada Django Model dan membuat file migration yang mendeskripsikan perubahan struktur database yang diperlukan. Perintah ini belum langsung mengubah database.

Sementara itu, `python manage.py migrate` digunakan untuk menerapkan file migration tersebut ke database sehingga struktur tabel pada database benar-benar berubah.

Contohnya, ketika saya menambahkan model baru `Education` pada `main/models.py`, saya menjalankan:

```bash
python manage.py makemigrations main
```

Django kemudian membuat file migration `0002_education.py` yang berisi instruksi untuk membuat tabel Education.

Setelah itu saya menjalankan:

```bash
python manage.py migrate
```

Perintah tersebut menerapkan migration sehingga tabel Education benar-benar dibuat pada database.

Perubahan struktur lain seperti menambahkan field baru ke model juga membutuhkan kedua perintah tersebut. Sebaliknya, perubahan method Python seperti memperbaiki `__str__()` atau menambahkan property `is_current` tidak membutuhkan migration karena perubahan tersebut tidak mengubah struktur tabel database.

### Tugas 3

#### 1. Jelaskan mengapa kita menggunakan `ModelForm` pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!

`ModelForm` digunakan karena Django dapat membentuk form berdasarkan struktur Model yang sudah tersedia. Dengan demikian, field pada form dapat mengikuti field yang terdapat pada model tanpa harus mendefinisikan kembali seluruh input dan proses validasinya secara manual.

Pada implementasi saya, model `Education` memiliki field seperti `institution`, `program`, `start_year`, `end_year`, `website`, dan `description`. Saya membuat `EducationForm` yang menggunakan model tersebut dan menentukan field yang memang dapat diisi oleh pengguna. Field seperti `id` tidak dimasukkan karena UUID tersebut dibuat secara otomatis oleh Django dan bukan merupakan data yang seharusnya diisi pengguna.

Dengan `ModelForm`, Django juga dapat melakukan validasi berdasarkan tipe field pada model. Sebagai contoh, field `website` berasal dari `URLField`, sehingga data yang diberikan dapat divalidasi sebagai URL. Field tahun juga dapat menggunakan input numerik agar lebih sesuai dengan tipe data pada model.

Keuntungan lain yang saya rasakan adalah proses penyimpanan data menjadi lebih sederhana. Pada Create Education saya dapat menggunakan:

`form.save()`

untuk membuat object baru. Sementara pada Update Education saya menggunakan:

`EducationForm(request.POST or None, instance=education)`

Dengan memberikan `instance`, form yang sama dapat digunakan untuk memperbarui object Education yang sudah ada, bukan membuat object baru. Hal ini membuat kode lebih ringkas serta mengurangi duplikasi antara proses Create dan Update.

Jika form dibuat sepenuhnya secara manual menggunakan HTML, saya perlu mengambil setiap nilai dari `request.POST`, melakukan validasi, mengubah tipe data jika diperlukan, menangani error, kemudian membuat atau memperbarui object secara manual. Cara tersebut memberikan kontrol yang lebih rendah-level, tetapi untuk form yang langsung merepresentasikan Django Model akan menghasilkan lebih banyak kode dan meningkatkan kemungkinan inkonsistensi antara form dan model.

Sementara itu, `{% csrf_token %}` digunakan sebagai perlindungan terhadap Cross-Site Request Forgery (CSRF). CSRF merupakan serangan ketika pengguna yang sudah memiliki sesi pada suatu website dibuat untuk mengirim request yang tidak mereka kehendaki melalui website lain.

Hal ini menjadi penting pada form yang mengubah data, seperti Create, Update, dan Delete Education. Django menyisipkan token ke dalam form melalui `{% csrf_token %}`. Ketika form dikirim dengan metode POST, Django memverifikasi token tersebut sebelum request diproses.

Contohnya, pada Delete Education saya menggunakan form dengan metode POST dan menyertakan `{% csrf_token %}`. Dengan demikian, request penghapusan tidak cukup hanya mengetahui URL endpoint-nya, tetapi juga harus memiliki token CSRF yang valid.

Perlu dibedakan bahwa CSRF token tidak digunakan untuk memvalidasi apakah nilai seperti `start_year` atau `website` benar. Validasi data tersebut merupakan tanggung jawab form. CSRF token secara khusus membantu memastikan bahwa request yang mengubah state aplikasi berasal dari form yang sah dalam konteks aplikasi tersebut.


#### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

JSON dan XML sama-sama dapat digunakan untuk merepresentasikan serta mengirimkan data, tetapi JSON umumnya lebih sesuai untuk kebutuhan aplikasi web modern karena strukturnya lebih ringkas dan dekat dengan struktur data yang digunakan oleh JavaScript.

Sebagai contoh, sebuah Education secara sederhana dapat direpresentasikan menggunakan JSON sebagai pasangan key dan value. Object dan array pada JSON juga memiliki bentuk yang sangat dekat dengan object dan array pada JavaScript. Karena JavaScript banyak digunakan pada frontend web, data JSON dapat diproses dengan relatif langsung.

XML menggunakan struktur berbasis tag. Untuk data yang sama, XML biasanya membutuhkan opening tag dan closing tag sehingga representasinya dapat menjadi lebih panjang. JSON cenderung membutuhkan karakter yang lebih sedikit sehingga payload yang dikirim melalui jaringan dapat lebih ringkas.

JSON juga mudah dibaca oleh manusia untuk data terstruktur yang umum digunakan dalam aplikasi web, misalnya object, array, string, number, boolean, dan null. Banyak framework serta API modern juga memiliki dukungan langsung terhadap JSON.

Pada project saya, endpoint `/api/education/` mengembalikan data Education dalam format JSON. Data tersebut dapat diperiksa melalui browser dan kemudian diproses kembali menggunakan Django deserializer sebelum ditampilkan pada halaman Education.

Walaupun demikian, hal ini tidak berarti XML tidak memiliki kegunaan. XML memiliki fitur seperti attributes, namespaces, schema, dan struktur document-oriented yang dapat berguna pada sistem tertentu atau integrasi yang memang menggunakan XML. Namun, untuk pertukaran data aplikasi web yang sebagian besar membutuhkan object dan array dengan struktur sederhana, JSON biasanya lebih ringan dan lebih praktis.

Karena itu, menurut saya alasan utama JSON lebih sering digunakan bukan sekadar karena sintaksnya lebih pendek, tetapi karena formatnya sesuai dengan pola data aplikasi web modern, mudah diproses oleh JavaScript, serta memiliki dukungan yang luas pada framework dan API.


#### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

Pada implementasi Education saya, proses dimulai ketika browser mengirim request menuju endpoint `/api/education/`. URL tersebut dipetakan oleh `main/urls.py` menuju fungsi view `get_education_json`.

Di dalam view tersebut, Django ORM digunakan untuk mengambil data Education dari database:

`Education.objects.all()`

Jika terdapat query pencarian melalui parameter `institution`, QuerySet tersebut terlebih dahulu difilter menggunakan `institution__icontains`. Setelah itu data diurutkan berdasarkan `start_year`.

Hasil Django ORM tersebut masih berupa QuerySet yang berisi object model `Education`. Object model Django bukan merupakan JSON dan tidak dapat langsung dikirim sebagai response JSON hanya dengan menganggapnya sebagai teks.

Karena itu saya menggunakan Django serializer:

`serializers.serialize("json", educations)`

Serialization adalah proses mengubah object Python atau object model Django menjadi representasi data yang dapat dikirim atau disimpan, dalam kasus ini berupa JSON.

Setelah serialization selesai, JSON dikembalikan menggunakan `HttpResponse` dengan `content_type="application/json"`.

Alurnya secara sederhana adalah:

`HTTP Request → URL Routing → View → Django ORM → QuerySet Education → Serialization → JSON → HttpResponse`

Pada halaman Education saya juga menggunakan proses sebaliknya. Fungsi `show_education` memperoleh response JSON tersebut, mengambil content-nya, melakukan decoding UTF-8, kemudian menjalankan:

`serializers.deserialize("json", ...)`

Hasil deserialisasi kemudian dikonversi kembali menjadi object Education sebelum diberikan sebagai `education_list` pada template.

Dengan demikian, alur halaman Education saya adalah:

`Database → QuerySet → Serialization → JSON → Deserialization → Education Object → Context → Template → Browser`

Serialization diperlukan karena object Django memiliki informasi dan perilaku Python yang tidak merupakan bagian dari standar JSON. JSON hanya dapat merepresentasikan struktur data tertentu seperti object, array, string, number, boolean, dan null. Serializer bertugas mengubah data dari model Django menjadi representasi yang sesuai dengan format tersebut.

Proses ini juga memisahkan representasi internal aplikasi dari format data yang dikirim. Model digunakan oleh Django untuk bekerja dengan database, sedangkan JSON menjadi format pertukaran data yang dapat dikonsumsi oleh browser, JavaScript, aplikasi lain, maupun endpoint API.

## AI Usage Disclosure

Saya menggunakan ChatGPT sebagai alat bantu belajar selama pengembangan project ini. Penggunaan AI dilakukan untuk membantu memahami konsep, debugging, review implementasi, penggunaan Git, serta penyusunan dokumentasi.

Saya tidak langsung menganggap setiap jawaban AI sebagai solusi yang benar. Kode dan saran yang diberikan tetap saya periksa, ketik, jalankan, dan uji pada project sebelum digunakan. Beberapa saran AI juga perlu diperbaiki setelah dibandingkan dengan tutorial, traceback Django, hasil unit test, maupun kondisi source code project.

### Week 1 - Tutorial 1 dan Tugas 1

Pada minggu pertama, saya menggunakan ChatGPT terutama untuk memahami pengembangan static web menggunakan HTML dan CSS.

Beberapa konsep yang saya pelajari dengan bantuan AI antara lain semantic HTML, CSS Grid, Flexbox, `grid-template-columns`, media query, hover, transition, penggunaan unit `rem`, serta perbedaan antara `margin`, `padding`, dan `gap`.

Saya juga menggunakan AI untuk membantu memahami responsive design. Contohnya, bagian Education pada awalnya menggunakan tiga kolom pada desktop. Saya kemudian mempelajari cara mengubah layout tersebut menjadi satu kolom pada layar yang lebih kecil menggunakan media query.

Beberapa keputusan desain tetap saya tentukan sendiri. Salah satunya adalah membuat nama institusi pendidikan dapat diklik menuju website terkait. Saya juga mengusulkan agar indikator external link berbentuk panah tidak selalu terlihat, tetapi hanya muncul ketika pengguna mengarahkan cursor ke Education item.

AI membantu menjelaskan implementasi ide tersebut menggunakan CSS pseudo-element, `opacity`, `transform`, hover, dan transition.

Selama implementasi, saya menemukan bahwa saran AI tidak selalu langsung sesuai dengan kondisi project. Beberapa bagian perlu diperiksa kembali, seperti selector CSS, duplikasi style, penulisan unit CSS, dan penempatan transition.

Karena itu, saya tetap melakukan pengecekan melalui localhost, responsive view browser, `git status`, dan `git diff`. Perubahan juga saya commit secara bertahap agar setiap perubahan dapat dilacak dengan lebih jelas.

#### AI Prompting Log - Week 1

Berikut beberapa contoh prompt yang saya gunakan:

- "Jelaskan fungsi `display: grid`, `grid-template-columns`, `gap`, dan `padding` pada bagian Education agar saya memahami setiap baris CSS yang digunakan."

- "Jelaskan perbedaan `margin`, `padding`, dan `gap` menggunakan contoh yang sederhana."

- "Bagaimana cara membuat bagian Education yang menggunakan tiga kolom di desktop berubah menjadi satu kolom ketika dibuka melalui HP?"

- "Coba cek CSS saya dan jelaskan bagian mana yang salah atau tidak diperlukan, jangan langsung menulis ulang seluruh kode."

- "Bagaimana cara membuat nama Universitas Indonesia pada bagian Education bisa diklik dan mengarah ke website resminya?"

- "Tolong buatkan agar tanda panah external link tidak terlihat saat biasa, tetapi muncul ketika cursor diarahkan ke bagian Education."

- "Jelaskan fungsi `opacity`, `transform`, dan `transition` pada efek tanda panah tersebut agar saya memahami cara kerjanya."

- "Coba cek perubahan Git saya terlebih dahulu dan jelaskan file mana yang sebaiknya dimasukkan ke commit."

- "Bagaimana cara melakukan commit secara bertahap agar Git history saya tetap rapi dan setiap commit mewakili satu perubahan?"

- "Bagaimana cara menjalankan project Django saya di localhost menggunakan virtual environment?"

- "Coba evaluasi README saya berdasarkan kebutuhan Tugas 1 dan jelaskan bagian mana yang masih kurang."

- "Tolong bantu rapikan jawaban refleksi saya tanpa mengubah inti jawaban dan pengalaman yang saya alami selama mengerjakan tugas."

### Week 2 - Tutorial 2 dan Tugas 2

Pada minggu kedua, saya menggunakan ChatGPT terutama untuk memahami pengembangan web dinamis menggunakan Django dan pola Model-View-Template (MVT).

Saya meminta penjelasan secara rinci sebelum menggunakan beberapa konsep yang belum saya pahami, seperti Django Model, `UUIDField`, `primary_key`, `blank`, `null`, `__str__`, `@property`, Django ORM, `Education.objects.all()`, `order_by()`, Django Template Language, `get_object_or_404()`, dan UUID path converter.

AI membantu saya memahami bagaimana data berpindah dari database menuju halaman web melalui alur Model, View, context, dan Template. Saya juga mempelajari perbedaan antara data yang ditulis secara hard-coded pada HTML dengan data yang disimpan dan dikelola menggunakan Django Model.

Pada Tugas 2, saya mengubah bagian Education yang sebelumnya ditulis langsung pada HTML menjadi data dinamis yang berasal dari database. AI membantu menjelaskan proses pembuatan model Education, migration, view, URL routing, template loop, empty state, serta halaman detail Education.

Saya juga menggunakan AI untuk memahami unit testing Django. Test yang dibuat kemudian berhasil menemukan bug nyata pada implementasi saya. Property `is_current` pada Education belum terbaca dengan benar sehingga halaman menampilkan `None` sebagai tahun selesai, bukan `Present`. Setelah melihat hasil test dan traceback, saya memperbaiki model dan menjalankan seluruh test kembali hingga berhasil.

Dalam proses pengerjaan, saya juga menemukan beberapa contoh ketika saran AI perlu dikoreksi. Salah satunya adalah ketika AI menyarankan penggunaan Django Admin untuk memasukkan data lokal, sedangkan setelah saya meminta AI memeriksa Tutorial 2 kembali, metode yang digunakan pada tutorial adalah Django shell. Saya kemudian menggunakan workflow Django shell agar lebih sesuai dengan materi tutorial.

Kesalahan lain ditemukan ketika query Education ditulis sebagai `Education.objects.all.order_by(...)`. Setelah menjalankan project, Django menampilkan error karena `all` masih merupakan method dan belum dipanggil. Saya kemudian memperbaikinya menjadi `Education.objects.all().order_by(...)`.

Saat memasukkan data Education, beberapa external link institusi juga sempat tidak ikut dimasukkan. Saya membandingkannya kembali dengan implementasi Education pada Tugas 1 dan kemudian memperbarui data menggunakan link yang sebelumnya sudah digunakan.

Saya menggunakan AI untuk membantu review Git history dan memisahkan perubahan menjadi beberapa commit berdasarkan tujuan, seperti perubahan model, routing, template, testing, admin registration, dan refactoring.

Untuk fitur tambahan, saya membuat halaman detail bagi setiap Education menggunakan UUID. View menggunakan `get_object_or_404()` sehingga request dengan Education yang tidak tersedia dapat menghasilkan response 404 dengan benar. Fitur tambahan tersebut juga diuji melalui unit test.

Secara keseluruhan, penggunaan AI pada Week 2 lebih berfokus pada pemahaman alur Django, debugging, testing, dan evaluasi implementasi. Saya tetap memverifikasi setiap perubahan melalui traceback, unit test, browser, dokumentasi tugas, `git status`, dan source code project sebelum melakukan commit.

#### AI Prompting Log - Week 2

Berikut beberapa contoh prompt yang saya gunakan:

- "Jelaskan secara detail setiap baris pada model Education karena saya ingin memahami fungsi `UUIDField`, `primary_key`, `blank`, `null`, `__str__`, dan `@property` sebelum menuliskannya."

- "Kenapa `Education.objects.all.order_by()` menghasilkan error dan apa perbedaan `all` dengan `all()`?"

- "Jelaskan per baris bagaimana Django Template Language pada `education.html` bekerja, terutama `{% for %}`, `{% empty %}`, `{% if %}`, dan `{{ variable }}`."

- "Bantu saya mengubah data Education yang sebelumnya hard-coded di HTML menjadi data dari Django Model dan database."

- "Kenapa Education object saya tampil sebagai `Education object (UUID)` dan bukan nama institusi?"

- "Cek error unit test saya yang mengatakan Education tidak memiliki `is_current` dan jelaskan kenapa halaman menampilkan `None` bukan `Present`."

- "Bantu saya membuat unit test untuk halaman Education yang menguji URL, template, data model, empty state, dan logic `is_current`."

- "Jelaskan cara membuat halaman detail Education menggunakan UUID dan `get_object_or_404()`."

- "Bantu saya membuat test untuk halaman detail Education dan memastikan UUID yang tidak ditemukan menghasilkan 404."

- "Bandingkan cara memasukkan data lokal dengan Tutorial 2 karena saya ingin mengikuti workflow tutorial."

- "Cek Git status saya dan bantu menentukan perubahan mana yang sebaiknya dipisahkan menjadi commit agar history tetap rapi."

- "Audit project saya dan jelaskan requirement Tugas 2 mana yang sudah selesai serta bagian mana yang masih perlu dikerjakan."

- "Bantu saya memperbarui README Tugas 2 berdasarkan implementasi yang benar-benar sudah saya kerjakan."

### Week 3 - Tutorial 3 dan Tugas 3

Pada minggu ketiga, saya menggunakan ChatGPT sebagai alat bantu untuk memahami konsep Django Form, `ModelForm`, serialization, deserialization, JSON data delivery, CRUD, URL routing, serta unit testing untuk fitur-fitur tersebut.

Saya berusaha menggunakan AI sebagai alat untuk menjelaskan konsep dan melakukan review, bukan hanya sebagai generator kode. Sebelum menggunakan beberapa implementasi, saya meminta penjelasan per baris agar memahami hubungan antara Model, Form, View, URL, Template, serta data yang dikirim melalui request.

Pada pembuatan `EducationForm`, saya mempelajari bagaimana `ModelForm` menghubungkan form dengan model `Education`, fungsi `fields`, `labels`, `widgets`, dan alasan field otomatis seperti UUID tidak dimasukkan ke dalam form. Saya juga mengubah widget untuk `start_year` dan `end_year` menjadi `NumberInput` agar bentuk input lebih sesuai dengan tipe data yang digunakan.

Saya menggunakan kembali satu template `education_form.html` untuk Create dan Update Education. Perbedaannya dikendalikan melalui context seperti `page_title` dan `submit_label`. Untuk Update, saya mempelajari fungsi `instance=education` pada `ModelForm` agar `form.save()` memperbarui object yang sudah ada dan tidak membuat record baru.

AI juga membantu menjelaskan proses serialization dan deserialization. Pada endpoint Education, QuerySet diubah menjadi JSON menggunakan Django serializer. Data tersebut kemudian dideserialisasi kembali sebelum diberikan kepada template Education. Saya menggunakan fitur tersebut bersamaan dengan pencarian berdasarkan nama institusi.

Selain requirement utama, saya menambahkan beberapa peningkatan UX. Halaman Education memiliki search bar, feedback menggunakan Django Messages setelah operasi Create, Update, dan Delete, serta confirmation modal sebelum Education dihapus.

Selama pengerjaan, saya menemukan bahwa saran dan kode dari AI tidak selalu langsung benar. Karena itu, traceback Django dan unit test tetap menjadi sumber utama untuk memverifikasi implementasi.

Salah satu error terjadi ketika nama URL route ditulis sebagai `create education` menggunakan spasi, sedangkan template memanggil `main:create_education`. Hal tersebut menghasilkan `NoReverseMatch`. Saya memperbaiki penamaan route agar konsisten menggunakan underscore.

Saya juga menemukan beberapa kesalahan kecil pada implementasi yang menyebabkan error berantai, seperti nama template `education_forms.html` yang tidak sesuai dengan file sebenarnya `education_form.html`, typo `paget_title` pada context, penggunaan variabel `education` dan `educations` yang tidak konsisten, serta Django lookup yang seharusnya menggunakan `institution__icontains`.

Pada implementasi JSON, saya sempat menulis `start__year` pada `order_by`, padahal nama field sebenarnya adalah `start_year`. Django membaca double underscore sebagai pemisah lookup sehingga muncul `FieldError`. Error tersebut diperbaiki setelah saya membaca traceback dan mencocokkannya kembali dengan model Education.

Unit test juga menemukan beberapa kesalahan yang tidak terlihat hanya dari tampilan browser. Contohnya, saya sempat menggunakan `self.Education` padahal object test bernama `self.education`, serta menggunakan `json.load()` terhadap `response.content`. Setelah mempelajari perbedaannya, saya menggantinya dengan `json.loads()` karena `response.content` merupakan data bytes, bukan file object.

Saya juga menemukan bahwa sebuah test search awalnya memberikan false failure. Test menggunakan `assertNotContains(response, "Universitas Indonesia")`, padahal string tersebut tetap terdapat pada footer website walaupun card Universitas Indonesia sudah berhasil difilter dari hasil pencarian. Saya kemudian memperbaiki test agar memeriksa `education_list` pada context secara langsung. Menurut saya perubahan tersebut menghasilkan test yang lebih tepat karena menguji data hasil filtering, bukan seluruh teks HTML yang dapat memiliki string yang sama untuk alasan lain.

Saat menambahkan global success message pada `base.html`, saya juga sempat lupa menutup blok `{% if messages %}` menggunakan `{% endif %}`. Karena hampir semua halaman melakukan extend terhadap `base.html`, satu kesalahan tersebut menyebabkan banyak test terlihat gagal sekaligus. Setelah membaca traceback, saya mengetahui bahwa error-error tersebut sebenarnya memiliki satu akar masalah yang sama dan memperbaiki root template tersebut.

Pengalaman ini menunjukkan keterbatasan penggunaan AI dalam debugging. AI dapat membantu membaca traceback dan menjelaskan kemungkinan penyebab error, tetapi saran masih dapat mengandung typo, asumsi yang tidak sesuai dengan kondisi source code, atau solusi yang perlu disesuaikan. Karena itu saya tidak menggunakan keberhasilan menghasilkan kode sebagai indikator bahwa implementasi sudah benar.

Setiap perubahan tetap saya validasi menggunakan `python manage.py check`, `python manage.py test main`, pengujian manual melalui browser, serta pemeriksaan `git diff` dan `git status`. Saya juga melakukan commit secara bertahap menggunakan branch `tugas-3-education` agar perubahan dapat ditelusuri berdasarkan fitur.

#### AI Prompting Log - Week 3

Berikut beberapa contoh prompt yang saya gunakan selama Tutorial 3 dan Tugas 3:

- "Jelaskan `ModelForm` baris per baris dan hubungan antara `model`, `fields`, `labels`, dan `widgets` menggunakan bahasa sederhana."

- "Kenapa field UUID tidak perlu dimasukkan ke dalam `EducationForm`?"

- "Apakah `start_year` dan `end_year` sebaiknya menggunakan `TextInput` atau `NumberInput`? Jelaskan alasannya berdasarkan tipe field pada model."

- "Jelaskan fungsi `request.POST or None` pada Django Form dan apa yang terjadi ketika halaman pertama kali dibuka dibandingkan ketika form disubmit."

- "Jelaskan perbedaan proses Create dan Update menggunakan `ModelForm`."

- "Apa fungsi `instance=education` pada `EducationForm`, dan apa yang terjadi jika parameter tersebut tidak diberikan saat melakukan Update?"

- "Bagaimana cara menggunakan satu template `education_form.html` untuk Create dan Update agar tidak membuat dua template yang isinya hampir sama?"

- "Jelaskan fungsi `page_title` dan `submit_label` yang dikirim melalui context ke template form."

- "Kenapa operasi Delete sebaiknya menggunakan request POST, bukan GET?"

- "Jelaskan fungsi `{% csrf_token %}` dan kenapa token tersebut diperlukan pada form Create, Update, dan Delete."

- "Cek error `NoReverseMatch` saya dan jelaskan hubungan antara `name` pada `urls.py` dengan `{% url %}` pada template."

- "Kenapa `name='create education'` tidak dapat dipanggil menggunakan `main:create_education`?"

- "Bantu saya membaca traceback `TemplateDoesNotExist` dan mencari perbedaan antara nama template pada view dengan nama file sebenarnya."

- "Kenapa typo `paget_title` menyebabkan judul pada form Edit tidak tampil?"

- "Kenapa penggunaan variabel `education` dan `educations` yang tidak konsisten dapat menghasilkan `UnboundLocalError`?"

- "Jelaskan fungsi `institution__icontains` pada Django ORM dan kenapa digunakan dua underscore."

- "Bagaimana cara membuat fitur pencarian Education berdasarkan nama institusi menggunakan query parameter GET?"

- "Bagaimana cara menampilkan empty state yang berbeda ketika database benar-benar kosong dan ketika hasil search tidak ditemukan?"

- "Jelaskan serialization menggunakan Django `serializers.serialize()` secara baris per baris."

- "Mengapa QuerySet atau object Django Model perlu diserialisasi sebelum dikembalikan dalam bentuk JSON?"

- "Jelaskan perbedaan serialization dan deserialization menggunakan contoh data Education."

- "Kenapa hasil `serializers.deserialize()` masih perlu diambil menggunakan `.object` sebelum diberikan ke template?"

- "Bagaimana cara mempertahankan fitur pencarian Education setelah data halaman harus melalui proses JSON serialization dan deserialization?"

- "Kenapa `order_by('-start__year')` menghasilkan `FieldError` sedangkan field pada model saya bernama `start_year`?"

- "Jelaskan kapan double underscore pada Django ORM memang diperlukan dan kapan underscore biasa harus digunakan."

- "Bantu saya membuat endpoint `/api/education/` yang mengembalikan data Education dalam format JSON."

- "Bagaimana cara mengecek endpoint JSON menggunakan browser dan memastikan `Content-Type` response adalah `application/json`?"

- "Bantu saya membuat unit test untuk Create Education menggunakan Django test client."

- "Jelaskan cara menguji Update Education dan fungsi `refresh_from_db()` setelah melakukan POST."

- "Bantu saya membuat test untuk Delete Education dan memastikan object benar-benar sudah hilang dari database."

- "Bagaimana cara membuat unit test untuk endpoint JSON dan mengecek isi field `institution`?"

- "Apa perbedaan `json.load()` dan `json.loads()` dan kenapa `response.content` harus diproses menggunakan `json.loads()`?"

- "Kenapa test saya gagal ketika menggunakan `self.Education.id`, padahal object dibuat di `setUp()`?"

- "Search Education saya sudah bekerja di browser, tetapi `assertNotContains(response, 'Universitas Indonesia')` masih gagal. Bantu saya mencari penyebabnya."

- "Apakah lebih tepat menguji seluruh HTML response atau memeriksa `education_list` pada response context untuk fitur search?"

- "Cek hasil `python manage.py test main` saya dan bantu kelompokkan error berdasarkan akar masalah agar saya tidak memperbaiki setiap traceback secara terpisah."

- "Kenapa satu kesalahan pada `base.html` dapat menyebabkan banyak unit test terlihat gagal sekaligus?"

- "Jelaskan error `Unclosed tag: if` pada Django Template Language dan cara menentukan `{% endif %}` yang hilang."

- "Bagaimana cara menggunakan Django Messages agar pengguna mendapat feedback setelah Create, Update, dan Delete berhasil?"

- "Bantu saya membuat confirmation modal sebelum Delete Education agar tidak hanya menggunakan popup `confirm()` bawaan browser."

- "Bagaimana cara reuse style modal Project untuk Education tanpa membuat CSS baru yang terlalu banyak?"

- "Bantu saya membuat UI halaman Education agar konsisten dengan halaman Projects, termasuk tombol Add dan search bar."

- "Cek apakah penambahan search, feedback message, dan custom delete modal dapat dianggap sebagai peningkatan UI/UX di luar requirement minimum."

- "Cek `git status` dan bantu saya menentukan file mana yang sebaiknya dimasukkan ke commit agar satu commit hanya mewakili satu perubahan."

- "Apakah perubahan JSON data delivery dan perubahan wording UI sebaiknya berada pada commit yang sama atau dipisahkan?"

- "Bantu saya menggunakan conventional commit seperti `feat:`, `fix:`, `test:`, dan `docs:` agar Git history lebih terorganisir."

- "Audit implementasi Tugas 3 saya berdasarkan requirement resmi dan tunjukkan mana yang sudah selesai, mana yang masih wajib, dan mana yang merupakan fitur tambahan."

- "Bantu saya menulis refleksi Tugas 3 berdasarkan implementasi serta error yang benar-benar saya alami, bukan jawaban generik."

- "Bantu saya menjelaskan keterbatasan penggunaan AI selama debugging dan contoh bagian yang tetap harus saya koreksi serta verifikasi secara manual."

## Week 4 Documentation

Bagian ini mendokumentasikan implementasi Tutorial 4 dan Tugas 4 tanpa menggantikan dokumentasi dari minggu sebelumnya. Fokus pengembangan pada minggu ini adalah autentikasi, session, cookie, otorisasi berbasis peran, serta fitur Star pada data Education.

### Tutorial 4 - Implementasi Autentikasi, Session, dan Cookie

Pada Tutorial 4, saya mengimplementasikan autentikasi menggunakan sistem autentikasi bawaan Django. Model akun menggunakan `User` dari `django.contrib.auth`, sehingga saya tidak membuat model pengguna baru.

Fitur autentikasi yang diimplementasikan meliputi:

- Membuat halaman registrasi menggunakan `UserCreationForm`.
- Membuat halaman login menggunakan `AuthenticationForm`.
- Menggunakan fungsi `login()` untuk menyimpan status autentikasi pengguna pada session.
- Menggunakan fungsi `logout()` untuk menghapus session pengguna.
- Menambahkan URL `/register/`, `/login/`, dan `/logout/`.
- Menambahkan template `register.html` dan `login.html`.
- Menampilkan pesan kesalahan ketika data registrasi atau kredensial login tidak valid.
- Menampilkan pesan keberhasilan setelah akun berhasil dibuat.
- Menampilkan username pengguna yang sedang login pada navigation bar.
- Menampilkan tombol Login dan Register untuk pengunjung yang belum login.
- Menampilkan tombol Logout untuk pengguna yang sudah login.
- Mempertahankan halaman profil, Experience, Projects, dan Education agar tetap dapat dibaca tanpa login.

Django menyimpan identitas pengguna yang sudah login menggunakan session. Browser menyimpan session key melalui cookie `sessionid`, sedangkan data session sebenarnya disimpan dan dikelola oleh server. Pada setiap request berikutnya, Django menggunakan session tersebut untuk menentukan nilai `request.user`.

Saya juga menggunakan cookie `last_login` untuk menyimpan waktu login terakhir. Cookie tersebut dibuat menggunakan `response.set_cookie()` setelah proses login berhasil dan dihapus menggunakan `response.delete_cookie()` ketika pengguna melakukan logout.

Implementasi cookie tersebut memungkinkan halaman utama menampilkan informasi sesi login terakhir. Cookie `last_login` hanya digunakan untuk informasi tampilan dan bukan sebagai bukti autentikasi. Status autentikasi tetap ditentukan oleh sistem session Django.

Form yang mengubah data menggunakan metode POST dan menyertakan `{% csrf_token %}`. Token tersebut digunakan oleh Django untuk melindungi aplikasi dari Cross-Site Request Forgery. Request POST yang tidak membawa token CSRF yang valid akan ditolak sebelum mencapai logika perubahan data pada view.

Pada bagian otorisasi Tutorial 4, tindakan Create dan Delete Project dibatasi kepada pemilik portofolio atau superuser. Pembatasan tersebut tidak hanya dilakukan dengan menyembunyikan tombol pada template, tetapi juga diperiksa kembali pada sisi server menggunakan `request.user.is_superuser`.

Pengunjung tanpa login akan diarahkan menuju halaman login ketika mencoba mengakses tindakan yang memerlukan akun. Pengguna yang sudah login tetapi tidak memiliki hak akses akan menerima HTTP `403 Forbidden`.

Tutorial 4 juga menambahkan fitur Star pada Project menggunakan relasi `ManyToManyField` antara model `Project` dan model `User`. Relasi many-to-many digunakan karena satu Project dapat diberikan Star oleh banyak pengguna dan satu pengguna dapat memberikan Star pada banyak Project.

Fitur Star menggunakan form POST dengan CSRF token. Pengguna yang sudah memberikan Star dapat membatalkannya menggunakan tombol yang sama. Relasi many-to-many memastikan bahwa satu pengguna tidak menghasilkan Star ganda pada Project yang sama.

Endpoint JSON Project diperiksa kembali setelah penambahan relasi pengguna. Pemeriksaan tersebut diperlukan karena perubahan model dapat ikut mengubah data yang dipublikasikan oleh serializer. Informasi internal atau sensitif tidak boleh keluar melalui endpoint publik tanpa sengaja.

### Tugas 4 - Authentication, Session, and Cookies Implementation

Pada Tugas 4, pola autentikasi dan otorisasi dari Tutorial 4 diterapkan pada bagian Education yang dikembangkan pada Tugas 3.

Halaman daftar dan detail Education tetap dapat dibaca oleh semua pengunjung. Tindakan yang mengubah data dibatasi berdasarkan empat peran berikut:

| Peran | Membaca | Create | Update | Delete | Star/Unstar |
|---|---:|---:|---:|---:|---:|
| Pengunjung tanpa login | Ya | Harus login | Harus login | Harus login | Harus login |
| Pengguna biasa | Ya | Tidak | Tidak | Tidak | Ya |
| Editor | Ya | Tidak | Ya | Tidak | Ya |
| Pemilik portofolio atau superuser | Ya | Ya | Ya | Ya | Ya |

#### Peran Editor

Peran Editor dibuat menggunakan Django Group dengan nama `Editor`. Group tersebut dibuat melalui Django Admin, kemudian akun yang dipilih dimasukkan ke dalam Group tersebut.

Akun Editor tetap merupakan pengguna biasa dan tidak perlu memperoleh `Staff status` atau `Superuser status`. Keanggotaan Editor diperiksa menggunakan:

`request.user.groups.filter(name="Editor").exists()`

Saya membuat helper `can_edit_education()` untuk memisahkan pemeriksaan hak Update Education dari isi view. Helper tersebut mengembalikan nilai benar apabila pengguna merupakan superuser atau anggota Group Editor.

Pemisahan tersebut mengurangi pengulangan logika pemeriksaan role dan membuat maksud kode lebih mudah dibaca. Superuser dan Editor dapat menggunakan fungsi Update yang sama, sedangkan Create dan Delete tetap hanya dapat dilakukan oleh superuser.

#### Pembatasan Akses pada Sisi Server

Setiap view yang membutuhkan akun menggunakan `@login_required`. Dengan demikian, pengunjung tanpa login diarahkan ke halaman Login.

Setelah pengguna berhasil login, view kembali memeriksa role pengguna. Jika pengguna sudah login tetapi tidak mempunyai izin untuk tindakan tersebut, view menghasilkan `PermissionDenied` yang dikembalikan Django sebagai HTTP `403 Forbidden`.

Pembatasan akses pada sisi server penting karena menyembunyikan tombol pada template saja tidak cukup. Pengguna masih dapat mencoba membuka URL secara langsung atau mengirim request secara manual meskipun tombol tidak terlihat.

Aturan yang diterapkan adalah:

- `create_education` hanya dapat digunakan oleh superuser.
- `update_education` dapat digunakan oleh superuser dan anggota Group Editor.
- `delete_education` hanya dapat digunakan oleh superuser.
- `toggle_education_star` dapat digunakan oleh seluruh pengguna yang sudah login.
- Halaman daftar Education, detail Education, dan endpoint JSON tetap dapat dibaca tanpa login.

#### Pembatasan Kontrol pada Template

Selain pemeriksaan pada server, tombol pada template ditampilkan sesuai role pengguna.

- Tombol Add Education hanya ditampilkan kepada superuser.
- Tombol Edit Education ditampilkan kepada superuser dan Editor.
- Tombol Delete Education hanya ditampilkan kepada superuser.
- Tombol Star atau Unstar ditampilkan kepada pengguna yang sudah login.
- Pengunjung tanpa login melihat tautan menuju halaman Login untuk memberikan Star.

Pemeriksaan template bertujuan memberikan antarmuka yang sesuai dengan hak pengguna. Pemeriksaan ini meningkatkan pengalaman pengguna, tetapi tidak menggantikan pemeriksaan keamanan pada view.

#### Star dan Unstar Education

Model `Education` ditambahkan field berikut:

`starred_by = models.ManyToManyField(User, related_name="starred_educations", blank=True)`

Relasi tersebut menyimpan akun pengguna yang memberikan Star pada setiap Education. Setelah perubahan model, migration dibuat dan diterapkan ke database menggunakan:

```bash
python manage.py makemigrations main
python manage.py migrate
```

View `toggle_education_star` hanya menerima pengguna yang sudah login. Perubahan Star dilakukan menggunakan request POST dan dilindungi oleh CSRF token.

Apabila pengguna belum memberikan Star, akun tersebut ditambahkan ke `starred_by`. Apabila pengguna sudah memberikan Star, akun tersebut dihapus dari relasi.

`ManyToManyField` mencegah relasi pengguna dan Education yang sama tersimpan lebih dari satu kali. Dengan demikian, satu pengguna hanya dapat mempunyai maksimal satu Star pada setiap Education.

Halaman Education menampilkan:

- Jumlah total Star pada setiap Education.
- Status apakah pengguna yang sedang login sudah memberikan Star.
- Tombol Star jika pengguna belum memberikan Star.
- Tombol Unstar jika pengguna sudah memberikan Star.
- Tautan Login bagi pengunjung tanpa akun.

#### Sortir Berdasarkan Jumlah Star

Sebagai fitur tambahan yang relevan dengan Tugas 4, saya menambahkan pilihan pengurutan Education berdasarkan jumlah Star terbanyak.

Pengguna dapat memilih antara:

- Tahun terbaru.
- Star terbanyak.

Ketika parameter `sort=stars` diberikan, QuerySet Education menggunakan `Count("starred_by")` untuk menghitung jumlah Star dan mengurutkan data dari jumlah terbesar.

Fitur ini merupakan peningkatan interaktivitas dan UX karena data Star tidak hanya ditampilkan sebagai angka, tetapi juga dapat digunakan untuk mengatur urutan Education.

Jika dua Education mempunyai jumlah Star yang sama, pengurutan berikutnya menggunakan tahun mulai, nama institusi, dan UUID agar hasil pengurutan tetap konsisten.

#### Integritas Endpoint JSON

Endpoint `/api/education/` tetap digunakan untuk menyediakan data Education dalam format JSON.

Setelah field `starred_by` ditambahkan, serializer dibatasi menggunakan parameter `fields`. Field yang dipublikasikan hanya:

- `institution`
- `program`
- `start_year`
- `end_year`
- `website`
- `description`

Relasi `starred_by` tidak disertakan dalam endpoint JSON Education. Dengan demikian, identifier internal pengguna yang memberikan Star tidak terekspos melalui endpoint publik.

Endpoint JSON Project juga diperbaiki agar hanya mengirimkan field Project yang memang diperlukan. Perubahan tersebut sekaligus memperbaiki typo dan masalah indentasi pada variabel `projects_json`.

Saya sempat menempatkan pembuatan `projects_json` di dalam kondisi pencarian `if title_query`. Akibatnya, ketika endpoint dibuka tanpa query pencarian, variabel tersebut belum dibuat dan Django menghasilkan `UnboundLocalError`.

Masalah tersebut diperbaiki dengan meletakkan proses serialization setelah blok filtering. Dengan susunan tersebut, `projects_json` selalu dibuat baik ketika terdapat pencarian maupun ketika endpoint dibuka tanpa query.

#### Efisiensi Pengambilan Data Star

Halaman Education melakukan deserialisasi JSON sebelum data diberikan kepada template, mengikuti pola dari Tugas 3.

Untuk menghindari query terpisah pada setiap kartu Education, relasi `starred_by` dimuat menggunakan `prefetch_related_objects()`. Jumlah Star dan status pengguna kemudian dihitung dari data relasi yang sudah dimuat.

Pendekatan tersebut menghindari pola query berulang untuk setiap object Education dan membuat pemisahan antara pengambilan data, penghitungan Star, serta rendering template menjadi lebih jelas.

#### Pengujian

Saya menambahkan pengujian untuk memeriksa perilaku empat peran pengguna.

Skenario yang diuji meliputi:

- Halaman daftar Education dapat dibaca tanpa login.
- Halaman detail Education dapat dibaca tanpa login.
- Endpoint JSON Education dapat dibaca tanpa login.
- Pengunjung tanpa login diarahkan ke halaman Login ketika mencoba melakukan tindakan yang memerlukan akun.
- Pengguna biasa memperoleh HTTP 403 ketika mencoba Create, Update, atau Delete Education.
- Editor dapat melakukan Update Education.
- Editor memperoleh HTTP 403 ketika mencoba Create atau Delete Education.
- Superuser dapat melakukan Create, Update, dan Delete Education.
- Tombol Add, Edit, dan Delete hanya ditampilkan kepada role yang sesuai.
- Seluruh pengguna yang sudah login dapat memberikan dan membatalkan Star.
- Request GET tidak dapat digunakan untuk mengubah Star.
- Request Star tanpa CSRF token ditolak.
- Satu pengguna tidak dapat menghasilkan Star ganda.
- Request GET tidak dapat digunakan untuk menghapus Education.
- Endpoint JSON Education tidak mengekspos field `starred_by`.
- Endpoint JSON Project tetap dapat digunakan.
- Education dapat diurutkan berdasarkan jumlah Star.

Perintah pemeriksaan yang digunakan adalah:

```bash
python manage.py check
python manage.py test main
```

`python manage.py check` berhasil dijalankan tanpa menemukan issue.

Unit test menemukan dua masalah nyata pada implementasi awal:

1. View `update_education` belum memiliki `@login_required`. Akibatnya, pengunjung tanpa login menerima HTTP 403 dari pemeriksaan role, bukan redirect menuju Login.
2. Variabel `projects_json` hanya dibuat di dalam blok `if title_query`. Akibatnya, endpoint Project tanpa parameter pencarian menghasilkan `UnboundLocalError`.

Kedua masalah tersebut diperbaiki berdasarkan traceback dan hasil pengujian. Setelah memperbaiki source code, seluruh pengujian perlu dijalankan kembali sebelum commit akhir agar hasil aktual pada repository dapat diverifikasi.

#### Git dan Branching

Pengembangan Tugas 4 dilakukan menggunakan branch:

`feature/tugas-4-education`

Perubahan dipisahkan menggunakan conventional commit agar riwayat Git mencerminkan tujuan setiap perubahan. Contoh commit yang digunakan antara lain:

- `feat: add education star relationship`
- `feat: enforce education roles and add star sorting`
- `test: cover education roles stars and public JSON`
- `fix: correct project JSON and education authorization`
- `docs: document tutorial and assignment 4`

Sebelum dikumpulkan, commit akhir harus di-push ke GitHub. Tautan yang dikumpulkan melalui SCELE harus berupa tautan menuju commit, bukan hanya tautan repository.

Format tautan commit:

`https://github.com/naufalkhairiy/myportofolio/commit/<commit-hash>`

Repository harus dapat dibuka secara publik. Tautan commit dapat diperiksa melalui Incognito atau Private Browsing sebelum dikumpulkan.

### Setup Tambahan Tutorial 4 dan Tugas 4

Setelah mengikuti langkah setup umum pada bagian sebelumnya, jalankan migration:

```bash
python manage.py migrate
```

Jika belum mempunyai superuser lokal, buat menggunakan:

```bash
python manage.py createsuperuser
```

Jalankan server:

```bash
python manage.py runserver
```

Buka Django Admin melalui:

```text
http://127.0.0.1:8000/admin/
```

Login menggunakan akun superuser, kemudian lakukan langkah berikut:

1. Buka bagian `Groups`.
2. Klik `Add`.
3. Isi Name dengan `Editor`.
4. Permissions dapat dibiarkan kosong karena implementasi memeriksa keanggotaan Group.
5. Simpan Group.
6. Buka bagian `Users`.
7. Pilih akun biasa yang akan dijadikan Editor.
8. Masukkan akun tersebut ke Group `Editor`.
9. Jangan memberikan `Staff status` atau `Superuser status` kepada akun Editor.
10. Simpan perubahan pengguna.

Untuk melakukan pengujian manual, siapkan:

- Satu akun pengguna biasa.
- Satu akun pengguna biasa yang dimasukkan ke Group Editor.
- Satu akun superuser sebagai pemilik portofolio.
- Satu sesi browser tanpa login.

Lakukan pemeriksaan berikut:

| Kondisi | Hasil yang diharapkan |
|---|---|
| Pengunjung membuka daftar dan detail Education | Halaman dapat dibaca |
| Pengunjung menekan tindakan yang memerlukan akun | Diarahkan ke Login |
| Pengguna biasa memberi Star | Star berhasil ditambahkan |
| Pengguna biasa membatalkan Star | Star berhasil dihapus |
| Pengguna biasa membuka Create, Update, atau Delete | HTTP 403 |
| Editor membuka Update Education | Form dapat dibuka dan disimpan |
| Editor membuka Create atau Delete Education | HTTP 403 |
| Superuser membuka Create, Update, dan Delete | Semua tindakan tersedia |
| Pengguna memilih Star terbanyak | Education diurutkan berdasarkan jumlah Star |
| Pengguna membuka `/api/education/` | JSON tampil tanpa `starred_by` |
| Pengguna membuka `/api/projects/` | JSON Project tampil tanpa error |
| Pengguna logout | Session berakhir dan cookie `last_login` dihapus |

### Refleksi Tugas 4

Halaman resmi Individual Assignment 4 menyatakan bahwa pertanyaan reflektif untuk pekan ini dihilangkan. Karena itu, tidak ada pertanyaan reflektif Tugas 4 yang harus dijawab.

Sebagai catatan pembelajaran, implementasi minggu ini membantu saya memahami perbedaan autentikasi dan otorisasi.

Autentikasi menentukan siapa pengguna yang sedang mengakses aplikasi. Proses ini dilakukan melalui registrasi, login, logout, session, dan `request.user`.

Otorisasi menentukan tindakan apa yang boleh dilakukan oleh pengguna yang sudah dikenali. Pada implementasi Education, pengguna biasa, Editor, dan superuser merupakan akun yang sama-sama dapat terautentikasi, tetapi mempunyai hak Create, Update, dan Delete yang berbeda.

Saya juga memahami bahwa menyembunyikan tombol pada template bukan merupakan perlindungan keamanan yang cukup. Pemeriksaan hak akses harus tetap diterapkan pada view karena URL dapat dibuka secara langsung atau dipanggil melalui request manual.

Penggunaan test membantu menemukan perbedaan perilaku yang sulit terlihat melalui browser. Salah satu contohnya adalah perbedaan antara redirect HTTP 302 untuk pengunjung tanpa login dan HTTP 403 untuk pengguna yang sudah login tetapi tidak mempunyai izin.

## AI Usage Disclosure - Week 4

Pada Tutorial 4 dan Tugas 4, saya menggunakan ChatGPT dan Codex untuk membantu membaca requirement resmi, meninjau source code project, merencanakan perubahan minimum, memahami autentikasi serta otorisasi Django, menyusun unit test, membaca traceback, dan memperbarui dokumentasi.

Saya memberikan source code project dalam bentuk ZIP agar saran dapat disesuaikan dengan nama model, fungsi view, template, dan URL yang benar-benar digunakan oleh project. Hal ini dilakukan untuk mengurangi kemungkinan solusi generik yang tidak sesuai dengan struktur aplikasi.

Saya meminta AI memprioritaskan requirement utama berikut:

- Registrasi, login, dan logout.
- Session dan cookie `last_login`.
- Pembatasan Create, Update, dan Delete berdasarkan role.
- Peran Editor menggunakan Django Group.
- Fitur Star dan Unstar pada Education.
- Perlindungan POST menggunakan CSRF token.
- Integritas endpoint JSON.
- Unit test untuk empat role pengguna.
- README dan AI disclosure.
- Pengumpulan menggunakan tautan commit GitHub.

AI juga digunakan untuk membandingkan implementasi dengan halaman resmi Tutorial 4 dan Tugas 4. Dari pemeriksaan tersebut diketahui bahwa Tugas 4 tidak mempunyai pertanyaan reflektif karena pertanyaan reflektif untuk pekan ini secara eksplisit dihilangkan.

### Strategi Penggunaan AI

Saya menggunakan strategi prompting berbasis konteks. Daripada hanya meminta “buatkan Tugas 4”, saya memberikan requirement resmi, source code yang sudah ada, traceback, serta batasan bahwa perubahan harus sesederhana mungkin dan tidak menambahkan fitur yang tidak diperlukan.

Saya juga meminta perubahan dijelaskan berdasarkan lokasi file agar dapat diterapkan secara bertahap. Ketika instruksi penempatan kode masih terlalu umum dan membingungkan, saya meminta ulang dalam bentuk blok lengkap yang dapat menggantikan satu fungsi atau satu file.

Setelah menerima saran, saya tetap menjalankan:

```bash
python manage.py check
python manage.py test main
```

Saya menggunakan traceback sebagai sumber bukti untuk menentukan akar masalah. Saya tidak menganggap kode benar hanya karena dapat disalin atau karena tidak menghasilkan syntax error.

### Bagian yang Dibantu AI

AI membantu pada bagian berikut:

- Membaca requirement resmi Tutorial 4 dan Tugas 4.
- Membandingkan requirement dengan isi project.
- Menentukan penggunaan Django Group untuk role Editor.
- Menyusun helper `can_edit_education()`.
- Menentukan penggunaan `@login_required` dan `PermissionDenied`.
- Membatasi tombol berdasarkan role pada template.
- Menambahkan `ManyToManyField` untuk Star Education.
- Membuat view Star dan Unstar berbasis POST.
- Menampilkan jumlah Star dan status pengguna.
- Menambahkan pengurutan berdasarkan jumlah Star.
- Membatasi field yang keluar melalui serializer JSON.
- Menyusun unit test authorization, Star, CSRF, API, dan template.
- Membaca hasil test dan traceback.
- Menentukan perbaikan terhadap decorator yang hilang.
- Menentukan perbaikan terhadap indentasi `projects_json`.
- Menyusun dokumentasi Week 4.

### Keterbatasan dan Koreksi terhadap AI

Penggunaan AI pada Week 4 menunjukkan bahwa jawaban yang terlihat lengkap belum tentu langsung dapat diterapkan tanpa pemeriksaan.

Pada instruksi awal, lokasi penempatan beberapa potongan kode masih terlalu umum. Contohnya, instruksi “tambahkan di dalam form pencarian sebelum tombol Cari” dapat membingungkan ketika pengguna harus menentukan batas awal dan akhir form. Instruksi kemudian diperbaiki dengan memberikan satu blok form lengkap untuk menggantikan blok lama.

Masalah lain terjadi pada fungsi `get_projects_json`. Potongan kode serialization sempat ditempatkan dengan indentasi yang salah sehingga hanya berjalan ketika `title_query` tersedia. Unit test kemudian menemukan `UnboundLocalError` ketika endpoint dibuka tanpa pencarian.

Decorator `@login_required` juga sempat belum terpasang pada `update_education`. Akibatnya, pengunjung tanpa login menerima HTTP 403 dari helper role, sedangkan requirement mengharuskan pengunjung diarahkan ke halaman Login. Kesalahan tersebut ditemukan melalui perbandingan response 403 dan response 302 pada unit test.

Instruksi pembuatan Editor juga sempat menimbulkan kebingungan karena halaman Django Admin menampilkan daftar Permissions. Setelah diperiksa kembali, Editor bukan permission bawaan yang akan muncul pada daftar tersebut. Editor merupakan nama Group baru yang harus dibuat melalui menu Groups, sedangkan daftar Permissions dapat dibiarkan kosong karena source code memeriksa nama Group secara langsung.

Contoh-contoh tersebut menunjukkan bahwa AI dapat membantu mempercepat penelusuran masalah, tetapi AI masih dapat menghasilkan instruksi yang kurang jelas, salah indentasi, atau tidak sepenuhnya sesuai dengan state source code terbaru.

Karena itu, saya melakukan perbaikan manual dengan:

- Membandingkan saran dengan source code project.
- Memeriksa posisi decorator dan indentasi.
- Menjalankan Django system check.
- Menjalankan unit test.
- Membaca traceback sampai ke nama fungsi dan nomor baris.
- Menguji role melalui akun berbeda.
- Memeriksa endpoint JSON melalui browser.
- Memeriksa `git diff` sebelum commit.
- Tidak memasukkan password, cookie, atau credential ke repository.

### AI Prompting Log - Week 4

Berikut beberapa contoh prompt dan permintaan yang digunakan selama Tutorial 4 dan Tugas 4:

- "Baca requirement resmi Tugas 4 dan audit ZIP project saya berdasarkan source code yang benar-benar ada."

- "Targetkan indikator nilai 4, tetapi gunakan implementasi minimum dan jangan menambahkan fitur yang tidak diperlukan."

- "Prioritaskan role Editor, authorization Education, Star Education, unit test, README, dan pengumpulan."

- "Pertahankan alur serialization dan deserialization JSON dari Tugas 3."

- "Pastikan endpoint JSON tetap berfungsi dan tidak membocorkan informasi sensitif."

- "Jelaskan file mana yang harus dibuka dan lokasi pasti untuk menempatkan kode."

- "Berikan satu blok form lengkap untuk menggantikan form lama agar saya tidak salah menempatkan pilihan sortir."

- "Kenapa Editor tidak muncul pada daftar Permissions di Django Admin?"

- "Jelaskan langkah membuat Group Editor dan memasukkan akun ke Group tersebut."

- "Baca traceback `UnboundLocalError: cannot access local variable 'projects_json'` dan tunjukkan akar masalahnya."

- "Kenapa test mengharapkan redirect 302 tetapi view menghasilkan HTTP 403?"

- "Buatkan isi `main/views.py` lengkap agar seluruh fungsi dapat disalin tanpa salah indentasi."

- "Tambahkan test untuk pengunjung, pengguna biasa, Editor, dan superuser."

- "Tambahkan test bahwa satu pengguna tidak menghasilkan Star ganda."

- "Tambahkan test bahwa request GET tidak dapat menghapus Education atau mengubah Star."

- "Tambahkan test CSRF untuk endpoint Star."

- "Tambahkan test agar endpoint JSON Education tidak mengeluarkan `starred_by`."

- "Tambahkan fitur ekstra yang sederhana dan relevan untuk indikator nilai 4."

- "Gunakan sortir berdasarkan jumlah Star sebagai peningkatan UX tanpa membuat fitur yang terlalu kompleks."

- "Perbarui README tanpa menghapus atau meringkas dokumentasi Week 1 sampai Week 3."

- "Cari halaman resmi PBP terlebih dahulu dan jangan mengarang pertanyaan reflektif yang tidak tersedia."


## Week 5 Documentation

Pada Tutorial 5 dan Tugas 5, fokus pengembangan beralih dari halaman yang sebagian besar dirender langsung oleh Django menjadi antarmuka yang lebih interaktif menggunakan JavaScript dan AJAX.

Bagian yang diterapkan pada Tugas 5 adalah Education, yaitu bagian portofolio yang sebelumnya dikembangkan pada Tugas 2 sampai Tugas 4.

### Tutorial 5 - Web Interactivity with JavaScript and AJAX

Pada Tutorial 5, saya mempelajari pola pengambilan dan pengiriman data tanpa melakukan full page reload menggunakan Fetch API.

Konsep utama yang dipelajari meliputi:

- Mengambil data JSON menggunakan `fetch()`.
- Menggunakan `async` dan `await` untuk menangani operasi asynchronous.
- Menampilkan loading state, error state, empty state, dan data state.
- Menggunakan `AbortController` untuk membatalkan request lama yang sudah tidak relevan.
- Mengimplementasikan search debouncing menggunakan `setTimeout()` dan `clearTimeout()`.
- Menggunakan Popover API untuk menampilkan form melalui modal.
- Mengirim `ModelForm` menggunakan `FormData`.
- Mengirim CSRF token melalui header `X-CSRFToken`.
- Menampilkan feedback menggunakan reusable toast.
- Melakukan escaping terhadap data yang dirender melalui JavaScript.
- Membersihkan input kembali pada server sebagai lapisan perlindungan tambahan terhadap XSS.

### Tugas 5 - AJAX pada Education

Pada Tugas 5, pola AJAX dari Tutorial 5 diterapkan pada bagian Education.

Sebelumnya, halaman Education mendapatkan data melalui proses serialization dan deserialization sebelum object diberikan kembali kepada Django template. Pada implementasi Tugas 5, halaman `/education/` hanya merender struktur dasar halaman, sedangkan daftar Education diambil langsung oleh JavaScript melalui endpoint:

`/api/education/`

Endpoint tersebut mengembalikan data dalam bentuk JSON menggunakan `JsonResponse`.

Setiap object Education yang dikirim memiliki identifier `pk` dan field yang diperlukan oleh frontend, termasuk:

- `institution`
- `program`
- `start_year`
- `end_year`
- `website`
- `description`
- `star_count`
- `is_starred`

Relasi lengkap `starred_by` tidak dikirim kepada browser.

### AJAX Loading dan Rendering

Template Education menyediakan empat state utama:

- Loading state ketika data sedang diminta.
- Error state apabila request gagal.
- Empty state apabila tidak ada data yang ditemukan.
- Education list apabila request berhasil dan mempunyai data.

JavaScript menjalankan `fetchEducations()` ketika halaman pertama kali dibuka. Function tersebut membuat request menuju endpoint JSON, membaca response menggunakan `response.json()`, kemudian membuat setiap Education menggunakan `buildEducationElement()`.

Dengan pendekatan ini, Django tidak lagi melakukan perulangan terhadap seluruh Education pada template. Data dikirim sebagai JSON dan komponen halaman dibangun oleh JavaScript.

### AJAX Search dan Debouncing

Pencarian Education menggunakan input institusi yang sama seperti implementasi sebelumnya, tetapi request sekarang dilakukan menggunakan AJAX.

Debouncing diterapkan dengan delay 300 milidetik. Setiap kali pengguna mengetik, timer sebelumnya dibatalkan menggunakan `clearTimeout()`. Timer baru kemudian dibuat menggunakan `setTimeout()`.

Request pencarian baru hanya dilakukan ketika pengguna berhenti mengetik selama sekitar 300 milidetik. Pendekatan ini mencegah browser mengirim request untuk setiap karakter yang diketik.

`AbortController` juga digunakan untuk membatalkan request sebelumnya apabila request baru sudah dimulai. Hal tersebut mencegah response lama yang datang terlambat menggantikan hasil pencarian terbaru.

### Modal Add Education dan AJAX POST

Tombol Add Education untuk superuser tidak lagi membuka halaman form terpisah. Tombol tersebut membuka modal menggunakan Popover API.

Form dalam modal tetap menggunakan `EducationForm`, tetapi proses submit dicegat menggunakan `event.preventDefault()` dan dikirim melalui Fetch API ke endpoint AJAX.

Data form dikirim menggunakan:

`new FormData(educationForm)`

Karena request tersebut menggunakan metode POST, CSRF token dibaca dari cookie `csrftoken` dan dikirim melalui header:

`X-CSRFToken`

Apabila form valid, endpoint mengembalikan HTTP 201 dan JSON yang berisi pesan keberhasilan. Modal kemudian ditutup, form di-reset, toast keberhasilan ditampilkan, dan daftar Education dimuat kembali tanpa reload halaman.

Apabila validation gagal, endpoint mengembalikan HTTP 400 dan error dari `EducationForm`. Pengguna kemudian melihat pesan tersebut melalui toast.

Pengguna yang bukan superuser menerima HTTP 403 apabila mencoba memanggil endpoint Add Education secara langsung.

### Perlindungan XSS

Data Education sekarang dirender melalui JavaScript menggunakan `innerHTML`. Karena data JSON tidak secara otomatis memperoleh auto-escaping seperti variable yang dirender langsung oleh Django template, setiap nilai dinamis yang dimasukkan ke HTML terlebih dahulu diproses melalui function `escapeHtml()`.

Function tersebut mengubah karakter khusus HTML seperti `&`, `<`, `>`, `"`, dan `'` menjadi HTML entity sehingga browser menampilkannya sebagai teks dan tidak menafsirkannya sebagai elemen HTML.

Sebagai lapisan perlindungan tambahan pada server, `EducationForm` menggunakan method:

- `clean_institution()`
- `clean_program()`
- `clean_description()`

Method tersebut menggunakan `strip_tags()` sebelum data disimpan.

Pada `institution`, input yang hanya berisi tag HTML akan menjadi string kosong setelah proses pembersihan dan menghasilkan `ValidationError`.

Server-side cleaning tidak digunakan sebagai pengganti escaping pada frontend. Keduanya digunakan sebagai lapisan perlindungan pada tahap yang berbeda.

### AJAX Star dan Unstar sebagai Fitur Tambahan

Sebagai fitur tambahan untuk meningkatkan interaktivitas, fitur Star dan Unstar Education yang sebelumnya menggunakan POST biasa diubah agar dapat bekerja melalui AJAX.

Ketika pengguna menekan Star atau Unstar, JavaScript mencegah submit form normal menggunakan `event.preventDefault()` dan mengirim POST menggunakan `fetch()`.

Request AJAX mengirim header:

`Accept: application/json`

View `toggle_education_star` menggunakan header tersebut untuk menentukan apakah response harus berupa JSON atau redirect biasa.

Dengan pendekatan tersebut, endpoint lama tetap memiliki fallback untuk form POST biasa, sedangkan request AJAX mendapatkan `JsonResponse`.

Setelah Star berhasil berubah, daftar Education dimuat ulang melalui `fetchEducations()` sehingga jumlah Star, status Star, dan urutan berdasarkan jumlah Star dapat diperbarui tanpa melakukan full page reload.

### Automated Testing dan Verification

Saya membuat file test aktif:

`main/test_tugas5.py`

Test tersebut menggunakan Django `TestCase` untuk pengujian backend dan `StaticLiveServerTestCase` bersama Selenium WebDriver untuk pengujian browser secara headless.

Skenario yang diuji meliputi:

- Endpoint JSON Education mengembalikan `pk`, `star_count`, dan `is_starred`.
- Guest dan pengguna biasa tidak dapat menggunakan endpoint Add Education.
- Superuser dapat menambahkan Education melalui endpoint AJAX.
- Payload XSS yang hanya berisi tag HTML ditolak oleh server.
- AJAX Star dan Unstar menghasilkan response JSON dan mengubah relasi `starred_by`.
- Guest dapat melihat data Education melalui AJAX.
- Guest tidak melihat tombol Add Education.
- Guest melihat tautan Login untuk memberikan Star.
- Search menggunakan debounce.
- Sorting dilakukan tanpa navigasi halaman.
- Superuser dapat membuka modal dan menambahkan data tanpa reload.
- Toast keberhasilan ditampilkan setelah Add Education.
- Payload XSS tidak menghasilkan JavaScript alert pada browser.

Test lama dari Tugas 4 tetap dipertahankan sebagai dokumentasi history dengan nama:

`main/tugas4_tests.py`

Nama tersebut sengaja tidak diawali dengan `test` sehingga tidak ikut test discovery untuk test aktif Tugas 5.

Sebelum commit akhir, pemeriksaan dilakukan menggunakan:

```bash
python manage.py check
python manage.py test main.test_tugas5 -v 2
python manage.py makemigrations --check --dry-run
git diff --check
```

Seluruh 7 automated test Tugas 5 berhasil dijalankan. Django system check juga tidak menemukan issue dan tidak terdapat perubahan model yang membutuhkan migration baru.

### Git dan Branching

Pengembangan Tugas 5 dilakukan menggunakan branch:

`feature/tugas-5-education`

Perubahan dibuat secara bertahap menggunakan conventional commit agar setiap commit mempunyai tujuan yang jelas.

Beberapa commit yang digunakan antara lain:

- `feat: sanitize education text fields`
- `feat: add AJAX backend for education`
- `feat: add AJAX education interface`
- `test: add automated tests for education AJAX`
- `feat: add AJAX education star toggle`
- `chore: archive Tugas 4 test suite`
- `fix: preserve education star fallback`

Pemisahan commit tersebut membantu membedakan perubahan pada validasi server, backend AJAX, frontend AJAX, automated testing, fitur tambahan, dan maintenance.

## Refleksi Tugas 5

### 1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai tidak ada event baru selama jangka waktu tertentu.

Pada pencarian Education, saya menggunakan debounce selama 300 milidetik. Ketika pengguna mengetik pada search input, timer sebelumnya dibatalkan menggunakan `clearTimeout()`, kemudian timer baru dibuat menggunakan `setTimeout()`.

Sebagai contoh, ketika pengguna mengetik kata `Universitas`, aplikasi tidak langsung mengirim request setiap kali huruf baru dimasukkan. Request baru dilakukan setelah pengguna berhenti mengetik selama kurang lebih 300 milidetik.

Teknik ini penting pada pencarian AJAX karena tanpa debounce setiap perubahan input dapat menghasilkan request HTTP baru. Hal tersebut membuat browser dan server melakukan pekerjaan yang sebenarnya belum diperlukan, terutama ketika pengguna mengetik dengan cepat.

Selain debouncing, implementasi saya juga menggunakan `AbortController`. Apabila request sebelumnya masih berjalan ketika pencarian baru dimulai, request lama dibatalkan. Hal ini membantu mencegah response lama yang datang terlambat menggantikan hasil pencarian terbaru.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`fetch()` merupakan operasi asynchronous dan mengembalikan sebuah `Promise`, bukan langsung sebuah object `Response`.

Pada implementasi saya terdapat kode:

```javascript
const response = await fetch(url);
```

`await` membuat function asynchronous menunggu sampai Promise dari `fetch()` selesai dan menghasilkan object `Response`. Setelah itu saya dapat memeriksa nilai seperti `response.ok`.

Body response JSON juga dibaca menggunakan:

```javascript
const data = await response.json();
```

`response.json()` juga menghasilkan Promise, sehingga `await` digunakan kembali agar proses parsing JSON selesai sebelum data digunakan.

Jika `await` pada `fetch()` dihapus tetapi kode berikutnya tetap sama, variabel `response` masih berisi Promise dan bukan object `Response`. Karena itu kode yang mengharapkan property seperti `response.ok` atau method seperti `response.json()` tidak dapat digunakan dengan cara yang sama.

`await` bukan satu-satunya cara menangani Promise karena JavaScript juga menyediakan `.then()`. Namun, saya menggunakan `async` dan `await` karena alur request, pemeriksaan response, parsing JSON, rendering data, dan error handling menjadi lebih mudah dibaca secara berurutan.

### 3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

Cross-Site Scripting atau XSS adalah serangan ketika data yang seharusnya hanya ditampilkan sebagai teks berhasil ditafsirkan dan dijalankan oleh browser sebagai HTML atau JavaScript.

Contoh payload yang digunakan dalam pengujian adalah:

```html
<img src="x" onerror="alert('XSS!')">
```

Ketika data ditampilkan menggunakan Django Template Language, Django secara default melakukan auto-escaping terhadap variable template. Karakter HTML khusus akan diubah sehingga browser tidak langsung menafsirkannya sebagai tag HTML.

Pada implementasi AJAX, data Education diterima sebagai JSON kemudian digunakan JavaScript untuk membangun HTML secara dinamis. Saya menggunakan `innerHTML` untuk memasukkan hasil tersebut ke halaman.

JSON sendiri tidak memberikan HTML escaping untuk konteks `innerHTML`. Jika data pengguna dimasukkan langsung ke template string tanpa perlindungan, karakter seperti `<` dan `>` dapat dibaca browser sebagai elemen HTML.

Karena itu, pada frontend saya menggunakan function `escapeHtml()` sebelum nilai dinamis dimasukkan ke `innerHTML`. Function tersebut mengubah karakter khusus HTML menjadi HTML entity sehingga browser menampilkannya sebagai teks.

Saya juga menambahkan perlindungan pada server melalui `clean_institution()`, `clean_program()`, dan `clean_description()` pada `EducationForm` menggunakan `strip_tags()`.

Pada field `institution`, input yang setelah proses pembersihan hanya menghasilkan string kosong akan ditolak menggunakan `ValidationError`.

Server-side cleaning bukan pengganti escaping pada frontend. Keduanya digunakan sebagai dua lapisan perlindungan pada tahap yang berbeda.

## AI Usage Disclosure - Week 5

Pada Tutorial 5 dan Tugas 5, saya menggunakan ChatGPT sebagai alat bantu belajar, membaca requirement, melakukan source code review, debugging, merencanakan implementasi, membuat automated test, mengatur Git workflow, dan menyusun dokumentasi.

Saya meminta AI menggunakan Tutorial 5 dan Tugas 5 sebagai sumber utama sebelum menentukan implementasi. Untuk konsep Django, saya menggunakan dokumentasi resmi Django sebagai referensi tambahan. Untuk konsep dasar JavaScript dan browser API, saya juga menggunakan W3Schools sebagai referensi.

### Strategi Penggunaan AI

Pada Week 5 saya menggunakan pendekatan source-first. Saya tidak langsung meminta AI membuat seluruh Tugas 5, tetapi terlebih dahulu meminta AI membaca requirement resmi dan membandingkannya dengan source code yang sudah tersedia.

Implementasi kemudian dibagi menjadi beberapa tahap:

1. Menambahkan server-side cleaning untuk input Education.
2. Mengubah backend Education agar menyediakan data yang diperlukan AJAX.
3. Mengubah halaman Education menjadi frontend AJAX.
4. Menambahkan Star dan Unstar melalui AJAX sebagai fitur interaktivitas tambahan.
5. Melakukan automated testing dan final verification.
6. Memperbarui dokumentasi dan AI disclosure.

Saya juga meminta agar implementasi tetap minimal dan tidak menambahkan fitur besar yang tidak diperlukan hanya untuk mengejar indikator nilai.

### Bagian yang Dibantu AI

AI membantu saya pada beberapa bagian berikut:

- Membandingkan Tutorial 5 dan requirement Tugas 5 dengan source code project.
- Menjelaskan pola `fetch()`, `async`, dan `await`.
- Menjelaskan dan mengimplementasikan debouncing.
- Menjelaskan fungsi `AbortController`.
- Menyusun loading, error, empty, dan data state.
- Mengubah endpoint Education menjadi `JsonResponse` manual.
- Membawa `star_count` dan `is_starred` melalui endpoint JSON.
- Menggunakan modal Add Education dengan Popover API.
- Mengirim `EducationForm` melalui `FormData`.
- Mengirim CSRF token melalui header `X-CSRFToken`.
- Menampilkan feedback melalui reusable toast.
- Menjelaskan risiko XSS ketika menggunakan `innerHTML`.
- Menggunakan `escapeHtml()` pada data dari JSON.
- Menggunakan `strip_tags()` dan method `clean_<field>()` pada server.
- Mengubah Star dan Unstar menjadi AJAX tanpa membuat endpoint baru.
- Membuat Django backend test dan Selenium headless browser test.
- Membaca traceback dan melakukan audit source code.
- Membantu memisahkan perubahan menjadi conventional commits.
- Membantu menyusun dokumentasi dan refleksi Tugas 5.

### Keterbatasan AI dan Perbaikan Manual

Penggunaan AI pada Tugas 5 menunjukkan bahwa saran AI tetap perlu dibandingkan dengan source code aktual dan diuji sebelum digunakan.

Pada salah satu tahap, AI sempat mengasumsikan bahwa import `serializers` sudah tidak digunakan dan menyarankan untuk menghapusnya. Setelah source code diperiksa kembali, `show_education()` lama ternyata masih menggunakan proses deserialization. Saya kemudian meminta AI melakukan audit terhadap file aktual sebelum melanjutkan perubahan.

Pada endpoint JSON Education, `return JsonResponse()` juga sempat berada di dalam perulangan. Jika dibiarkan, function akan berhenti setelah Education pertama sehingga object berikutnya tidak akan masuk ke response. Posisi `return` kemudian diperbaiki setelah source code diperiksa kembali.

Terdapat pula typo pada key response AJAX:

`messsage`

yang seharusnya:

`message`

Kesalahan tersebut dapat menyebabkan frontend gagal mengambil pesan melalui `result.message`.

Saat menambahkan test untuk AJAX Star, method test sempat ditempatkan pada class `Tugas5BrowserTests`, padahal method tersebut menggunakan `self.member` dan `self.star_url` yang dibuat pada `Tugas5BackendTests`.

Test kemudian menghasilkan:

```text
AttributeError: 'Tugas5BrowserTests' object has no attribute 'member'
```

Saya memindahkan method tersebut ke class backend test yang mempunyai setup sesuai.

Audit berikutnya juga menemukan typo:

`messages.succes`

yang seharusnya:

`messages.success`

Jalur AJAX tetap dapat lolos automated test karena response JSON dikembalikan sebelum kode fallback tersebut dijalankan. Hal ini menunjukkan bahwa keberhasilan satu jalur test belum tentu membuktikan seluruh jalur alternatif bebas dari kesalahan.

Saya juga menggunakan `git diff --check` dan menemukan trailing whitespace pada file test. Walaupun tidak memengaruhi fungsi program, whitespace tersebut tetap dibersihkan sebelum commit.

Karena itu, saya tidak menggunakan output AI sebagai bukti bahwa implementasi sudah benar. Verifikasi akhir tetap dilakukan menggunakan:

```bash
python manage.py check
python manage.py test main.test_tugas5 -v 2
python manage.py makemigrations --check --dry-run
git diff --check
git status
```

Pada verifikasi akhir, seluruh 7 automated test Tugas 5 berhasil dijalankan.

### AI Prompting Log - Week 5

Beberapa contoh prompt dan permintaan yang saya gunakan selama pengerjaan adalah:

- "Baca Tutorial 5 dan Tugas 5 terlebih dahulu sebelum menentukan implementasi."
- "Gunakan Tutorial 5 sebagai sumber utama, Django documentation untuk Django, dan W3Schools untuk JavaScript."
- "Targetkan indikator nilai 4 dengan perubahan seminimal mungkin."
- "Jangan menambahkan fitur besar yang tidak diperlukan."
- "Jelaskan setiap bagian kode agar saya memahami alurnya."
- "Audit source code saya sebelum menyarankan penghapusan import."
- "Kenapa `show_education()` tidak perlu melakukan deserialization lagi setelah menggunakan AJAX?"
- "Jelaskan debouncing menggunakan `setTimeout()` dan `clearTimeout()`."
- "Kenapa AJAX POST masih membutuhkan CSRF token?"
- "Kenapa data yang dimasukkan melalui `innerHTML` harus di-escape?"
- "Jelaskan kenapa `strip_tags()` bukan pengganti escaping pada JavaScript."
- "Tambahkan satu fitur interaktif yang sederhana dan relevan untuk indikator nilai 4."
- "Ubah Star dan Unstar menjadi AJAX tanpa membuat endpoint baru jika tidak diperlukan."
- "Buat automated test agar pengujian manual dapat diminimalkan."
- "Gunakan Selenium headless untuk menguji perilaku JavaScript pada browser."
- "Audit error berdasarkan traceback sebelum mengubah source code."
- "Cek `git diff --check` sebelum commit."
- "Pertahankan test Tugas 4 sebagai history tetapi jangan biarkan test lama mengganggu test discovery Tugas 5."
- "Audit README saya berdasarkan requirement resmi Tugas 5 dan rubrik nilai 4. Jangan tulis ulang seluruh README; beri instruksi patch-style seperti bagian mana yang harus diganti, bagian mana yang harus ditambahkan, dan bagian mana yang sudah benar agar dokumentasi minggu sebelumnya tetap terjaga."