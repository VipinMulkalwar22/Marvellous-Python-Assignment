from Arithmetic import Add,Mult,Sub,Div

def main():

    print("Enter the first no : ")
    no1 = int(input())
    print("Enter the Second no : ")
    no2 = int(input())

    result = Add(no1,no2)
    print("Addition is : ",result)

    result = Sub(no1,no2)
    print("Substraction is : ",result)

    result = Mult(no1,no2)
    print("Multiplication is : ",result)

    if (no2 != 0):
        result = Div(no1,no2)
        print("Division is : ",result)
    else:
        print("Please enter non-zero number")

if __name__ == "__main__":
    main()
