def ChkNum(value):

    if(value == 0):
        print("Zero")
    elif(value < 0):
        print("Negative Number")        
    else:
        print("Positive Number")


def main():
    print("Enter the no : ")
    no = float(input())
    ChkNum(no)

if __name__ == "__main__":
    main()