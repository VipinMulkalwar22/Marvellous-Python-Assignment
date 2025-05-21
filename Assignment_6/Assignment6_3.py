def DisplayTable(no):
    i = 1
    while(i <= 10):
        total = 0
        total = no * i
        print(no,"*",i,"=",total)
        i=i+1
    
def main():
    print("Enter a number :")
    no = int(input())
    Result = DisplayTable(no)

if __name__ == "__main__":
    main()