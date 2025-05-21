def Sum(no):
    i = 2
    total = 0
    while(i <= no):
        if(i % 2 == 0):
            total = total + i
        i=i+1
    return total

def main():
    Result = Sum(100)
    print("Sum of even numbers between 1 to 100 is :",Result)

if __name__ == "__main__":
    main()