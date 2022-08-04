import random

s = random.randint(100, 1000)
def massiv(s):
    a = str(s)
    clues = []
    for digits in a:
        clues.append(digits)
    print(clues)