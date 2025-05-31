Fact = 1
def Factorial(value):
    global Fact
    
    if(value >= 1):
        Fact = Fact * value
        Factorial(value - 1)
    
    return Fact

def main():
    print("Enter the number")
    no = int(input())    

    Ans = Factorial(no)

    print(Ans)

if __name__ == "__main__":
    main()