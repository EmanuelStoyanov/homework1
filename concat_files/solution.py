import sys

def main():
	filename = "MEGATRON.txt"
	file1 = open(filename,"a")
	contents = []

	for i in range(1 ,len(sys.argv)):
		filename = sys.argv[i]
		file2 = open(filename,"r")
		content=file2.read()
		contents.append(content)
	file1.write("\n".join(contents))	
	file2.close()	
	file1.close()
	return "\n".join(contents)

if __name__ == '__main__':
	main()
