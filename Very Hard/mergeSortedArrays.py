class MinHeap():
    def __init__(self):
        self.array = []
    
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
    
    def peek(self):
        return self.array[0]

def mergeSortedArrays(arrays):
    mergedArray = []
    heap = MinHeap()
    arrayLookup = {}
    arrayIndexes = [0] * len(arrays)
    
    for i in range(len(arrays)):
        heapInsert(heap, arrayLookup, arrays[i][0], i)
    
    while len(heap.array) > 0:
        number = heap.remove()
        mergedArray.append(number)
        i = arrayLookup[number].pop(0)
        arrayIndexes[i] += 1
        
        if arrayIndexes[i] < len(arrays[i]):
            heapInsert(heap, arrayLookup, arrays[i][arrayIndexes[i]], i)
    
    return mergedArray
    
    

def heapInsert(heap, arrayLookup, number, arrayIndex):
    heap.insert(number)
    
    if number in arrayLookup:
        arrayLookup[number].append(arrayIndex)
    else:
        arrayLookup[number] = [arrayIndex]
