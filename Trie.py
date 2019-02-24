import re

"""
1. This will implement a trie data structure with two methods - add(word) and search(word)
2. It will have to take care of regular expressions in words as well
3. The Trie is assumed to be a trie constructed for the purposes of storing a word sequence alone
"""

class TrieNode():
	def __init__(self,val,children=None):
		self.val = val
		self.children = []
		self.childrenvals = []
		self.mappingvals = {}
		self.updatemappingvals()

	def inChildren(self,val):
		# Takes a raw value and checks to see if that is a part of the children
		if val in self.childrenvals:
			return True
		else:
			return False

	def addChild(self,val):
		# Takes in a raw value and adds it into the children list if it is not already present
		if not self.inChildren(val):
			self.children.append(TrieNode(val))
			self.childrenvals.append(val)
			self.updatemappingvals()
		else:
			print ("The value is already present. No need to add again")

	def updatemappingvals(self):
		self.mappingvals = dict(zip(self.childrenvals,self.children))


class Trie():
	def __init__(self,left=None,right=None):
		# Instatntiating a Trie with root node which does not contain any value. The class does not give access to the user to set a root node value in the constructor
		self.root = TrieNode(None)
		#self.root.val = None
		self.left = left
		self.right = right

	def addWord(self,word):
		# This method will take inputs as raw strings and convert them to trie nodes before adding into data structure
		current = self.root
		for i,v in enumerate(word):
			#print (v)
			#print (current.val)
			if current.inChildren(v):
				current = current.mappingvals[v]
				pass
			else:
				#print ('Pass is: ',i)
				current.addChild(v)
				current = current.mappingvals[v]

	def search(self,word):
		# This method will take inputs as raw strings and check whether that word is in the data structure
		current = self.root
		
		for i in word:
			if current.inChildren(i):
				current = current.mappingvals[i]
			else:
				return False
		return True
	

	def printTrie(self,node):
		current = node
		if current:
			#print ("Number of children for the node ", current.val,len(current.children))
			for i in current.children:
				print ("Will start printing values of node",i.val)
				print (i.childrenvals)
				self.printTrie(i)
	


if __name__ == '__main__':
	DS = Trie()
	DS.addWord('bad')
	DS.addWord('dad')
	DS.addWord('mad')
	#DS.printTrie(DS.root)
	print (DS.search('cable'))
	print (DS.search('mad'))
