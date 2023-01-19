import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def print(self):
        return "("+str(self.x)+", "+str(self.y)+")"
    def distance_to_another_point(self,a):
        return math.sqrt((self.x-a.x)**2 + (self.y-a.y)**2)
    
ptr = Point(1,1)
#ptr.print()
origin = Point(0,0)
#print(ptr.distance_to_another_point(origin))

class Line_segment:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def print(self):
        print("Line segment is between the points "+self.p1.print()+" and "+self.p2.print())
    def length_of_line_segment(self):
        return self.p1.distance_to_another_point(self.p2)

l1 = Line_segment(origin,ptr)
#l1.print()
#print(l1.length_of_line_segment())



class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.a = self.p1.distance_to_another_point(self.p2)
        self.b = self.p2.distance_to_another_point(self.p3)
        self.c = self.p3.distance_to_another_point(self.p1)
        self.s = (self.a+self.b+self.c)/2
    def area_of_my_triangle(self): # triangle inequality
        return math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
ptr2 = Point(2,3)
tri = Triangle(origin,ptr,ptr2)
#print(tri.area_of_my_triangle())
#print(" Value of object",ptr2)
class Linked_list:
    def __init__(self,data):
        self.data = data
        self.next = None
    def insert(self,next_data):
        next_node = Linked_list(next_data)
        a = self
        while a.next!=None:
            a=a.next
        a.next = next_node
    def print(self):
        a = self
        while a!=None:
            print(a.data)
            a = a.next

        #while True:
        #    print(a.data)
        #    a=a.next
        #    if a==None:
        #        break
        
ll = Linked_list('A')
ll.insert('B')
ll.insert('C')
ll.insert('D')
ll.print()


class Binary_Tree:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
    def insert(self,)
    
bst = Binary_Tree(8,\
                  Binary_Tree(3\
                              ,Binary_Tree(1,None,None),\
                              Binary_Tree(6,None,None))\
                  ,Binary_Tree(10,None,Binary_Tree(14,None,None)))

one = Binary_Tree(1,None,None)
four = Binary_Tree(4,None,None)
seven  =Binary_Tree(7,None,None)
six = Binary_Tree(6,four,seven)
three = Binary_Tree(3,one,six)
fourteen = Binary_Tree(14,None,None)
ten = Binary_Tree(10,None,fourteen)
eight = Binary_Tree(8,three,ten)


































        



