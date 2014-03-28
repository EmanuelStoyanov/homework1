def number_to_list(n):
	return number_to_list2(n,[])

def number_to_list2(n,arr):
	if n<=0:
		arr.reverse()
		return arr
	else:
		arr.append(n%10)
		return number_to_list2(n//10,arr)
