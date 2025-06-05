class BankAccount:

    def __init__(self,act_number,act_name,act_balance):
        self.account_number = act_number
        self.name = act_name
        self.balance = act_balance

    def Deposit(self):
        print("Enter the Deposit Amount")
        self.balance = int(input())

    def Withdraw(self):
        print("Enter the Withdraw Amount")
        Amount = int(input())
        self.balance = self.balance - Amount
        return self.balance

    def Display(self):
        print("Account Name : {}, Account No : {}, Balance : {}".format(self.name,self.account_number,self.balance))
        
def main():
    baObj = BankAccount(100,"Vipin",25000)
    baObj.Deposit()
    baObj.Withdraw()
    baObj.Display()

if __name__ == "__main__":
    main()