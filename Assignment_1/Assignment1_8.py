def Display(value):
    for i in range(0,value,1):
        print("*",end=(" "))

def main():
    print("Enter the number")
    no = int(input())
    Display(no)

if __name__ == "__main__":
    main()