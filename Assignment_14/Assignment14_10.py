class Employee:

    def __init__(self,esalary,edept,ename):
        self.__salary = esalary
        self._department = edept
        self.name = ename


    def DisplayPri(self):
        print("Salary:",self.__salary)

def main():
    eObj = Employee(1000,"IT","Vipin")
    print(eObj.name)
    print(eObj._department)
    #print(eObj.__salary)
    eObj.DisplayPri()

if __name__ == "__main__":
    main()