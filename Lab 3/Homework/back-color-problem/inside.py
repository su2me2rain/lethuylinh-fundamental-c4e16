def is_inside(point = [], rect = []):
    result = False
    if point[0] >= rect[0] and point[0] <= rect[0]+rect[2]:
        if point[1] >= rect[1] and point[1] <= rect[1]+rect[3]:
            result = True
    return result

ex1 = is_inside([100, 120], [140, 60, 100, 200])
ex2 = is_inside([200, 120], [140, 60, 100, 200])
if ex1 == False:
    if ex2 == True:
        print("Your function is correct")
    else:
        print("Ooops, bugs detected")
else:
    print("Ooops, bugs detected")
