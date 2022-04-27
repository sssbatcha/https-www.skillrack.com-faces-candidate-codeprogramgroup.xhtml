
try:

    z=int(input())/int(input())
    if(0.0<z<0.24):
        print('E')
    if(0.25<z<=0.50):
        print('50%')
    if(0.51<z<=0.75):
        print('75%')
    if(0.76<z<1.0):
        print('E')
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("value error")




