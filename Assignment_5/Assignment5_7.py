def Area(value1,value2): 
    return value1 * value2

def Perimeter(value1,value2):  
    return 2 * (value1 + value2)

def main():
    
    print("Enter the length of Rectangle")
    no1 = int(input())

    print("Enter the Width of Rectangle")
    no2 = int(input())

    A = Area(no1,no2)
    print("Area :", A)
    P = Perimeter(no1,no2)
    print("Perimeter :", P)
    
if __name__ == "__main__":
    main()