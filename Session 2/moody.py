from random import randint
mood = randint(0, 100)
if mood <=30:
    print(':((')
elif mood <=60:
    print(':)')
else:
    print("Let's party")
