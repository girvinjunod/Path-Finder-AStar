from prioqueue import PrioQueue

def euclideanDistance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    
#20x20, diambil dari ppt
#lanjutin aja klo mau tes
'''matrixjalan = [
[1,2,3], #Arad
[1,6,7], #Zerind
[6,9], #Oradea
[], #Sibiu
[], #Fagaras
[], #Timiscara
[], #Lugoj
[], #Mehadia
[], #Dobreta
[], #Cralova
[], #Riminu vicea
[], #Pitesti
[], #Bucharest
[], #Giurgiu
[], #Urziceni
[], #Neamt
[], #Iasi
[], #Vasiui
[], #Hirsova
[] #Evorie
]'''

'''
matrixjalan = [ #weighted adj matrix
[0,2,3,0,0],
[2,0,15,2,0],
[3,15,0,0,13],
[0,2,0,0,9],
[0,0,13,9,0]
]
matrixgeo = [
[0,2,3,3,14], #0
[2,0,15,2,9.5], #1
[3,15,0,16,13], #2
[3,2,16,0,9], #3
[14,9.5,13,9,0] #4
]
'''

#input file
#nanti diganti jadi parse dari file
#koordinat tiap simpul
listkoordinat = [(0,0), (3,4), (3,0), (11,4), (11,-6)] 
n = len(listkoordinat)
#matrix buat jarak eclidean
matrixgeo = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        matrixgeo[i][j] = euclideanDistance(listkoordinat[i], listkoordinat[j])
#matrix adj
matrixjalan = [ 
[0,1,1,0,0],
[1,0,1,1,0],
[1,1,0,0,1],
[0,1,0,0,1],
[0,0,1,1,0]
]
#nama jalan, klo cukup nampilin node aj buang aj
matrixnama = [
["-","AB","AC","AD","AE"], #0
["BA","-","BC","BD","BE"], #1
["CA","CB","-","CD","CE"], #2
["DA","DB","DC","-","DE"], #3
["EA","EB","EC","ED","-"] #4
]
#nama simpul
nama = ['A', 'B', 'C', 'D', 'E']

#Mulai program


#list[prediksi, sejauhini, path, nama]
'''tes = PrioQueue()
tes.enqueue([200,100,['a','b','c'], 'c'])
tes.enqueue([255,135,['a','b','d'], 'd'])
tes.enqueue([150,100,['a','e','f'], 'f'])
tes.enqueue([225,75,['a','e','z'], 'z'])	
while not tes.isEmpty():
	print(tes.dequeue())'''
entry = 'A'
target = 'E'
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
#output dari node ke node
print("Jalur (node):")
for i in hasil:
    if i == target:
        print(i)
    else:
        print(i, end = "-")
#output node-sisi-node-dst
print("Jalur (jalan + node):")
for i in range(len(hasil) - 1):
    print(hasil[i], end= "-")
    a = hasil[i]
    b = hasil[i+1]
    ka = nama.index(a)
    kb = nama.index(b)
    print(matrixnama[ka][kb], end = "-")
print(hasil[i+1])