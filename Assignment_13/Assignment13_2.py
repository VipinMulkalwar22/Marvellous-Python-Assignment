class BankAccount:
    ROI = 10.5

    def __init__(self,uName,uAmount):
        self.Name = uName
        self.Amount = uAmount

    def Display(self):
        print("Name :"+self.Name)
        print("Amount :",self.Amount)

    def Deposit(self):
        print("Enter the Deposit Amount")
        self.Amount = int(input())

    def Withdraw(self):
        print("Enter the Withdraw Amount")
        wValue = int(input())
        self.Amount = self.Amount - wValue 

    def CalculateInterest(self):
        IntAmt = (self.Amount * BankAccount.ROI * 1)/100
        print("Interest Amount = ",IntAmt)

def main():
    Obj1 = BankAccount("Vipin","0.0")
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.CalculateInterest()
    Obj1.Display()


if __name__ == "__main__":
    main()