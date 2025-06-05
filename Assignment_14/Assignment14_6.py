class Calculator:
    def __init__(self,value1,value2):
        self.no1 = value1
        self.no2 = value2

    def Add(self):
        return self.no1+self.no2

    def Substract(self):
        return self.no1-self.no2
    
    def Multiply(self):
        return self.no1*self.no2

    def Divide(self):
        return self.no1/self.no2


def main():
    print("Enter the first no :")
    no1 = int(input())
    print("Enter the second no :")
    no2 = int(input())

    cObj = Calculator(no1,no2)
    cadd = cObj.Add()
    csub = cObj.Substract()
    cmul = cObj.Multiply()
    cdiv = cObj.Divide()

    print("Addition :",cadd)
    print("Substraction :",csub)
    print("Multiply :",cmul)
    print("Divide :",cdiv)

if __name__ == "__main__":
    main()