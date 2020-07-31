#!/usr/bin/python

import sys

# list generator expression
def main():
	f = [x for x in range(1,10)]
	print(f)

	# generatot expression, consume memory space 
	g = [x ** 2 for x in range(1,100)]
	print(f'sizeof(g)={sys.getsizeof(g)}')
	print(g)

	# generator object, consume time
	h = (x ** 2 for x in range(1, 100))
	print(f'sizeof(g)={sys.getsizeof(h)}')
	print(h)
	for v in h:
		print(v)
	
if __name__ == "__main__":
	main()
