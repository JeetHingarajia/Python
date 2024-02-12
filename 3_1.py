#1.Get the basic salary from the employee and display the net salary by calculating the following conditions: Applicable TA 4%, DA 30%, HRA 15% on basic salary. Applicable 3% tax, 12% PF on basic salary.
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
