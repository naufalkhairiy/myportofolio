# My Portfolio

Situs web portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia.

## Author

- Name: Naufal Khairiy Zulkarnain Sormin
- NPM: 2506621850
- Class: PBP D

## Project Description

Project ini merupakan website portofolio pribadi yang dibuat untuk mata kuliah Pemrograman Berbasis Platform di Universitas Indonesia. Website ini dibangun menggunakan Django, HTML, dan CSS serta berisi informasi profil, social links, dan riwayat pendidikan saya.

Tampilan website dibuat responsif agar tetap nyaman digunakan pada desktop maupun perangkat mobile. Selain menampilkan informasi dasar, website ini juga memiliki beberapa interaksi sederhana seperti hover effect, transition, smooth scrolling, serta external link pada riwayat pendidikan.

## Main Features

- Informasi profil pribadi dan foto.
- Informasi NPM dan program studi.
- Social links menuju GitHub, LinkedIn, dan email.
- Section Education yang menampilkan riwayat pendidikan.
- External link pada institusi pendidikan.
- Hover effect dan transition pada beberapa elemen.
- Smooth scrolling melalui navigation bar.
- Responsive layout untuk desktop dan perangkat mobile.

## Technologies Used

- Django
- HTML5
- CSS3
- CSS Grid
- Flexbox
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

6. Jalankan Django development server.

```bash
python manage.py runserver
```

7. Buka alamat berikut melalui browser:

```text
http://localhost:8000/
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

## AI Usage Disclosure

Saya menggunakan ChatGPT sebagai alat bantu selama pengerjaan tugas ini, terutama untuk memahami konsep CSS, responsive design, semantic HTML, penggunaan Git, debugging, serta membantu menyusun dokumentasi dan refleksi tugas.

Dalam proses implementasi, saya tidak langsung menyalin seluruh kode yang diberikan oleh AI. Saya mencoba mengetik, menguji, dan memahami perubahan secara bertahap agar saya mengetahui fungsi dari bagian yang saya tambahkan ke project.

Beberapa konsep yang saya pelajari dengan bantuan AI antara lain CSS Grid, `grid-template-columns`, media query, hover, transition, perbedaan `margin`, `padding`, dan `gap`, penggunaan unit `rem`, serta perubahan layout antara desktop dan mobile.

Saya juga ikut menentukan beberapa keputusan desain dan fitur pada website. Salah satu ide yang saya berikan adalah membuat nama institusi pendidikan dapat diklik menuju situs terkait. Saya kemudian mengusulkan agar indikator external link berbentuk panah tidak selalu terlihat, tetapi hanya muncul ketika pengguna mengarahkan kursor ke Education item. AI membantu menjelaskan bagaimana ide tersebut dapat diimplementasikan menggunakan HTML, CSS pseudo-element, hover, opacity, transform, dan transition.

Selama pengerjaan, saya menemukan bahwa saran AI tidak selalu langsung sesuai dengan kondisi project. Beberapa bagian perlu diperiksa kembali atau diperbaiki setelah diuji, seperti kesalahan pada selector CSS, duplikasi style, penulisan unit CSS, dan penempatan transition pada elemen yang tepat.

Karena itu, saya tetap melakukan pengecekan manual menggunakan localhost, responsive view pada browser, `git status`, dan `git diff`. Saya juga melakukan commit secara bertahap setelah suatu bagian selesai agar perubahan project dapat dilacak dengan lebih jelas.

ChatGPT juga saya gunakan untuk membantu merapikan penulisan README dan jawaban refleksi. Isi refleksi tetap didasarkan pada pengalaman dan proses yang saya alami selama mengerjakan project, sedangkan AI membantu membuat penyampaiannya menjadi lebih jelas dan terstruktur.

Secara keseluruhan, AI membantu mempercepat proses belajar, debugging, dan dokumentasi. Namun, ide desain, pengujian hasil, pemilihan perubahan yang digunakan, serta keputusan akhir implementasi tetap saya tentukan berdasarkan hasil yang saya lihat dan pahami dari project saya sendiri.

### AI Prompting Log

Berikut beberapa contoh prompt yang saya gunakan selama pengerjaan:

- "Jelaskan fungsi `display: grid`, `grid-template-columns`, `gap`, dan `padding` pada bagian Education agar saya memahami setiap baris CSS yang digunakan."

- "Jelaskan perbedaan `margin`, `padding`, dan `gap` menggunakan contoh yang sederhana."

- "Bagaimana cara membuat bagian Education yang menggunakan tiga kolom di desktop berubah menjadi satu kolom ketika dibuka melalui HP?"

- "Coba cek CSS saya dan jelaskan bagian mana yang salah atau tidak diperlukan, jangan langsung menulis ulang seluruh kode."

- "Bagaimana cara membuat nama Universitas Indonesia pada bagian Education bisa diklik dan mengarah ke website resminya?"

- "Tolong buatkan agar tanda panah external link tidak terlihat saat biasa, tetapi muncul ketika kursor diarahkan ke bagian Education."

- "Jelaskan fungsi `opacity`, `transform`, dan `transition` pada efek tanda panah tersebut agar saya memahami cara kerjanya."

- "Coba cek perubahan Git saya terlebih dahulu dan jelaskan file mana yang sebaiknya dimasukkan ke commit."

- "Bagaimana cara melakukan commit secara bertahap agar Git history saya tetap rapi dan setiap commit mewakili satu perubahan?"

- "Bagaimana cara menjalankan project Django saya di localhost menggunakan virtual environment?"

- "Coba evaluasi README saya berdasarkan kebutuhan Tugas 1 dan jelaskan bagian mana yang masih kurang."

- "Tolong bantu rapikan jawaban refleksi saya tanpa mengubah inti jawaban dan pengalaman yang saya alami selama mengerjakan tugas."