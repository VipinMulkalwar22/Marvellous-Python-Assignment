def Display(value):
    for i in range(1,value+1):
        for j in range(1,value+1):
            print(j, end=" ")
        print(end="\n")

def main():
    print("Enter the number :")
    no = int(input())
    Display(no)

if __name__ == "__main__":
    main()