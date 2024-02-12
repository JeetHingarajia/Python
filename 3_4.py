#4 A tuition class owner wants to make a simple application to allocate grade to the students on the basis of marks student have scored. Accept marks from the students.
	#Marks more than 90 – A1 grade
	#Marks 80 or less than or equal 90 – A grade
	#Marks 70 or less than or equal 80 – B1
	#arks 60 or less than or equal 70 – B
	#Marks 50 or less than or equal 60 – Can do Better!
	#Marks <50 – Need to work hard.

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