b = int(input('How many B bacteria are there? '))
t = int(input('How much time in minutes will we wait? '))
time = t//2
n = b*(2**time)
print('After', t, 'minutes, we would have', n, 'bacteria.')
