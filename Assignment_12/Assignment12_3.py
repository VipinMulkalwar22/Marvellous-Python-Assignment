class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        print("Enter the First No :")
        self.value1 = int(input())

        print("Enter the Second No :")
        self.value2 = int(input())

    def Addition(self):
        return self.value1 + self.value2

    def Substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1/self.value2
        
def main():
    
    obj1 = Arithmatic()
    obj1.Accept()
    Add = obj1.Addition()
    print("Addition : ",Add)
    Sub = obj1.Substraction()
    print("Substraction : ",Sub)
    Mul = obj1.Multiplication()
    print("Multiplication : ",Mul)
    Div = obj1.Division()
    print(f"Division : {Div:.2f}")

if __name__ == "__main__":
    main()