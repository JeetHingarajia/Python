#7) The distance between two cities is input through keyboard. Write a program to convert and print this distance in feet, meter, inch and centimeter. 

city=int(input('Enter The distance between two cities :'))
print(city)

print('convert into feet',city*3280)
print('convert into meter',city*1000)
print('convert into inch',city*39370)
print('convert into centemeter',city*100000)

Output:-
Enter The distance between two cities :5
5
convert into feet 16400
convert into meter 5000
convert into inch 196850
convert into centemeter 500000
