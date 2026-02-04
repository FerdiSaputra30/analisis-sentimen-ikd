# Analisis Sentimen Aplikasi Identitas Kependudukan Digital (IKD)

Aplikasi web untuk menganalisis sentimen ulasan pengguna aplikasi **Identitas Kependudukan Digital (IKD)** yang tersedia di Google Play Store.  
Analisis sentimen dilakukan untuk mengetahui kecenderungan opini pengguna terhadap aplikasi tersebut.

## Objek

Ulasan pengguna aplikasi **Identitas Kependudukan Digital (IKD)** yang diperoleh dari Google Play Store.

## Metode

Metode yang digunakan dalam aplikasi ini meliputi:
- Pengumpulan data ulasan pengguna Google Play Store (manual dalam format CSV)
- Pra-pemrosesan teks ulasan
- Analisis sentimen berbasis kamus kata (positif, negatif, netral)
- Visualisasi hasil analisis dalam bentuk statistik dan grafik pie
- Implementasi dalam aplikasi web berbasis Python Flask

## Teknologi yang Digunakan

- Python 3
- Flask
- HTML dan CSS
- Chart.js
- File CSV

## Cara Menggunakan Aplikasi

1. Buka aplikasi melalui browser
2. Upload file CSV yang berisi ulasan pengguna
3. Klik tombol Upload & Analisis
4. Sistem akan menampilkan:
                            1).Total ulasan
                            2).Jumlah dan persentase sentimen
                            3).Grafik pie distribusi sentimen
                            4).Kesimpulan hasil analisis
