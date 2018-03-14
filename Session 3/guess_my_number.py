from random import randint
n = randint(0, 100)
count = 0
while True:
    guess = int(input("Can you guess my number? "))
    if guess == n:
        print('Correct. You are smart.')
        break
    elif guess<n:
        print('too small')
    else:
        print('too large')
    count += 1
    if count == 9:
        print("game over")
        break
