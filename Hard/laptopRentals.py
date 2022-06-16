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

def laptopRentals(times):
    if len(times) == 0:
        return 0
    
    count = 1
    times = sortedByStartTimes(times)
    minHeap = MinHeap()
    minHeap.insert(times[0][1])
    
    for i in range(1, len(times)):
        if times[i][0] >= minHeap.peek():
            minHeap.remove()
            
        minHeap.insert(times[i][1])
        count = max(count, len(minHeap.array))
    
    return count

def sortedByStartTimes(times):
    return sorted(times, key = lambda t: t[0])
