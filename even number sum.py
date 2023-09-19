#Question4:Sum of even no.
a = int(input("Enter a number:"))
s = 0
while a:
    if a%2 == 0:
        s = s+1
    a = a-1
print(s)
