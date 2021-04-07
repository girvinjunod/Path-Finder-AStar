from prioqueue import PrioQueue
from haversine import haversineDistance

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