def count_vowels(str):
	vowels = "aeiouyAEIOUY"
	count = 0
	for letter in str:
		if member(vowels,letter):
			count+=1
	return count

def member(arr,elem):
	for element in arr:
		if elem == element:
			return True
	return False

