def nth_fibonacci(n):
	arr = [1,1]
	for i in range(2,n+1):
		newfib = arr[i-1] + arr[i-2]
		arr.append(newfib)
	return arr[n-1]

