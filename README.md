

## 🧩 TCP Server & Client – Pemrograman Socket Python

Proyek ini merupakan implementasi sederhana dari **komunikasi client-server berbasis TCP** menggunakan Python, dilengkapi dengan versi server **single-threaded** dan **multi-threaded**, serta satu halaman HTML pendukung untuk dokumentasi atau tampilan.

### 🔧 Fitur

* Komunikasi dua arah antara client dan server menggunakan TCP
* **SingleThread-Server**: server menangani satu client pada satu waktu
* **MultiThread-Server**: server dapat menangani banyak client secara bersamaan dengan threading
* **Client**: menghubungkan dan mengirim pesan ke server
* **kelompok.html**: berisi dokumentasi, identitas tim, atau tampilan web sederhana

### 📁 Struktur Proyek

```
/tcp_project
│
├── kelompok.html             # Halaman HTML berisi dokumentasi atau informasi kelompok
├── client.py                 # TCP client: menghubungkan ke server dan mengirim pesan
├── SingleThread-Server.py    # Server TCP sederhana (1 client dalam satu waktu)
└── MultiThread-Server.py     # Server TCP dengan dukungan multithreading (multi client)
```

### 🚀 Cara Menjalankan

1. Jalankan `SingleThread-Server.py` atau `MultiThread-Server.py` untuk mengaktifkan server.
2. Jalankan `client.py` untuk menghubungkan client ke server dan mengirim pesan.
3. (Opsional) Buka `kelompok.html` di browser untuk melihat dokumentasi atau informasi proyek.

### 📚 Kebutuhan

* Python 3.x
* Tidak memerlukan pustaka eksternal (menggunakan `socket` dan `threading` bawaan)

---

**Proyek ini sebagai latihan dasar pemrograman jaringan dan bisa dikembangkan untuk aplikasi chat, monitoring sistem, atau simulasi IoT.**

