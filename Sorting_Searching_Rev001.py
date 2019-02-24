
"""
1. bubbleSort:
	a. Time Complexity = O(n^2)
	b. Space Complexity = O(1)

2. selectionSort:
	a. Time Complexity = O(n^2)
	b. Space Complexity = O(1) 
	c. Better than bubble sort everytime - AS it follows the same idea, but waits until the end of the loop to identify the max element and does one swap

3. insertionSort:
	a. Time COmplexity = O(n^2)
	b. Space Complexity = O(1)
	c. Better if we have a partially sorted list. Works off the assumption that most of the list is sorted


4. mergeSort:
	a. Time Complexity = O(nlogn)
	b. Space Complexity = O(n)

"""
import pdb

def bubbleSort(nums):
	for i in range(len(nums)-1):
		for j in range(i+1,len(nums),1):
			if nums[i]>nums[j]:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp
	return nums


def selectionSort(nums):
	for i in range(len(nums)-1,-1,-1):
		maxpos = i
		for j in range(i):
			if nums[j] > nums[maxpos]:
				maxpos = j
		temp = nums[i]
		nums[i] = nums[maxpos]
		nums[maxpos] = temp
	return nums

def insertionSort(nums):
	for i in range(1,len(nums)):
		pos = i
		while pos > 0 :
			if nums[pos] < nums[pos-1]:
				temp = nums[pos-1]
				nums[pos-1]=nums[pos]
				nums[pos] = temp
				pos-=1
	return nums

def mergeSort(nums):
	length = len(nums)

	if length ==1:
		return nums
	
	mid = length//2

	nums1 = nums[0:mid]
	nums2 = nums[mid:]

	#pdb.set_trace()
	# Check

	mergeSort(nums1)
	mergeSort(nums2)



	i=j=k=0

	len1 = len(nums1)
	len2 = len(nums2)

	numsarray = []

	while i<len1 and j<len2:
		if nums1[i]<nums2[j]:
			nums[k] = nums1[i]
			i += 1
			k += 1
		else:
			nums[k] = nums2[j]
			j += 1
			k += 1

	#pdb.set_trace()
	
	while i<len1:
		nums[k] = nums1[i]
		i+=1
		k+=1

	while j<len2:
		nums[k] = nums2[j]
		j+=1
		k+=1
	

	return nums




#print (bubbleSort([9,8,7,5,3,1]))
#print (selectionSort([9,8,7,5,3,1]))
#print (insertionSort([9,8,7,5,3,1]))
print (mergeSort([9,8,7,5,3,1]))

