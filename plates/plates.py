def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = (len(s)>=2 and len(s)<=6 and s[2]!="0") and s.isalnum() and s[0].isnumeric() == False
    return x



main()