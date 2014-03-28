def sum_of_digits2(n,sum):
	if n <= 0:
		return sum
	else:
		return sum_of_digits2(n//10,sum+n%10)

def sum_of_digits(n):
	return sum_of_digits2(abs(n),0)
