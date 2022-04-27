from fractions import Fraction as frac

def func():

    try:
        a=input()
        b=(frac(a).numerator)
        d=(frac(a).denominator)
        c=(b/d)
        if(c==0.0):
            print('E')
            func()
        elif(0.0<c<=0.25):
            print('25%')
            func()
        elif(0.26<=c<=0.50):
           print('50%')
           func()
        elif(0.50<c<=0.75):
            print('75%')
            func()
        elif(0.75<c<=1.0):
            print('F')
            func()
        elif (c>1.0):
            print('not valid')
            func()
    except ZeroDivisionError:
        print("cannot divide by zero")
        func()
    except ValueError:
        print("value error")
        func()

func()
