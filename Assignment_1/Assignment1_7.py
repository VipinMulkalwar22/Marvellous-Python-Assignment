def ChkNum(value):
    if((value % 5) == 0):
        return True
    else:
        return False

def main():
    print("Enter the no")
    no = int(input())
    Result = ChkNum(no)
    print(Result)

if __name__ == "__main__":
    main()