name = input('Enter your fullname: ').lower().strip().split(' ')
# print(namelist)
for k in name:
    for j in name:
        if j == '':
            name.remove(j)

print('Updated: ',end='')
for i in range(len(name)):
    word=list(name[i])
    word[0]=word[0].upper()
    print(*word ,sep='', end=' ')
print()
