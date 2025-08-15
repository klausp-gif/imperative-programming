v = 9
while v <= 65:
    print(v, end=' ')
    v += 4
print()

v = 3
for _ in range(13):
    print(v, end=' ')
    v *=2
print()

for _ in range(1, 41):
    if _ % 4 == 0:
        x = -1
    else:
        x = _
    print(x, end=' ')
print()

low = 0
high = 0
for n in range(51):
    v = n*(n - 30)*(n - 50)
    if v > high:
        high = v
    if v < low:
        low = v

print('highest value: ',high)
print('lowest value: ',low)

s = int(input('please give the value of s: '))

n = 1
found = False

while found == False:
    if n* (n + 1) / 2 > s:
        found = True
    else:
        n += 1

print(n)