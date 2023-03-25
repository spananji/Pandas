#Write a Python program to find the factorial of a given number.

number = int(input('Enter the number:\n'))
fact = 1
for i in range(1,number+1):
    fact = fact * i
print(fact)


