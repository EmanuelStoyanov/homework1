def count_words(arr):
	dict = {}
	for word in arr:
		dict[word] = countmember(word,arr) 
	print(dict)
	return dict

def countmember(word,arr):
	count = 0
	for one in arr:
		if one == word:
			count+=1
	return count
