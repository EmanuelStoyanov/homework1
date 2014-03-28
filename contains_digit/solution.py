def toArr(n,arr):
	if n<=0:
		arr.reverse()
		return arr
	else:
		arr.append(n%10)
		return toArr(n//10,arr)

def contains_digit(number,digit):
	return member(toArr(number,[]),digit)

def member(arr,elem):
	for element in arr:
		if elem == element:
			return True
	return False

