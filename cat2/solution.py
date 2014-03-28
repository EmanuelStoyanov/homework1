import sys

def main():
    content = []    
    for i in range(1 ,len(sys.argv)):
        filename = sys.argv[i]
        f = open(filename,"r")
        content.append(f.read())
    f.close()
    print('\n'.join(content))
    return '\n'.join(content)

if __name__ == '__main__':
	main()