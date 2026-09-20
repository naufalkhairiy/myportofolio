# My Portfolio

Situs web portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia.

## Author

- Name: Naufal Khairiy Zulkarnain Sormin
- NPM: 2506621850
- Class: PBP D

## Project Description

Project ini merupakan website portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia. Website ini dibangun menggunakan Django, HTML, dan CSS serta dikembangkan secara bertahap mengikuti materi tutorial dan tugas mingguan.

Pada tahap awal, website berisi halaman profil statis dengan informasi pribadi, social links, dan riwayat pendidikan. Pada pengembangan berikutnya, website mulai menerapkan arsitektur Model-View-Template (MVT) Django untuk mengelola data secara dinamis melalui database.

Saat ini, data Experience dan Education dikelola menggunakan Django Model dan ditampilkan melalui View serta Django Template Language. Education memiliki halaman daftar tersendiri dan halaman detail untuk setiap riwayat pendidikan. Website juga dilengkapi responsive design, navigation bar, hover effect, transition, serta external link menuju institusi terkait.

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
- Data Project tersedia melalui endpoint JSON dan ditampilkan setelah deserialisasi.
- Education dapat dibuat, diperbarui, dan dihapus melalui antarmuka web.
- `EducationForm` menggunakan Django `ModelForm`.
- Data Education tersedia melalui endpoint JSON.
- Halaman Education menampilkan data setelah proses deserialisasi JSON.
- Pencarian Education berdasarkan nama institusi.
- Reusable form template untuk Create dan Update Education.
- Confirmation modal sebelum menghapus Education.
- Success feedback menggunakan Django Messages.
- Unit test untuk CRUD, JSON data delivery, filtering, dan search Education.

## Technologies Used

- Python
- Django
- Django Template Language (DTL)
- HTML5
- CSS3
- CSS Grid
- Flexbox
- SQLite untuk development lokal
- PostgreSQL pada deployment PWS
- Git dan GitHub

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

7. Jalankan unit test untuk memastikan project berjalan dengan benar.

```bash
python manage.py test main
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