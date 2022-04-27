
try:

    z=str(input())
    a=int(z[0])
    b=int(z[2])
    c=a/b

    if(0.0<=c<=0.25):
        print('E')
    if(0.26<=c<=0.50):
        print('50%')
    if(0.50<c<=0.75):
        print('75%')
    if(0.75<c<=1.0):
        print('E')
    if (c>1.0):
        print('not valid')
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("value error")