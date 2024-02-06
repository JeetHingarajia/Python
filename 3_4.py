#4

mark=int(input('Enter Student Mark : '))

if mark>90:
	print('A1 grade')
elif mark>80 and mark<=90:
	print('A grade')
elif mark>70 and mark<=80:
	print('B1 grade')
elif mark>60 and mark<=70:
	print('B grade')
elif mark>60 and mark<=50:
	print('You can do better')
else:
	print('need to work hard')