a=int(input('please input amount of marks: '))
if a>=90:
    g=(10)
elif a>=70:
    g=(9)
else:
    g=(8)
print('Your grade is ',g)

n=int(input('please give n:'))
if n<=0:
    print('n must be greater than 0')
else:
    result=1
    while n>1:
        result*=n
        n-=1
print(result)
