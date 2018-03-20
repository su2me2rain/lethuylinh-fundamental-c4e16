from random import choice
alphabet = {}
for i in list(map(chr, range(97,123))):
    alphabet[i] = 0

n = list(input('Enter a sentence: ').lower())
for i in range(len(n)):
    char = choice(n)
    if char in alphabet.keys():
        alphabet[char] += 1
        n.remove(char)

for k in alphabet.keys():
    if alphabet[k] != 0:
        print(k, ' ', alphabet[k])
