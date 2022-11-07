class PriorityQueueSortedList:
    def __init__(self):
            self._data = []
            self._size = 0
    
    def peek(self):
        print(f"Data prioritas tertinggi: ('{self._data[0][0]}', {self._data[0][1]})")
    
    def add(self,d,p):
        if self._size == 0:
            self._data.append([d,p])
        else:
            x = 0
            while self._data[x][1] < p:
                x += 1
            self._data.insert(x,[d,p])
        self._size +=1

    def update(self,prioBaru,dataBaru):
            x = 0
            while self._data[x][1] != prioBaru:
                x += 1
            del self._data[x]
            self._data.insert(x,[dataBaru,prioBaru])

    def remove(self):
        pp = self._data[0][1]
        while self._data[0][1] == pp:
            del self._data[0]

    def removePriority(self,p):
        x = 0
        while self._data[x][1] != p:
            x += 1
        while self._data[x][1] == p:
            del self._data[x]
    def printAll(self):
        print('Isi Semua Queue:',end=' ')
        for i in range(0,len(self._data)):
            if i == len(self._data) -1:
                print(f"('{self._data[i][0]}', {self._data[i][1]})")
            else:
                print(f"('{self._data[i][0]}', {self._data[i][1]}), ",end = '')

sortedList = PriorityQueueSortedList() 
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printAll()
