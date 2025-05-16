def Factorial(value):
    Fact = 1
    for i in range(value,0,-1):
        Fact = Fact * i
    return Fact

def main():
    print("Enter the number : ")
    no = int(input())

    result = Factorial(no)

    print("Factorial of ",no,"is",result)

if __name__== "__main__":
    main()
