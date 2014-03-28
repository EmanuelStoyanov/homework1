import sys


def main():
    result = 0
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    result = sum(map(int, content.split(" ")))
    print(result)
    return result
    file.close()

if __name__ == '__main__':
	main()