#question 2 Factorial calculation:Write a program that calculates the factorial of a given positive integer using a while loop.

a = int(input("Enter a positive integer:"))
s = 1
while a:
    s = s*a
    a = a-1
print(s)
