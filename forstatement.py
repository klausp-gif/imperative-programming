n=int(input('please give n: '))

if n<=0:
    print('not a positive value::', n)
else:
    result=1
    for v in range(2, n+1):
        result *=v
    
    print(result)