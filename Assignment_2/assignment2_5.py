def chkPrime(value):
    
    if(value <= 1):
        return False

    for i in range(2,int(value ** 0.5)+1):
        if(value % i == 0):
            return False
            break
    
    return True

def main():
    print("Enter the number : ")
    no = int(input())

    result = chkPrime(no)

    if result == True:
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

    
if __name__== "__main__":
    main()
