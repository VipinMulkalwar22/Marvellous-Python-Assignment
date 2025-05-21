def Display(no):
    for i in range(no+1):
        for j in range(i):
            print("*",end=" ")
        print(end="\n")

def main():
    print("Enter a number :")
    no = int(input())
    Display(no)

if __name__ == "__main__":
    main()