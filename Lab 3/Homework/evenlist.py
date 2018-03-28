def get_even_list(l):
    k = len(l)
    count = 0
    for i in range(k):
        if l[i-count] % 2 != 0:
            l.remove(l[i-count])
            count += 1
    return l

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
