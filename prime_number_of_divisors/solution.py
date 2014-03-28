def prime_number_of_divisors(n):
	return is_prime(num_of_divisors(abs (n)))

def num_of_divisors(n):
	return len(divisors(n))

def divisors(n):
	if n != 1:
		arr = [1, n]
	else:
		return [1]
	for i in range(2,n):
		if n % i == 0:
			arr.append(i)
	return arr

def is_prime(n):
	return sum_of_divisors(abs(n)) == abs(n) + 1 

def sum_of_divisors(n):
	return sum (divisors(n))

def sevens_in_a_row(arr,n):
	for i in range(0,len(arr)):
		if arr[i] == 7:
			if sum(arr[i:i+n]) == 7 * n:
				return True
	return False
