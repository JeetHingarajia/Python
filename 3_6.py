#6. Accept two integer values in separate variable, display the small value and big value out of it.

a=int(input('Enter A: '))
b=int(input('Enter B: '))

if(a<b):
	print('A is smaller as A',a)
	print('B is bigger as B',b)
else:
	print('A is bigger as A',a)
	print('B is smaller as B',b)
