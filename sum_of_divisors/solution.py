def sum_of_divisors(n):
	return sum (divisors(n))

def divisors(n):
	if n != 1:
		arr = [1, n]
	else:
		return [1]
	for i in range(2,n):
		if n % i == 0:
			arr.append(i)
	return arr