from LinkedList import LinkedList
from Element import Element

class Stack(object):
	def __init__(self,ll):
		self.ll = ll
	def push(self,new_element):
		self.ll.insert_first(new_element)

	def pop(self):
		temp = self.ll.head
		self.ll.delete_first()
		return temp.value

e1 = Element(3)
e2 = Element(4)
e3 = Element(5)
e4 = Element(6)
e5 = Element(7)
e6 = Element(8)
e7 = Element(1)
e8 = Element(2)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.insert(e6,3)

Demo_stack  = Stack(ll)

print "The stack was defined properly"

print "Push operation commenced"
Demo_stack.push(e8)
print Demo_stack.ll.head.value
print "Pop operation commenced"
print Demo_stack.pop()
print Demo_stack.ll.head.value
