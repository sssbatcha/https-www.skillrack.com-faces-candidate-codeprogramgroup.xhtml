expr = list(map(str,input("Expression: ").split()))
#print(expr)
no1 = int(expr[0])
no2 = int(expr[2])


#print(no1,no2)
if expr[1] == "+":
    no3 = no1 + no2
    print("%.1f"%no3)
elif expr[1] == "-":
    no3 = no1 - no2
    print("%.1f"%no3)
elif expr[1] == "*":
    no3 = no1 * no2
    print("%.1f"%no3)
elif expr[1] == "/":
    no3 = no1 / no2
    print("%.1f"%no3)