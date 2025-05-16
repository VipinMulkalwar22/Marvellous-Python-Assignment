def numOfDigit(value):
    count = 0
    
    while (value != 0):
        value = int(value / 10)
        count = count + 1
    
    return count


def main():
    print("Enter the number : ")
    no = int(input())

    result = numOfDigit(no)

    print("Number of digit in ",no,"is ",result)
    
if __name__== "__main__":
    main()
