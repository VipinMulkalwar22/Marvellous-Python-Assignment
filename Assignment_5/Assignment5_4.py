def Largest(value1,value2,value3):  
    if(value1 >= value2 and value1 >= value3):
        print("Largest Number is", value1)
    elif(value2 >= value1 and value2 >= value3):
        print("Largest Number is", value2)
    else:
        print("Largest Number is", value3)        

def main():
    
    print("Enter the First No")
    no1 = int(input())

    print("Enter the Second No")
    no2 = int(input())

    print("Enter the Third No")
    no3 = int(input())

    Largest(no1,no2,no3)
    
if __name__ == "__main__":
    main()