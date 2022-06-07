class MinHeap():
    def __init__(self, array):
        self.array = []
        
        for a in array:
            self.insert(a)
    
    def parentIndex(self, i):
        return int((i - 1) / 2)
    
    def leftChildIndex(self, i):
        return (i * 2) + 1
    
    def rightChildIndex(self, i):
        return (i * 2) + 2
    
    def siftUp(self):
        i = len(self.array) - 1
        
        while i > 0:
            p = self.parentIndex(i)
            
            if self.array[p] > self.array[i]:
                self.array[p], self.array[i] = self.array[i], self.array[p]
                i = p
            else:
                break
    
    def siftDown(self):
        i = 0
        
        while i < len(self.array):
            l = self.leftChildIndex(i)
            r = self.rightChildIndex(i)
            
            if (l < len(self.array)) and (r < len(self.array)):
                if self.array[l] <= self.array[r]:
                    c = l
                else:
                    c = r
            elif l < len(self.array):
                c = l
            else:
                break
                
            if self.array[i] > self.array[c]:
                self.array[c], self.array[i] = self.array[i], self.array[c]
                i = c
            else:
                break

    def insert(self, x):
        self.array.append(x)
        self.siftUp()
    
    def remove(self):
        x = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.siftDown()
        return x
    
    def isValid(self):
        for i in range(len(self.array)):
            l = self.leftChildIndex(i)
            r = self.rightChildIndex(i)
            
            if (l < len(self.array)) and (self.array[i] > self.array[l]):
                return False
            
            if (r < len(self.array)) and (self.array[i] > self.array[r]):
                return False
        
        return True
    
    def length(self):
        return len(self.array)
    
def heapSort(array):
    sortedArray = []
    heap = MinHeap(array)
    
    while len(heap.array) > 0:
        sortedArray.append(heap.remove())
    
    return sortedArray
