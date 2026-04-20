# my_math.py

def main():
	a = 10
	b = 7
	result1 = add(a, b)
	result2 = sub(a, b)

	print('Output from my_math.py:')
	print(f'{a} + {b} = {result1}')
	print(f'{a} - {b} = {result2}')

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

print(f'__name__ = {__name__}')

if __name__ == '__main__':
	main()