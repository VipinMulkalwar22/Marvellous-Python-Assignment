multiplication=lambda value1,value2 : value1 * value2

def main():
    print("Enter the first no :")
    no1 = int(input())

    print("Enter the Second no :")
    no2 = int(input())

    result = multiplication(no1,no2)
    print("multiplication is",result)

if __name__ == "__main__":
    main()