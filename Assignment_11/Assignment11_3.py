sum = 0
def SumDigit(value):
    global sum 
    if(value > 0):
        rem = value % 10
        sum = sum + rem
        SumDigit(int(value / 10))
    
    return sum

def main():
    print("Enter the number")
    no = int(input())    

    Ans = SumDigit(no)

    print(Ans)

if __name__ == "__main__":
    main()