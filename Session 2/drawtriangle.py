side = int(input('Input the side: '))
# Triangle left
for i in range(side):
    for i in range(i+1):
        print('* ', end=(''))
    print()

# Triangle right
# for i in range(side):
#     for j in range(side-i):
#         print('  ', end=(''))
#     for h in range(i+1):
#         print('* ', end=(''))
#     print()

# print Z
# for i in range(side):
#     if i==0 or i==side-1:
#         for j in range(side):
#             print("* ", end=(''))
#         print()
#     else:
#         for j in range(side-i-1):
#             print('  ', end=(''))
#         print('* ', end=(''))
#         print()
