#3

liter=float(input('Enter Value : '))

if liter<90:
	print('Water bill = 0')
elif liter>=90 and liter<=150:
	print('Water bill with Rs 2 = ',liter*2)
elif liter>150 and liter<=250:
	print('Water bill with Rs 5 = ',liter*5)
elif liter>250:
	print('Water bill with Rs 10 = ',liter*10)