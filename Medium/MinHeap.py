# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.buildHeap(array)

    def parentIndex(self, i):
        return int((i - 1) / 2)

    def leftChildIndex(self, i):
        return (i * 2) + 1

    def rightChildIndex(self, i):
        return (i * 2) + 2

    def buildHeap(self, array):
        for a in array:
            self.insert(a)

    def siftDown(self, heap):
        i = 0

        while i < len(heap) - 1:
            l = self.leftChildIndex(i)
            r = self.rightChildIndex(i)

            if (l < len(heap)) and (r < len(heap)):
                if heap[l] < heap[r]:
                    c = l
                else:
                    c = r
            elif l < len(heap):
                c = l
            else:
                return heap

            if heap[c] < heap[i]:
                swap(heap, i, c)
                i = c
            else:
                return heap

    def siftUp(self, heap):
        i = len(heap) - 1

        while i > 0:
            p = self.parentIndex(i)

            if heap[p] > heap[i]:
                swap(heap, i, p)
                i = p
            else:
                return heap

    def peek(self):
        return self.heap[0]

    def remove(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.siftDown(self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
