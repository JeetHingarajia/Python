#1.
Bsalary=int(input('Enter Basic Salary : '))
print(Bsalary)

TA=(Bsalary*4/100)
print(TA)

DA=(Bsalary*30/100)
print(DA)

HRA=(Bsalary*15/100)
print(HRA)

Gsalary=Bsalary+TA+DA+HRA
print('gross salary is',Gsalary)

Tax=(Bsalary*3/100)
print(Tax)

PF=(Bsalary*12/100)
print(PF)

Netsalary=Gsalary-Tax-PF
print('net salary is',Netsalary)