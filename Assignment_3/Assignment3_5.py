from MarvellousNum import chkPrime

def ListPrime(value):
    sum = 0
    primeNo = []
    for i in range(len(value)):
        isPrime = chkPrime(value[i])
        if (isPrime == True):
            primeNo.append(value[i])
            sum = sum + value[i]

    return sum,primeNo

def main():
    Data= []
    print("Enter the number of element :")
    size = int(input())

    print("Enter each element :")

    for i in range(size):
        no = int(input())
        Data.append(no)
    
    print("Input Elements :", Data)
    total,primeValue = ListPrime(Data)
    print("Prime Elements Are :", primeValue)
    print("Sum :", total)
    
if __name__ == "__main__":
    main()   