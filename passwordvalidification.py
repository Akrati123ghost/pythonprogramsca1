#question05:password validation
n = '15678'
while True:
    a = (input('Enter password:'))
    if a == n:
        print('correct password')
        break
    else:
        print('Try again')
