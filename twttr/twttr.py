txt = input("Input: ").strip()

for i in txt:
    if i in ['a',"e","i","o","u","A","E","I","O","U"]:
        txt=txt.replace(i,"")
print(f"{txt}")