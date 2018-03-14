menu = ['champion', 'estimation', 'wonderful']
from random import choice
import random

word = choice(menu)
print(word)
characters = list(word)

for i in range(len(characters)):
    random_char = choice(characters)
    print(random_char, end=' ')
    characters.remove(random_char)
print()
answer = False
while answer == False:
    guess = input('Your guess: ')
    if guess == word:
        answer = True
        print('Correct!')
    else:
        print('Incorrect. Try again: ')
