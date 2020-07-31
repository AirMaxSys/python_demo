#!/usr/bin/python

# python dictionary basic

def main():
	# create dict
	m_dict = {'bill' : 18, 'old dog' : 24, 'chicken' : 23, 'force gun' : 25}
	print(m_dict)

	print('bill' in m_dict)

	# 字典以键(索引)来访问
	print(m_dict['chicken'])

	m_dict['old dog'] = 30
	print(m_dict['old dog'])

	m_dict['hh'] = 'hello he'
	print(m_dict)

	# create dict by constructor
	dict2 = dict(one=1, two=2, three=3)
	print(f'dict2:{dict2}')

	# create dict by comprehensions
	dict3 = {num: num ** 2 for num in range(1, 10)}
	print(f'dict3:{dict3}')

	# traverse dict by key
	print('Traverse dict2:')
	for key in dict2:
		print(f'{key}:{dict2[key]}')

if __name__ == "__main__":
	main()
