#3Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water is being delivered by the Corporation on per litre charges as below:
	#Upto 90 litres – Rs. 0/ltr
	#Upto 150 litres – Rs. 2/ltr
	#Upto 250 litres – Rs. 5/ltr
	#More than 250 – Rs. 10/ltr

liter=float(input('Enter Value : '))

if liter<90:
	print('Water bill = 0')
elif liter>=90 and liter<=150:
	print('Water bill with Rs 2 = ',liter*2)
elif liter>150 and liter<=250:
	print('Water bill with Rs 5 = ',liter*5)
elif liter>250:
	print('Water bill with Rs 10 = ',liter*10)