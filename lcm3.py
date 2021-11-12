x = int(input())
y = int(input())
l,i = 1,2
while(True):
    if(x%i==0 and y%i==0):
        x=x//i
        y=y//i
        l*=i
    elif(x<=i or y<=i):
            l=l*x*y
            break
    else:
        i+=1

print(l)
