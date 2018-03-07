n = int(input('Input an integer number: '))
k = 1
result = 1
for i in range(n):
    result = result * k
    k = k + 1
print('The factorial of ',n,' consecutive integer numbers from 1 is ', result)
