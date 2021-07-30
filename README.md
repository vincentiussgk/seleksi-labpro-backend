# seleksi-labpro-backend

Stack:
- Framework: Flask (Python)
- ORM: SQLAlchemy
- Database: MySQL/MariaDB

Instalasi:
(Instruksi instalasi menggunakan OS Windows sebagai acuan)

Pertama, untuk setup database:

0. Untuk keperluan Database, dibutuhkan MariaDB (https://mariadb.com/downloads/). Versi yang dipakai adalah 10.6.3-GA
0a. Untuk men-setup database, bukalah installer MariaDB, set port=3306 dan password=admin.
0b. Setelah selesai, jalankan mariadb (bisa melalui search di taskbar), dan masuk dengan password admin.
0c. Buatlah database dengan perintah ``create database DoraemonDB``.

Sekarang, untuk setup backend:

1. Jalankan perintah ``py -3 -m venv venv``
2. Kemudian, jalankan ``venv\Scripts\activate``
2a. Jika langkah 2 gagal, bukalah Powershell sebagai admin, kemudian jalankan ``Set-ExecutionPolicy RemoteSigned`` dan ulangi 
kembali langkah 2. Untuk mencegah *security risk*, setelah menyelesaikan langkah 2, jalankan ``Set-ExecutionPolicy Restricted``
pada Powershell.
3. Sekarang, kita berada pada virtual environment yang sudah di-setup. Jalankan ``pip install Flask`` untuk mendownload Flask.
4. Untuk menjalankan server, jalankan perintah ``$env:FLASK_APP = "app"`` untuk meng-export aplikasi kita, dan jalankan menggunakan
``flask run``.
