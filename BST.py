class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)
    def is_leaf(self):
        if self.left==None and self.right==None:
            return True
        return False
    def delete(self,key):
        if self.key>key:
            if self.left.key == key:
                if self.left.is_leaf()==True:
                    self.left=None
                    return
            self.left.delete(key)
        elif self.key<key:
            if self.right.key == key:
                if self.right.is_leaf()==True:
                    self.right=None
                    return
            self.right.delete(key)
        else:
            t = self.right
            m = self
            k = 0
            while t.left!=None:
                if k==0:
                    m=m.right
                    k+=1
                else:
                    m=m.left
                    k+=1
                t=t.left
            self.key = t.key
            if k>0:
                m.left=t.right
            else:
                m.right=t.right


    def display(self):
        lines, *_ = self._display_aux() #lines is a list of strings
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key #creates a string of the root node, if root was 8 we would have '8' not the number 8
            width = len(line) # this will be 1 since the line is defined by the root, line only has 1 element (we are in no child)
            height = 1 #depth of the tree at a leaf (no children) is always 1
            middle = width // 2 # divisional floor
            return [line], width, height, middle # returns all 4 of these things, list of line, width, height, and middle 

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux() #list of lines, n = w, p = h, x = mid
            s = '%s' % self.key 
            u = len(s) # u will be the length of the number s, if 100 is inserted then u = 3, if 10 then u = 2 etc
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s # this is all spacing
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' ' # this is more spacing
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux() #[8] 1, 1, 0
        right, m, q, y = self.right._display_aux() #[12], 2, 1, 1
        s = '%s' % self.key # 11
        u = len(s) 
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

"""
This code iterates down the left side of the tree until it reaches a leaf, then it stores those values and determines the
right side of the left subtree. It then moves to the right subtree after the left subtree has been recursed through. This 
algorithm goes line by line and determines the number of spaces and underscores required to make the tree fit appropriately 
when printed. It stores the left subtree in the left list, and it stores the right subtree in the right list. Then,
it zips these two lists together, preserving and combining the spacing to ensure that the display looks correct. 
It stores each line in the tree in a list, then iterates through that list and prints each line which contains
the number of spaces, underlines, and connecting characters. 
"""
import random

b = BstNode(10)
#for k in range(50):
#   b.insert(random.randint(0, 100))
b.insert(5) 
b.insert(7) 
b.insert(15) 
b.insert(13) 
b.insert(17) 
b.insert(12)
b.insert(8)
b.insert(2) 
b.insert(14)

b.display()
b.delete(2)
b.display()


# The math and calculations in this problem are extremely well refined, reverse engineering this code would
# most likely lead to a longer run time and less efficient code.

# get the comments for this code from Suraj's github account