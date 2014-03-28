def prime_factorization(n):
	return prime_factorization2(n,[])




def prime_factorization2(n,listofprimes):
	if is_prime(n):
		listofprimes.append(n)
		listofprimes.sort()
		return makeprint(listofprimes,[])
	else:
		for number in range(2,n):
			if n % number == 0:
				listofprimes.append(number)
				return prime_factorization2(n//number,listofprimes)


def makeprint(arr,tuples):
	count = 1
	if len(arr) == 1:
		tuples.append((arr[0],1))
		return tuples
	else:
		for i in range(1,len(arr)):
			if(i == len(arr) - 1) and arr[0]==arr[i]:
				tuples.append((arr[0],count+1))
				return tuples
			elif arr[0]==arr[i]:
				count+=1
			else:
				tuples.append((arr[0],count))
				return makeprint(arr[i:],tuples)
	


def is_prime(n):
	return sum_of_divisors(abs(n)) == abs(n) + 1 

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
