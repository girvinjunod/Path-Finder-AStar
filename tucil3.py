#Tucil Stima 3

#Girvin Junod 13519096 K02
#

from prioqueue import PrioQueue
from vgraf import GraphVisualization

def euclideanDistance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

#input file
'''
#nanti diganti jadi parse dari file
#koordinat tiap simpul
listkoordinat = [(0,0), (3,4), (3,0), (11,4), (11,-6)] 
#matrix adj
matrixjalan = [ #blom ada handle kasus g ada jalan
[0,1,1,0,0],
[1,0,1,1,0],
[1,1,0,0,1],
[0,1,0,0,1],
[0,0,1,1,0]
]
#nama simpul
nama = ['A', 'B', 'C', 'D', 'E']

#nama jalan, klo cukup nampilin node aj buang aj
matrixnama = [
["-","AB","AC","AD","AE"], #0
["BA","-","BC","BD","BE"], #1
["CA","CB","-","CD","CE"], #2
["DA","DB","DC","-","DE"], #3
["EA","EB","EC","ED","-"] #4
]
'''
namafile = input("Nama file: ")
f = open(namafile) #baca soal
read = f.read().split('\n') #dipisahkan dari newline
listkoordinat = []
nama = []
matrixjalan = []
#liat format di txt
for i in range(len(read)):
    if ("=" in read[i]):
        nexti = i+1
        break
    idxpostnama = read[i].index("-")
    nama.append(read[i][0:idxpostnama-1])
    read[i] = read[i].replace(" ", "") #hapus spasi
    idxpostnama = read[i].index("-") + 1
    read[i] = read[i][idxpostnama:]
    templist = read[i].split(",")
    listkoordinat.append((float(templist[0]), float(templist[1])))
for i in range(nexti, len(read)):
    templist = read[i].split(" ")
    for j in range(len(templist)):
        templist[j] = int(templist[j])
    matrixjalan.append(templist)
n = len(listkoordinat)
#matrix buat jarak eclidean
matrixgeo = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        matrixgeo[i][j] = euclideanDistance(listkoordinat[i], listkoordinat[j])

#list[prediksi, sejauhini, path, nama]

#coba2 gambar graf
#Gambar graf
graf = GraphVisualization()
for i in range(n):
    for j in range(n):
        if (matrixjalan[i][j]):
            graf.addEdge(nama[i], nama[j], matrixgeo[i][j])
graf.visualize()

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

#Mulai algo
kawal = nama.index(entry)
ktujuan = nama.index(target)
awal = [matrixgeo[kawal][ktujuan] ,0, [entry], entry]
listjalan = PrioQueue()
listjalan.enqueue(awal)
while not listjalan.isEmpty():
    popped = listjalan.dequeue()
    if (popped[3] == target):
        break
    path = popped[2]
    indeks = nama.index(popped[3])
    for i in range(len(matrixjalan[indeks])):
        if (matrixjalan[indeks][i]):
            sofar = popped[1] + matrixgeo[indeks][i]
            isipath = []
            for j in range(len(path)):
                isipath.append(path[j])
            isipath.append(nama[i])
            grup = [matrixgeo[i][ktujuan] + sofar, sofar, isipath, nama[i]]
            listjalan.enqueue(grup)
hasil = popped[2]
distance = popped[1]

#output dari node ke node
print("Jalur (node):")
for i in hasil:
    if i == target:
        print(i)
    else:
        print(i, end = "-")
print("Panjang jalur:" , '{0:.3g}'.format(distance))

'''#output node-sisi-node-dst
print()
print("Jalur (jalan + node):")
for i in range(len(hasil) - 1):
    print(hasil[i], end= "-")
    a = hasil[i]
    b = hasil[i+1]
    ka = nama.index(a)
    kb = nama.index(b)
    print(matrixnama[ka][kb], end = "-")
print(hasil[i+1])
print("Panjang jalur:" , distance)'''

graf.keep()