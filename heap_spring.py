

class Heap:
    def __init__(self):
        self.heap = [-99999]
    # n is the index 
    def left(self,n):
        return 2*n
    def right(self,n):
        return 2*n+1
    def parent(self,n):
        if n==0:
            return None
        else:
            return n//2
    def insert(self,val):
        self.heap.append(val)
        self.heapify(len(self.heap)-1)
    def heapify(self,n):
        #[inf,9,29,21,44,97,24]
        # iteration 1
        # parent = 3
        # n = 6
        #
        # iteration 2
        # n = 3
        # parent = 1
        parent = self.parent(n)
        if parent ==None:
            return 
        elif self.heap[parent]>self.heap[n]:
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            self.heapify(parent)
    def heapify_top_down(self,n):
        # n = 1
        #left = 2n; right = 2n+1
        # leftn = 2
        left = self.left(n)
        right = self.right(n)
        len_heap = len(self.heap)
        if right>=len_heap:
            if left>=len_heap:
                return
            else:
                if self.heap[left]<self.heap[n]:
                    self.heap[left],self.heap[n] = self.heap[n],self.heap[left]
        else:
            min_index = n
            if self.heap[left]<self.heap[right]:
                min_index = left
            else:
                min_index = right
            if self.heap[n]>self.heap[min_index]:
                self.heap[min_index],self.heap[n] = self.heap[n],self.heap[min_index]
                self.heapify_top_down(min_index)
    def delete(self):
        #[-99999, 9, 29, 21, 44, 97, 24]
        # iteraion 1
        #[-99999, 21, 29, 24, 44, 97, ]
        self.heap[1] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify_top_down(1)
        


h = Heap()
print("----------------( now inserting 9 )--")
h.insert(9)
print(h.heap)
print("----------------( now inserting 8 )--")
h.insert(8)
print(h.heap)
print("----------------( now inserting 7 )--")
h.insert(7)
print(h.heap)
print("----------------( now inserting 6 )--")
h.insert(6)
print(h.heap)
print("----------------( now inserting 5 )--")
h.insert(5)
print(h.heap)
print("----------------( now inserting 4 )--")
h.insert(4)
print(h.heap)
print("----( now deleting )----")
h.delete()
print(h.heap)
print("----( now deleting )----")
h.delete()
print(h.heap)
print("----( now deleting )----")
h.delete()
print(h.heap)
print("----( now deleting )----")
h.delete()
print(h.heap)
