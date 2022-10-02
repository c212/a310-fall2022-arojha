class heap:
    def __init__(self,arr):
        self.hp = arr
        self.l = len(arr)
    def leaf_node(self,pos):
        if 2*pos+1>=self.l:
            return False
        elif self.hp[2*pos+1]==None:
            return False
        return True
    def heapify(self,pos):
        if self.leaf_node(pos)==True:
            if 2*pos+2==self.l:
                if self.hp[pos]>self.hp[2*pos+1]:
                    self.hp[pos],self.hp[2*pos+1] = self.hp[2*pos+1],self.hp[pos]
            else:
                if self.hp[2*pos+1]<self.hp[2*pos+2]:
                    if self.hp[pos]>self.hp[2*pos+1]:
                        self.hp[pos],self.hp[2*pos+1] = self.hp[2*pos+1],self.hp[pos]
                elif self.hp[2*pos+1]>self.hp[2*pos+2]:
                    if self.hp[pos]>self.hp[2*pos+2]:
                        self.hp[pos],self.hp[2*pos+2] = self.hp[2*pos+2],self.hp[pos]  
    def insert(self,val):
        self.hp.append(val)
        self.l+=1
        self.min_heap()
    def delete(self):
        k = self.hp[0]
        print("deleting {}".format(k))
        self.hp[0] = self.hp[-1]
        del self.hp[-1]
        self.l-=1
        self.min_heap()
    def min_heap(self):
        i = len(self.hp)//2
        for _ in range(i):
            i = len(self.hp)//2
            while i>=0:
                #print(i)
                self.heapify(i)
                i-=1

arr  = [9]
d = heap(arr)
print(d.hp)
# indert elements
d.insert(4)
d.insert(7)
d.insert(3)
d.insert(15)
d.insert(22)
d.insert(100)
d.insert(1)
print(d.hp)

#delete elements
d.delete()
print(d.hp)
d.delete()
print(d.hp)
