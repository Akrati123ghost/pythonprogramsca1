#question
import time
n = int(input('Enter the number'))
print('Counter start')
while n:
    print(n)
    n -= 1
    time.sleep(0.5)
else:
    print('Counter stop')
