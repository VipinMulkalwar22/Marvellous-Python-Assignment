def chkPrime(no):
    if(no <= 1):
        return False

    for i in range(2,int(no ** 0.5)+1):
        if(no % i == 0):
            return False
            break
    return True

def main():
    print("Enter a number :")
    no = int(input())
    Result = chkPrime(no)
    if (Result == True):
        print(no,"is a prime number")
    else:
        print(no,"is not a prime number")

if __name__ == "__main__":
    main()