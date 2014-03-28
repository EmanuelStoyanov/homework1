import sys

def main():
	command = sys.argv[1]
	filename = sys.argv[2]
	file = open(filename,"r")
	content=file.read()
	if command == "chars":
		print(len(content))
		return len(content)
	if command == "words":
		print(len(content.split(" ")))
		return len(content.split(" "))
	if command == "lines":
		print(len(content.split("\n")))
		return len(content.split("\n"))
	file.close()

if __name__ == '__main__':
	main()