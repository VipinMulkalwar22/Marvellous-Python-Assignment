def Addition(no1,no2):
    return no1 + no2

def Substraction(no1,no2):
    return no1 - no2

def Multiplication(no1,no2):
    return no1 * no2

def Division(no1,no2):
    try:
        return no1/no2
    except ZeroDivisionError as zobj:
        print(zobj)

def main():
    print("Enter the First no :")
    no1 = int(input())
    print("Enter the second no :")
    no2 = int(input())
    
    sum = Addition(no1,no2)
    diff = Substraction(no1,no2)
    prod = Multiplication(no1,no2)
    div = Division(no1,no2)

    print("Addition is :",sum)
    print("Substraction is :",diff)
    print("Multiplication is :",prod)
    print("Division is :",div)


if __name__ == "__main__":
    main()