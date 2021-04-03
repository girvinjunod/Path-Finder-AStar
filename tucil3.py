#Tucil Stima 3

#Girvin Junod 13519096 K02
#

from prioqueue import PrioQueue
from peta import MapV
from haversine import haversineDistance

def euclideanDistance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

#input file

namafile = input("Nama file: ")
f = open(namafile) #baca soal
read = f.read().split('\n') #dipisahkan dari newline
listkoordinat = []
nama = []
matrixjalan = []
n = int(read[0])
#liat format di txt
for i in range(1, n+1):
    idxpostnama = read[i].index("-")
    nama.append(read[i][0:idxpostnama-1])
    read[i] = read[i].replace(" ", "") #hapus spasi
    idxpostnama = read[i].index("-") + 1
    read[i] = read[i][idxpostnama:]
    templist = read[i].split(",")
    listkoordinat.append((float(templist[0]), float(templist[1])))
nexti = i+1
for i in range(nexti, len(read)):
    templist = read[i].split(" ")
    for j in range(len(templist)):
        templist[j] = int(templist[j])
    matrixjalan.append(templist)

#matrix buat jarak euclidean (jarak garis lurus antar simpul)
#Sebenarnya karena bumi ga datar, pakai haversine formula buat jarak antar 2 simpul, ga euclidean
matrixgeo = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        matrixgeo[i][j] = haversineDistance(listkoordinat[i], listkoordinat[j])

listlat = []
listlon = []
for i in range(n):
    listlat.append(listkoordinat[i][0])
    listlon.append(listkoordinat[i][1])
#Buat map
map = MapV(listlat, listlon, nama)

#Isi jalur di map
for i in range(n):
    for j in range(n):
        listlat = []
        listlon = []
        name = []
        if (matrixjalan[i][j]):
            listlat.append(listkoordinat[i][0])
            listlat.append(listkoordinat[j][0])
            listlon.append(listkoordinat[i][1])
            listlon.append(listkoordinat[j][1])
            name.append(nama[i])
            name.append(nama[j])
            map.tambahjalur(listlat, listlon, name)

#input node awal dan akhir
print("Pilihan Node: ")
for i in nama:
    print(i, end=" ")
print()
while(1):
    entry = input("Masukkan node awal: ")
    target = input("Masukkan node target: ")
    if (entry not in nama or target not in nama):
        print("input invalid, please try again")
        print()
    else:
        break

#Tambah simpul awal akhir di map
nwal = [entry]
latawal = [listkoordinat[nama.index(entry)][0]]
lonawal = [listkoordinat[nama.index(entry)][1]]
nakhir = [target]
latakhir = [listkoordinat[nama.index(target)][0]]
lonakhir = [listkoordinat[nama.index(target)][1]]
map.tambahAwal(latawal, lonawal, nwal)
map.tambahAkhir(latakhir, lonakhir, nakhir)

#Mulai algo A*
kawal = nama.index(entry) #koordinat awal
ktujuan = nama.index(target) #koordinat tujuan
#list awal
#list[estimasi, sejauhini, path, nama]
awal = [matrixgeo[kawal][ktujuan] ,0, [entry], entry]

#prioqueue untuk A*, prioritas dari estimasi
listjalan = PrioQueue()
listjalan.enqueue(awal) #prioqueue dari list
while not listjalan.isEmpty():
    popped = listjalan.dequeue() #dequeue dari list
    if (popped[3] == target): #kalau sudah ketemu target di end
        break
    path = popped[2] #ambil path sejauh ini
    indeks = nama.index(popped[3]) #ambil indeks nama dari yang didequeue
    for i in range(len(matrixjalan[indeks])):
        if (matrixjalan[indeks][i]): #jika ada jalur
            sofar = popped[1] + matrixgeo[indeks][i]
            isipath = []
            for j in range(len(path)):
                isipath.append(path[j])
            isipath.append(nama[i])
            grup = [matrixgeo[i][ktujuan] + sofar, sofar, isipath, nama[i]]
            listjalan.enqueue(grup) #Masukkan ke prioqueue

hasil = popped[2] #Path dari awal ke akhir
distance = popped[1] #total jarak akhir

#memasukkan hasil ke map
listlathasil = []
listlonhasil = []
namahasil = []
for i in range(len(hasil)):
    idxhasil = nama.index(hasil[i])
    listlathasil.append(listkoordinat[idxhasil][0])
    listlonhasil.append(listkoordinat[idxhasil][1])
    namahasil.append(nama[idxhasil])

map.tambahjalurhasil(listlathasil,listlonhasil, hasil)

#output dari jalur dan distancenya
print("Jalur terpendek:")
for i in hasil:
    if i == target:
        print(i)
    else:
        print(i, end = "-")
print("Panjang jalur:", distance, "km")

map.visualize() #panggil map