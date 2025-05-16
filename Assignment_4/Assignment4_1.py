power=lambda value : value * value

def main():
    print("Enter the no :")
    no = int(input())

    result = power(no)
    print("Power of",no,"is",result)

if __name__ == "__main__":
    main()