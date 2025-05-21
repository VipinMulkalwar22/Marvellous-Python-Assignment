def Factorial(no):
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    
    return Fact
    
def main():
    print("Enter a number :")
    no = int(input())
    Result = Factorial(no)
    print("Factorial of",no,"is",Result)

if __name__ == "__main__":
    main()