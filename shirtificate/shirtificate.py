def main():
    name = input("Name: ")

    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()