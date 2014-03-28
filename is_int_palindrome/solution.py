def is_int_palindrome(n):
	return symetric (toArr(n,[]))

def toArr(n,arr):
	if n<=0:
		arr.reverse()
		return arr
	else:
		arr.append(n%10)
		return toArr(n//10,arr)

def symetric(arr):
	n = len(arr)
	for i in range(0,n//2):
		if arr[i] != arr[n-i-1]:
			return False
	return True
