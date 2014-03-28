def is_number_balanced(n):
	arr = toArr(n,[])
	left = arr[0:len(arr)//2]
	if(len(arr) % 2 == 0):
		right = arr[len(arr)//2:len(arr)]
	else:
		right = arr[len(arr)//2 + 1:len(arr)]
	return sum(left) == sum(right)

def toArr(n,arr):
	if n<=0:
		arr.reverse()
		return arr
	else:
		arr.append(n%10)
		return toArr(n//10,arr)