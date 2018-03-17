numbers = [1, 2, 3, 4,3,6,7,8,4,1,2,1]

#usingcount()
n = int(input('Enter a number: '))
k = numbers.count(n)
print(n, 'appears', k, 'time(s) in my list.')

#notusingcount()
count = {}
for i in numbers:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1
n = int(input('Enter a number: '))
print(n, 'appears', count[n], 'time(s) in my list.')
