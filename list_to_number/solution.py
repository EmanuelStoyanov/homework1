def list_to_number(digits):
	thenumber=0
	digits.reverse()
	for i in range(0,len(digits)):
		thenumber += digits[i] * 10 ** i
	return thenumber