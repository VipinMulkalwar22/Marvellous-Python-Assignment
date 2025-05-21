def EvenOdd(value1):  
    if(value1 % 2 == 0):
        print(value1,"is even number")
    else:
        print(value1,"is an odd number")     

def main():
    
    print("Enter the First No")
    no1 = int(input())

    EvenOdd(no1)
    
if __name__ == "__main__":
    main()