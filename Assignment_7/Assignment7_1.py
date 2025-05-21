square = lambda no1 : no1 * no1
cube = lambda no1 : no1 * no1 * no1

def main():
    print("Enter the number")
    no1 = int(input())

    print("Square :",square(no1))
    print("Cube : ",cube(no1))
    

if __name__ == "__main__":
    main()