x=str(input())
if x==('3/4'):
    print('75%')
elif x==('1/4'):
    print('25%')
elif x==('4/4'):
    print('F')
elif x==('0/4'):
    print('E')



try:
    x==4/0
except:
    print("Can't divide with zero")