from Element import Element

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def __str__(self):
    	return "Linked List Created"

    def append(self,new_element):
    	current = self.head
    	if self.head:
    		while current.next:
    			current = current.next
    		current.next = new_element
    	else:
    		self.head = new_element
    def get_position(self, position):
    	current = self.head
    	i = 0
    	while i<position:
    		#print current.value
    		current = current.next
    		i += 1
    	return current.value
    def insert (self,new_element,position):
    	current = self.head
    	i = 0
    	while i<position-1:
    		current = current.next
    		i += 1
    	temp = current.next
    	current.next = new_element
    	new_element.next = temp
    def delete(self, element):
    	current = self.head
    	while current.value!=element:
    		current = current.next
    	current.value = None
    



e1 = Element(3)
e2 = Element(4)
e3 = Element(5)
e4 = Element(6)
e5 = Element(7)
e6 = Element(8)


ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.insert(e6,3)

#print ll.head.value
#print ll.head.next.value
#print ll.head.next.next.value
#print ll.head.next.next.next.value
ll.delete(8)
print ll.get_position(3)