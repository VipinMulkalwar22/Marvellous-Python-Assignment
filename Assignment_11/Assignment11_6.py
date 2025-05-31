sum = 0
def Addition(value):
    global sum
    
    if(value >= 1):
        sum = sum + value
        Addition(value - 1)

    return sum
    
def main():
    print("Enter the number")
    no = int(input())    

    Ans = Addition(no)
    print(Ans)

if __name__ == "__main__":
    main()