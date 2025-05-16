def numOfDigitSum(value):
    sum = 0
    
    while (value != 0):
        rem = value % 10
        value = int(value / 10)
        sum = sum + rem
    
    return sum


def main():
    print("Enter the number : ")
    no = int(input())

    result = numOfDigitSum(no)

    print("Number of digit in ",no,"is ",result)
    
if __name__== "__main__":
    main()
