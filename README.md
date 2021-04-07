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
#### Library Python
- plotly, install dengan `pip install plotly`. Cek apakah sudah terinstall dengan `pip show plotly`

### bonus
- Nodejs, install dari https://nodejs.org/en/. Cek apakah sudah terinstall dengan `node -v` dan `npm -v`. Pastikan npm sudah versi latest dengan `npm install npm@latest -g`
- Dependencies lain dapat diinstall dengan `npm install`
#### Library Python
- Flask, install dengan `pip install flask`. Cek apakah sudah terinstall dengan `pip show flask`

## How to Run:

#### Menjalankan non-bonus:
- ketik dan enter `python src/normal.py` di terminal
- Akan diprint hasil jalur dan jarak di terminal, lalu akan membuka tampilan peta di browser Anda (jika gagal konek ke server lokal coba jalankan lagi programnya)
- Masukkan input nama file, pastikan file input ada di folder test
- Masukkan input pilihan untuk node awal dan akhir untuk pencarian jalur
#### Menjalankan bonus:
- Pastikan semua dependencies sudah terinstall
- jalankan `cd src/frontend`
- jalankan `npm run serve`
- Akan ditunjukkan di terminal letak program di suatu server, pergi ke salah satu pilihannya. Misal `http://localhost:8080/`
- Klik titik di map untuk membuat node, klik dua titik untuk membuat suatu sisi antar node
- Klik tombol 'x' untuk berhenti membuat graf
- Klik 2 node sebagai node awal dan akhir pencarian jalur
- Klik tombol 'x' untuk menunjukkan jalur terpendek antara dua node itu dan jaraknya

## Author:
- Girvin Junod 13519096
- Hera Shafira 13519131
