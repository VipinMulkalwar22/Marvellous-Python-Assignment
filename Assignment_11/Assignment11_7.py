i = 1
def Display(n):
    # for i in range(1,value+1):
    #     for j in range(1,i+1):
    #         print("*",end = " ")
    #     print()

    # i = 1
    # while(value >= i):
    #     j = 1
    #     while(i >= j):
    #         print("*", end=" ")
    #         j = j + 1
    #     print()
    #     i = i + 1
    global i
    if(n >= 1):
        print("*" * i,sep=" ",end = "\n")
        i = i + 1
        Display(n-1)

def main():
    print("Enter the number")
    no = int(input())    
    Display(no)
    
if __name__ == "__main__":
    main()