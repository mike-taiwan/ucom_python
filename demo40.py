import math
import random

print math.pi, math.log10(10), math.log10(2)
print math.sqrt(5)
for k in range(0, 100):
    print random.randint(10, 50),

print "\n"
stores = ['7-11', 'Fami', "OK", "Hi-Life"]
for k in range(0, 10):
    print random.choice(stores),

pokers = ['A', 'K', 'Q', 'J', '10', '9']
for l in range(0, 10):
    random.shuffle(pokers)
    print pokers