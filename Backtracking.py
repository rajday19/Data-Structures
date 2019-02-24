"""

Generate all power sets given a list of numbers

"""
x  =[1,2,3]
word = "ripe"


def powerset(nums):
	result = [[]]
	for i in nums:
		newsubsets = [subset + [i] for subset in result]
		result.extend(newsubsets)
	return result

#print (powerset(x))

def get_permutations(string):
	# Base case
	if len(string) <= 1:
		return set([string])

	all_chars_except_last = string[:-1]
	last_char = string[-1]

	# Recursive call: get all possible permutations for all chars except last
	permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

	print ("\nPermutations are: ", permutations_of_all_chars_except_last)
	print ("\nAll characters except last: ",all_chars_except_last)

	# Put the last char in all possible positions for each of
	# the above permutations
	permutations = set()
	
	for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
		for position in range(len(all_chars_except_last) + 1):
			permutation = (permutation_of_all_chars_except_last[:position]+ last_char+ permutation_of_all_chars_except_last[position:])
			permutations.add(permutation)
	
	return permutations


def fib(n):
	mem = {}
	if n==0:
		mem[n] = 0
		return 0
	elif n==1:
		mem[n] = 1
		return 1
	else:
		x = mem.get(n,fib(n-1)+fib(n-2))
		mem[n] = x
		return x


def getperm(nums):
	
	if len(nums) <=1:
		return [nums]

	All_except_last = nums[:-1]
	Last_num = nums[-1]

	Perm_all_except_last = getperm(All_except_last)

	#print ("\nPermuations of all except last: ",Perm_all_except_last)
	#print ("\nAll except last: ",All_except_last)
	#print ("\nLast number is: ",Last_num)

	permutations = []

	for perm in Perm_all_except_last:
		for pos in range(len(All_except_last)+1):
			#print ("Perm is: ",perm)
			x = perm[:]
			x.insert(pos,Last_num)
			permutations.append(x)
		#print  ("\nPermuations are: ",permutations)

	return permutations


print (getperm([1,2,3,4]))