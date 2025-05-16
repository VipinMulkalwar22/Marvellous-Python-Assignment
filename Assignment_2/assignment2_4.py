def sumFactors(value):
    sum = 0
    for i in range(1,int(value/2)+1):
        if(value % i == 0):
            sum = sum + i 
    return sum

def main():
    print("Enter the number : ")
    no = int(input())

    result = sumFactors(no)

    print("Addition of factors is",result)

if __name__== "__main__":
    main()
