def main():
    time = input("What time is it?").strip()
    x = time.split(":")
    hours = int(x[0])
    mins = convert(int(x[1]))
    hours=hours+mins
    #breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
    if hours >= 7.00 and hours<=8.00:
        print("breakfast time")
    elif hours >= 12.00 and hours<=13.00:
        print("lunch time")
    elif hours >= 18.00 and hours<=19.00:
        print("dinner time")

def convert(time):
    if time>=0 and time<=60:
        mins=(time/60)
        mins=round(mins,2)
        #print(mins)
        return mins

if __name__ == "__main__":
    main()