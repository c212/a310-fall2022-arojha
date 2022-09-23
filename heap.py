
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
    def min_heap(self):
        i = len(self.hp)//2
        for _ in range(i):
            i = len(self.hp)//2
            while i>=0:
                #print(i)
                self.heapify(i)
                i-=1

arr  = [9,4,7,3,15,22,100,1]
d = heap(arr)
print(d.hp)
print(d.leaf_node(4))
d.min_heap()
print(d.hp)

