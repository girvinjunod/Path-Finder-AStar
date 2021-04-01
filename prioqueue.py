class PrioQueue:
    #ctor
    def __init__(self):
	    self.prioqueue = []

    #buat print prioqueue
    def __str__(self):
        return ' '.join([str(i) for i in self.prioqueue])

	# cek kosong
    def isEmpty(self):
        return len(self.prioqueue) == 0

	# enqueue elemen, prionya ada di dequeue jadi ga usah diurutin di enqueue
    def enqueue(self, data):
        self.prioqueue.append(data)

	# dequeue dari yg terkecil
    def dequeue(self):
        min = 0
        for i in range(len(self.prioqueue)):
            if self.prioqueue[i][0] < self.prioqueue[min][0]:
                min = i
        pilihmin = self.prioqueue[min]
        del self.prioqueue[min]
        return pilihmin