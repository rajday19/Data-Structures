"""
1. Problem 1

Print a string in reverse order

"""

def reverse(word,s):
	if len(word)==0:
		#print ("Exit condition hit")
		#print ("Reversed string is: ",s)
		return s
	else:
		s = s + word[-1]
		#print (s)
		#print (word[:-1])
		return reverse(word[:-1],s)


print (reverse("check",""))
