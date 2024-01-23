#accept one integer value from user convert it to binary,octal,hexadecimal.

a=int(input('enter value :'))

binary=bin(a)
print(binary)

octal=oct(a)
print(octal)

hexdec=hex(a)
print(hexdec)

Output:-
enter value :2
0b10
0o2
0x2