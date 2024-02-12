#5. Income Tax department wants to make an application that calculates tax on the basis of the income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid. The tax slab is as below:
	#Income up to 8 lakhs – No tax
	#Income more than 8 lakh and less than 10 lakhs – 15% of income
	#Income more than 10 lakhs and less than 20 lakhs – 20% of income
	#Income more than 20 lakhs – 30% of income

Income=int(input('Enter Income : '))

if Income<800000:
	print('No tax')
elif Income>800000 and Income<=1000000:
	print('15 % TAX ON 	INCOME',Income*15/100)
elif Income>1000000 and Income<=2000000:
	print('20 % TAX ON 	INCOME',Income*20/100)
elif Income>2000000:
	print('30 % TAX ON 	INCOME',Income*30/100)
else:
	print('invalid')