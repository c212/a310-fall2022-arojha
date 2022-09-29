class largestIn:

  def largestIn(tree):
    if tree.right == None:
      return tree.key
    else:
      return largestIn(tree.right)

class BST:
  def __init__(self, key, left = None, right = None):
    (self.key, self.left, self.right) = (key, left, right)

  def remove(self, value):
    if self.key == value:
      if self.left == None:
          return self.right
      else:
        a = largestIn(self.left)
        self.key = a
        self.left = self.left.remove(a) # tree works off the left side 
        return self
    elif self.key > value:
      self.left = self.left.remove(value)
      return self
    else:
      self.right = self.right.remove(value)
      return self

  def insert(self, node): 
    if self.key == node.key: return # this modifies the tree
    elif self.key < node.key:
      if self.right is None: self.right = node # inserting a node to the right if right sub tree is empty
      else: self.right.insert(node)
    else: # self.key > node.key
      if self.left is None: self.left = node # inserting a node to left if left sub tree is empty
      else: self.left.insert(node)

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
