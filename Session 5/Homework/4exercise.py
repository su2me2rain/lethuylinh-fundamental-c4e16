farm = {0: 1}
for k in range(1,5):
    if k > 1:
        farm[k] = farm[k-1] + farm[k-2]
    else:
        farm[k] = 2*farm[k-1]
for k in farm:
    print('Month', k,':', farm[k], 'pair(s) of rabbit.')
