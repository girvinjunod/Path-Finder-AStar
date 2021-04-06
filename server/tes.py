from prioqueue import PrioQueue
from haversine import haversineDistance
import os
from pathlib import Path
def parsefile(namafile):
    #input file
    filepath = os.path.dirname(Path(__file__).absolute().parent)
    namafile1 = os.path.join(filepath, 'test', namafile)
    f = open(namafile1) #baca soal
    read = f.read().split('\n') #dipisahkan dari newline
    listkoordinat = []
    nama = []
    matrixjalan = []
    n = int(read[0])
    #liat format di txt
    for i in range(1, n+1):
        idxpostnama = read[i].index("|") #pisahin berdasarkan -
        nama.append(read[i][0:idxpostnama-1]) #isi list nama
        read[i] = read[i].replace(" ", "") #hapus spasi
        idxpostnama = read[i].index("|") + 1 #ambil indeks koordinat
        read[i] = read[i][idxpostnama:] #jadi koordinat aj
        templist = read[i].split(",") #pisahin berdasarkan koma
        listkoordinat.append((float(templist[0]), float(templist[1]))) #dibuat jadi tuple dan dimasukin ke list
    nexti = i+1 #buat ngeliat matriks jalan di input
    for i in range(nexti, len(read)):
        templist = read[i].split(" ") #pisahin dari spasi
        for j in range(len(templist)):
            templist[j] = int(templist[j]) #konversi input dari str ke int, biar jadi boolean
        matrixjalan.append(templist)

    #matrix buat jarak euclidean (jarak garis lurus antar simpul)
    #Sebenarnya karena bumi ga datar, pakai haversine formula buat jarak antar 2 simpul, ga euclidean
    matrixgeo = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrixgeo[i][j] = haversineDistance(listkoordinat[i], listkoordinat[j])
    return nama, matrixjalan, matrixgeo, listkoordinat

def buatmatrixdistance(matrixjalan, listkoordinat):
    n = len(matrixjalan)
    matrixgeo = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrixgeo[i][j] = haversineDistance(listkoordinat[i], listkoordinat[j])
    return matrixgeo

def astar2(entry,target, matrixjalan, matrixgeo,listkoordinat):
    #Mulai algo A*
    listvisited = [] #Cek apakah sudah di visit atau blom, hanya untuk handle kasus tidak ada jalur
    idxawal = listkoordinat.index(entry) #indeks awal
    idxtujuan = listkoordinat.index(target) #indeks tujuan
    #list awal
    #list[estimasi, sejauhini, path, nama]
    awal = [matrixgeo[idxawal][idxtujuan] ,0, [entry], entry]
    #prioqueue untuk A*, prioritas dari estimasi
    listjalan = PrioQueue()
    listjalan.enqueue(awal) #prioqueue dari list
    found = False
    while not listjalan.isEmpty():
        popped = listjalan.dequeue() #dequeue dari list
        listvisited.append(popped[3])
        if (popped[3] == target): #kalau sudah ketemu target di end
            found = True
            break
        path = popped[2] #ambil path sejauh ini
        indeks = listkoordinat.index(popped[3]) #ambil indeks nama dari yang didequeue
        for i in range(len(matrixjalan[indeks])):
            if (matrixjalan[indeks][i] and listkoordinat[i] not in listvisited): #jika ada jalur
                sofar = popped[1] + matrixgeo[indeks][i]
                isipath = []
                for j in range(len(path)):
                    isipath.append(path[j])
                isipath.append(listkoordinat[i])
                grup = [matrixgeo[i][idxtujuan] + sofar, sofar, isipath, listkoordinat[i]]
                listjalan.enqueue(grup) #Masukkan ke prioqueue
    listedge = []
    if found:
        jalan = popped[2]
        distance = popped[1]
        for i in range(len(jalan) - 1):
            listedge.append([jalan[i], jalan[i+1]])
        return jalan, listedge, found, distance
    return popped, listedge, found, 0
namafile = 'bucharest.txt' #input file
nama, matrixjalan, matrixgeo, listkoordinat = parsefile(namafile)
entry = (44.457, 26.093)
target = (46.181, 21.312)
hasil, listedge, found, distance = astar2(entry, target, matrixjalan, matrixgeo, listkoordinat)
if found:
    print("Edges:", listedge)
    print("Path:", hasil)
    print("Distance:", distance, "km")
else:
    print("G ada jalan weh")
#matrixdistance = buatmatrixdistance(matrixjalan, listkoordinat)