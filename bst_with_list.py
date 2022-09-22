class BST:
	def __init__(self,key):
		self.bst = [key]
		self.root=0
	def insert(self,key):
		l = len(self.bst)
		i = self.root
		while True:
			if self.bst[i]==key:
				break
			if self.bst[i]==None:
				self.bst[i]=key
				break
			elif self.bst[i]>key:
				i=2*i+1
			elif self.bst[i]<key:
				i=2*i+2
			if i>=l:
				self.bst+=[None]*(i+1-l)
	def print_array(self):
		print(self.bst)
		return

k = BST(10)
k.insert(15)
k.insert(13)
k.insert(5)
k.insert(1)
k.insert(6)
k.insert(19)
k.print_array()
