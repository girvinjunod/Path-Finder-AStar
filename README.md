# Description
Repository untuk tucil 3 stima tentang algoritma Astar untuk penemuan jalur terpendek di peta. 
Program kami dibagi menjadi program normal dan program bonus. 
Program normal berupa program yang menerima input nama file input dari terminal, input node awal dan tujuan. 
Lalu program akan menampilkan jalur terdekat antara kedua node beserta jaraknya serta menampilkannya dalam sebuah peta.
Program bonus berupa program yang dapat menampilkan suatu peta dunia, lalu pengguna dapat mengklik titik-titik di peta untuk
membuat node-node dan juga bisa menghubungkan node-node tersebut membentuk sebuah graf di peta. Lalu, user dapat memilihi dua node
untuk dicari jalur terdekatnya dan program akan menampilkannya di peta serta jaraknya.
## Dependencies
- Python 3.8.8 (Dicoba di versi ini, versi lain bisa jadi tidak bisa)
### non-bonus
- plotly, install dengan `pip install plotly`. Cek apakah sudah terinstall dengan `pip show plotly`

### bonus
- Nodejs, install dari https://nodejs.org/en/. Cek apakah sudah terinstall dengan `node -v` dan `npm -v`. Pastikan npm sudah versi latest dengan `npm install npm@latest -g`
- Vuejs, bisa diinstall dengan command `npm install -g @vue/cli`
- Yarn, jika dipakai, install dengan `npm install --global yarn`
- Dependencies lain dapat diinstall dengan `yarn install` atau `npm install` saat berada di directory frontend
- Flask (pada python), install dengan `pip install flask`. Cek apakah sudah terinstall dengan `pip show flask`
- Flask_cors (pada python), install dengan `pip install flask_cors`

## How to Run:

### Menjalankan non-bonus:
- Masuk ke folder `src`
- jalankan `python normal.py` di terminal
- Akan diprint hasil jalur dan jarak di terminal, lalu akan membuka tampilan peta di browser Anda (jika gagal konek ke server lokal coba jalankan lagi programnya)
- Masukkan input nama file, pastikan file input ada di folder test
- Masukkan input pilihan untuk node awal dan akhir untuk pencarian jalur
### Menjalankan bonus:
#### Set-up
- Pindah ke folder frontend dengan menjalankan `cd src/frontend`
- Masukkan command `yarn install` atau `npm install`
- jalankan `npm run serve`
- Terminal akan menampilkan link website lokal, misal `http://localhost:8080/`, klik link tersebut.
- Buka terminal lain, pergi ke folder server
- Install flask dengan command `pip install flask` dan install flask_cors dengan command `pip install flask_cors`, apabila belum menginstall flask dan flask_cors
- Masukkan command `python app.py` di terminal lain tersebut
- Sekarang frontend dan backend sudah berhasil dinyalakan
#### Menggunakan web
- Graf dibuat dengan membuat kumpulan sisi dengan mengklik dua titik yang berhubungan
- Bila sudah selesai membuat graf, klik tombol `selesai membuat graf`
- Pilih 2 titik sebagai titik asal dan tujuan pathfinding
- Bila sudah, klik tombol `OK!`
- Hasil pathfinding akan ditampilkan pada map dan jarak antar kedua titik pun akan ditampilkan
- Untuk melakukan lagi, refresh website lokal

## Author:
- Girvin Junod 13519096
- Hera Shafira 13519131

## Disclaimer:
Bila menemukan kesulitan dalam menjalankan program harap hubungi id line : herash
