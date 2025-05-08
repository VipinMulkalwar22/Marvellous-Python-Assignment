def Add(value1,value2):
    return value1 + value2

def main():
    print("Enter the first no :")
    no1 = int(input())
    print("Enter the second no :")
    no2 = int(input())

    sum = Add(no1,no2)

    print("Addition is :",sum)

if __name__ == "__main__":
    main()