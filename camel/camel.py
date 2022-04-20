x = input('camelCase:')
y = list(x.lower())
count=0
for i in x[1:]:
    if i.isupper():
        y.insert(x.index(i)+count,"_")
        count+=1
y="".join(y)
print(f'snake_case: {y}')