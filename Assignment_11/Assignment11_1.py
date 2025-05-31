def recDisplay(value):
    if(value > 1):
        recDisplay(value - 1)

    print(value,end=" ") 

def main():
    print("Enter the number")
    no = int(input())    

    recDisplay(no)

if __name__ == "__main__":
    main()