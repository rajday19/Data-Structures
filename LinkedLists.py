"""
This will have the linked list implementation

    List() creates a new list that is empty. It needs no parameters and returns an empty list.
    add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list. Item will only be the value
    remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
    search(item) searches for the item in the list. It needs the item and returns a boolean value.
    isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
    size() returns the number of items in the list. It needs no parameters and returns an integer.
    append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
    insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
    pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.


"""
import unittest

class LLNode():
	def __init__(self,headval,nextNode=None):
		self.headval=headval
		self.nextNode=nextNode

	def getData(self):
		return self.headval

	def setData(self,val):
		self.headval = val

	def getnextNode(self):
		return self.nextNode

	def setnextNode(self,newnextNode):
		self.nextNode = newnextNode

class LL():
	def __init__(self,head=None):
		self.head = head
		if self.head:
			self.len = 1
		else:
			self.len=0

	def add(self,item):
		if self.head:
			current = self.head
			while current.nextNode:
				current = current.nextNode
			current.nextNode=LLNode(item)
			self.len+=1
		else:
			self.head = LLNode(item)
			self.len+=1

	def remove(self,item):
		if self.head:
			current = self.head
			if current.headval==item:
				if current.nextNode:
					self.head = current.nextNode
					self.len-=1
				else:
					self.head=None
					self.head.nextNode=None
					self.head-=1

			while current.nextNode.headval!=item and current.nextNode.headval!= None:
				current = current.nextNode

			if current.nextNode.headval == item:
				current.nextNode = current.nextNode.nextNode
				self.len-=1
			else:
				return None
		else:
			return None

	def search(self,item):
		if self.head:
			current = self.head
			while current and current.headval!=item:
				current = current.nextNode

			if current:
				return True
			else:
				return False

		return False

	def isEmpty(self):
		return self.head==None

	def size(self):
		return self.len

	def append(self,item):
		if self.head:
			current = self.head
			while current.nextNode:
				current=current.nextNode
			current.nextNode = LLNode(item)
			self.len+=1

		else:
			self.head = LLNode(item)
			self.len+=1

	def index(self,item):
		index = 0
		current = self.head
		while current and current.headval!=item:
			current=current.nextNode
			index+=1
		if current:
			return index
		else:
			return None

	def insert(self,item,pos):
		index=0
		if pos==0:
			if self.head:
				temp = self.head
				self.head = LLNode(item)
				self.head.nextNode=temp
				self.len+=1
			else:
				self.head = LLNode(item)
				self.len+=1

		current = self.head
		while index<pos-1:
			current = current.nextNode
			index+=1
		temp = current.nextNode
		current.nextNode = LLNode(item)
		current.nextNode.nextNode = temp
		self.len+=1

	def pop(self):
		current = self.head

		while current.nextNode:
			current = current.nextNode

		temp  =current.headval
		current.headval=None
		self.len-=1

		return temp


class LLTest(unittest.TestCase):

	def test_LL_pop(self):
		Check = LL()
		Check.add(5)
		Check.add(7)
		self.assertEqual(Check.pop(),7)
	
	def test_search(self):
		Check  =LL()
		Check.add(5)
		Check.add(6)
		Check.add(7)
		self.assertTrue(Check.search(7))

if __name__ == "__main__":

	unittest.main()

"""
	print ("Checking main")
	Check = LL()
	print (Check.isEmpty())
	Check.add(5)
	Check.add(7)
	print (Check.size())
	Check.append(10)
	Check.insert(4,2)
	print (Check.size())
	print (Check.pop())
	print (Check.size())
"""