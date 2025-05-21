def CeltoFahrenheit(value1):  
    return ((value1 * (9/5)) + 32)

def main():
    
    print("Enter the temperature in Celsius")
    no1 = int(input())

    Fahr = CeltoFahrenheit(no1)
    print("Temperature in Fahrenheit is : ", Fahr)
    
if __name__ == "__main__":
    main()