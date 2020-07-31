#!/usr/bin/python

# python set
# set is unordered

def main():
	# create 4 set
	set1 = {1,2,3,3,4}
	print(set1) # {1, 2, 3, 4}

	set2 = set(range(1,10)) # use constructor
	print(set2)

	set3 = set((1,2,3,4,4))
	print(set3)

	set4 = {num for num in range(1,10) if num % 2 == 0}
	print(set4)

	# push and pop
	set1.add(100)
	print(f'set1 add(100):{set1}')

	set1.update([101, 102]) # add list, set, dictionary, string, etc.
	print(f'set1 update([1,2]):{set1}')

	set1.discard(3) # remove item form set if it is present
	print(f'set1 discard(3):{set1}')

	try:
		set1.remove(1000) # remove item form set if it not in, raise KeyError exception 
	except(KeyError):
		print('1000 not in set1')

	v = 1
	if v in set1:
		set1.remove(v)
	print(f'set1 remove(1):{set1}')

	# pop() returns a random element from the set. 
	# the set is updated and will not contain the element (which is returned).
	# If the set is empty, TypeError exception is raised.
	try:
		set1.pop()
	except(KeyError):
		print('set is empty')
	print(f'after set1 pop:{set1}')

	# set calculations 
	# union, intersection and difference operation(operator reload)
	print(f'set1 union set2:{set1 | set2}')
	print(f'set1 intersection set2:{set1 & set2}')
	print(f'set1 difference set2:{set1 - set2}')
	# 判断子集和超集(subset or superset)
	msubset = {1,2}
	msuperset = {1,2,3}
	print(f'msubset is subset:{msubset<=msuperset}')
	print(f'msuperset is superset:{msuperset.issuperset(msubset)}') # use set method

if __name__ == "__main__":
	main()
