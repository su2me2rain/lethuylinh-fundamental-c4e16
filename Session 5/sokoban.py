maps = {
    'x': 5,
    'y': 5,
}

player = {
    'x': 0,
    'y':4
}

boxes = [
    {'x': 1, 'y': 1},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': 3}
]

destination = [
    {'x': 2, 'y': 1},
    {'x': 3, 'y': 2},
    {'x': 4, 'y': 3}
]
#printmap
while True:
    for y in range(maps['y']):
        for x in range(maps['x']):
            box_is_here = False
            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    box_is_here = True
                    break

            destination_is_here = False
            for d in destination:
                if d['x'] == x and d['y'] == y:
                    destination_is_here = True
                    break
            player_is_here = False
            if x == player['x'] and y == player['y']:
                player_is_here = True

            if box_is_here:
                print('B  ', end='')
            elif player_is_here:
                print('P  ', end='')
            elif destination_is_here:
                print('D  ', end='')
            else:
                print('_  ', end='')
        print()

    #checkresult
    #k = 0
    #for box in boxes:
    #     for d in destination:
    #         if box['x'] == d['x'] and box['y'] == d['y']:
    #             k += 1
    # if k == len(destination):
    #     print('You win')
    #     break

    is_win = True
    for box in boxes:
        if box not in destination:
            in_win = False

    #Moveperson
    dx = 0
    dy = 0
    move = input('Your move? ').upper()
    if move == 'W':
        print('Up')
        dy =-1
    elif move == 'S':
        print('Down')
        dy =1
    elif move == 'A':
        print('Left')
        dx =-1
    elif move == 'D':
        print('Right')
        dx =1
    if 0 <= player['x'] + dx <= maps['x']-1 and 0 <= player['y'] + dy <= maps['y']-1:
        player['x'] += dx
        player['y'] += dy

    #moveblock
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            if 0 <= box['x'] + dx <= maps['x']-1 and 0 <= box['y'] + dy <= maps['y']-1:
                box['x'] += dx
                box['y'] += dy
            else:
                player['x'] -= dx
                player['y'] -= dy
