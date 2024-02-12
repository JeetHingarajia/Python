#8. An online selling app wants to develop a application to calculate shipping charges on the purchase. Accept amount from the user and calculate the shipping charges. The shipping charges are as below:
#Shopping amount less than 1500 – The shipping charges is Rs. 100/-
#--Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
#--Please pay (amount+100)
#Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
#--Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
#--Please pay (amount+70)
#Shopping amount more than 3000 – Free shipping + 7% discount on amount
#--Type a message: You saved (amount*7/100)
#--Please pay (amount – discount)

amount=int(input('Enter amount : '))

if amount<1500:
	print('The shipping charges is Rs. 100/-')
	print('Please purchase (1500-amount) to avail shipping charge of Rs. 80/- Please pay : ',amount+100)

elif amount>1500 and amount<=3000:
	print('The shipping charges is Rs. 70/-')
	print(' Please purchase (3000-amount) to avail shipping charge of Rs. 50/- Please pay',amount+70)

elif amount>3000:
	print('Free shipping + 7% discount on amount')
	discount= amount - (amount*7/100) 
	print('You saved Please pay ',discount)
else:
	print('invalid')