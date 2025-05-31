sum = 1
def Power(x,n):
    global sum
    if(n >= 1):
        sum = sum * x 
        Power(x,n-1)
    
    return sum
    
def main():
    print("Enter the number")
    no = int(input())    

    print("Enter the Power")
    pow = int(input()) 

    Ans = Power(no,pow)
    print(Ans)

if __name__ == "__main__":
    main()