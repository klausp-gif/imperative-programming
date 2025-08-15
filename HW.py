a = int(input('give integer a: '))
b = int(input('give integer b: '))

if a == b:
    r = (a + b)**2
else:
    r = a + b
print(r)

x = 10
while x <= 37:
    print(x, end=' ')
    x += 3
print()

x = 998
while x >= 900:
    print(x, end=' ')
    x -= 2
print()

for x in range(20):
    if x % 2 == 0:
        v = 1
    else:
        v = -1
    print(v, end=' ')
print()

for x in range(60):
    if x % 3 == 2:
        v = 9
    else:
        v = 7
    print(v, end=' ')
print()

import random

x = 0

x += random.randint(1, 10) + random.randint(1, 10)

while x < 17:
    x += random.randint(1, 10)
if x > 21:
    x = 'bust'
print(x)

a = int(input('give integer a: '))
b = int(input('give integer b: '))

if a >= 100 and b <= 50:
    v = 1
else:
    v = 0
print(v)

if a >= 100 and b <= 50 or b >= 100 and a <= 50:
    v = 1
else:
    v = 0
print(v)

for _ in range(3, 6):
    p = 3 + (_ - 2) * 3