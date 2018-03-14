n = int(input('Enter a number: '))
count = 0
while True:
    n = n//10
    count += 1
    if n==0:
        break
print('The number of digits is: ', count)
