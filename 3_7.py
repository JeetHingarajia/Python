#7. Accept marks from 4 students, display which mark is highest among all.

s1=int(input('Enter Student1 Mark : '))
s2=int(input('Enter Student2 Mark : '))
s3=int(input('Enter Student3 Mark : '))
s4=int(input('Enter Student4 Mark : '))

if s1>s2 and s1>s3 and s1>s4:
	print('S1 is highest')
elif s2>s1 and s2>s3 and s2>s4:
	print('S2 is highest')
elif s3>s1 and s3>s2 and s3>s4:
	print('S3 is highest')
elif s4>s1 and s4>s2 and s4>s3:
	print('S4 is highest')
