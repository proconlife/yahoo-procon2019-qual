k,a,b=map(int,input().split())
if b-a <= 2:
    print(k+1)
elif k < a+1:
    print(k+1)
else:
    k-=(a+2-1)
    q,mod=divmod(k,2)
    print(mod+q*(b-a)+b)
