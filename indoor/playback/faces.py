def convert(x):
    y=x.split(" ")
    z=""
    for i in range(1,len(y),2):
        if y[i]==":)":
            z+=y[i-1]+" 🙂 "
        elif y[i]==":(":
            z+=y[i-1]+" 🙁 "
    print(z)
def main():
    x=input()
    convert(x)
    #convert("Hello :)")

main()
