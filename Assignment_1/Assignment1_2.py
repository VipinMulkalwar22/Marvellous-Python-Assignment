def ChkNum(value):
    if((value % 2) == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter the no")
    no = int(input())
    ChkNum(no)

if __name__ == "__main__":
    main()