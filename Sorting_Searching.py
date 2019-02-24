
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
	c. Better if we have a partially sorted list. Wroks off the assumption that most of the list is sorted


4. mergeSort:
	a. Time Complexity = O(nlogn)
	b. Space Complexity = O(n)

"""


def bubbleSort(array):
	print("Length of array is: ",len(array))
	for i in range(len(array)-1):
		for j in range(i+1,len(array)):
			if array[i]>array[j]:
				temp = array[i]
				array[i]=array[j]
				array[j]=temp
			else:
				pass
	return array

def selectionSort(array):
	
	for i in range(len(array)-1,-1,-1):
		maxindex=i
		for j in range(i):
			if array[j]>array[maxindex]:
				maxindex = j
			else:
				pass
		temp = array[i]
		array[i] = array[maxindex]
		array[maxindex] = temp
	return array
		
def insertionSort(array):
	print ("Running insertion sort. Input array is: ",array)
	for i in range(1,len(array),1):
		pos = i
		while pos>0:
			if array[pos]<array[pos-1]:
				temp = array[pos]
				array[pos] = array[pos-1]
				array[pos-1] = temp
				pos -=1
			else:
				pass
	return array

def mergeSort(array):

	arraylen = len(array)

	if arraylen==1:
		return array

	mid = len(array)//2
	#print (mid)
	
	nums1 = array[0:mid]
	nums2 = array[mid:]


	mergeSort(nums1)
	mergeSort(nums2)

	i = len(nums1)
	j = len(nums2)

	k = l = m = 0

	while k<i and l<j:
		if nums1[k] < nums2[l]:
			array[m] = nums1[k]
			k+=1
			m+=1
		elif nums1[k] > nums2[l]:
			array[m] = nums2[l]
			l+=1
			m+=1
		else:
			print ("Cannot pass same element twice")

	

	while k<i:
		array[m] = nums1[k]
		m+=1
		k+=1

	while l<j:
		array[m] = nums2[l]
		m+=1
		l+=1

	return array


def binarySearch(array,target):

	if len(array)==1:
		return array[0]==target

	mid = len(array)//2
	if array[mid] == target:
		return True
		
	if array[mid] > target:
		return binarySearch(array[0:mid],target)
	else:
		return binarySearch(array[mid+1:],target)









if __name__ == "__main__":
	nums = [10,7,4,3,1]
	#print (bubbleSort(nums))
	#print (selectionSort(nums))
	#print (insertionSort(nums))
	#print (mergeSort(nums))
	print (binarySearch([1,3,4,7,10],10))