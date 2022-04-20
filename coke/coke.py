amount_due = 50
while amount_due > 0:
    insert_coin = int(input("Insert coin: "))
    
    if insert_coin in [25,10,5]:
        amount_due-= insert_coin
        if amount_due>0:
            print(f"Amount Due: {amount_due}")
        elif amount_due < 0:
            change_owed = abs(amount_due)
        else:
            change_owed = 0
    else:
        print(f"Amount Due: {amount_due}")
        continue

print(f"Change Owed: {change_owed}")