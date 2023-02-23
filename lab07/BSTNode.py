

class BstNode:
    def __init__(self, key):
        self.key = key # aka value
        self.right = None
        self.left = None
    def valid(self,node):
        if node==None:
            return 0
        else:
            return 1
    def insert_helper(self,node):
        if self.key>node.key:
            if self.valid(self.left)==1:
                self.left.insert_helper(node)
            else:
                self.left = node
        else:
            if self.valid(self.right)==1:
                self.right.insert_helper(node)
            else:
                self.right=node
    def insert(self, value):
        a = BstNode(value)
        self.insert_helper(a)
    def find(self,value):
        if self.key==value:
            print("Value found ", value)
        elif self.key>value:
            if self.valid(self.left)==1:
                self.left.find(value)
            else:
                print("value not found")
        else:
            if self.valid(self.right)==1:
                self.right.find(value)
            else:
                print("value not found")
    def checker(self,node):
        # smallest value on the right
        # just check smallest 
        if node.left==None and node.right==None:
            return "leaf"
        elif node.right==None:
            return "left"
        else:
            return "both"
        
    def smallest_value(self,node):
        if node.left==None:
            return node
        else:
           self.smallest_value(node.left)

    def del_helper(self,node,value):
        if self.valid(node)==0:
            print("does not exist")
        else:
            node.delete(value)
    
    def delete(self,value):
        # Smallest value to the right
        if self.key==value:
            if self.checker(self)=="leaf":
                self=None
            elif self.checker(self)=="left":
                self = self.left
            else:
                temp  = self.smallest_value(self.right)
                self = temp
                self.right.delete(temp.key)
        elif self.key>value:
            #if self.valid(self.left)==0:
            #    print("does not exist")
            #else:
            #    self.left.delete(value)
            self.del_helper(self.left,value)
        else:
            self.del_helper(self.right,value)
            
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
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
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
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

