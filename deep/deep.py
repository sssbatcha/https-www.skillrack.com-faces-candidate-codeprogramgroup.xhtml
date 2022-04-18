txt = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()
if txt == "42" or txt == "forty-two" or txt == "forty two":
    print("Yes")
else:
    print("No")