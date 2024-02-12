#2Get the marks of 5 subjects at the command line and display the total of marks, and percentage.
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
d=int(sys.argv[4])
e=int(sys.argv[5])

sum=a+b+c+d+e

print('The sum is : ',sum)

per=sum*100/500
print('Percentage is : ',per)