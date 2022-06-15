# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.leftHeap = MaxHeap()
        self.rightHeap = MinHeap()

    def insert(self, number):
        if self.leftHeapLength() == self.rightHeapLength():
            if (self.leftHeapLength() > 0) and (self.rightHeap.peek() < number):
                numberToInsertInLeftHeap = self.rightHeap.remove()
                self.rightHeap.insert(number)
                self.leftHeap.insert(numberToInsertInLeftHeap)
            else:
                self.leftHeap.insert(number)
                
            self.median = self.leftHeap.peek()
        else:
            if self.leftHeap.peek() > number:
                numberToInsertInLeftHeap = self.leftHeap.remove()
                self.leftHeap.insert(number)
                self.rightHeap.insert(numberToInsertInLeftHeap)
            else:
                self.rightHeap.insert(number)
                
            self.median = (self.leftHeap.peek() + self.rightHeap.peek()) / 2
    
    def leftHeapLength(self):
        return len(self.leftHeap.array)
    
    def rightHeapLength(self):
        return len(self.rightHeap.array)

    def getMedian(self):
        return self.median
    
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

class MaxHeap():
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
            
            if self.array[p] < self.array[i]:
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
                if self.array[l] >= self.array[r]:
                    c = l
                else:
                    c = r
            elif l < len(self.array):
                c = l
            else:
                break
                
            if self.array[i] < self.array[c]:
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
