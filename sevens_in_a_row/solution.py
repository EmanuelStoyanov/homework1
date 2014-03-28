def sevens_in_a_row(arr,n):
	for i in range(0,len(arr)-n+1):
		if arr[i] == 7:
			if sum(arr[i:i+n]) == 7 * n:
				return True
	return False

"""
1 7 7 7 5 6 7
0 1 2 3 4
1 7 7 7 5"""