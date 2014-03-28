import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    file = open(filename, "w")
    content = []
    for i in range(0, n):
        content.append(str(randint(1, 1000)))
    file.write(" ".join(content))
    file.close()


if __name__ == '__main__':
	main()