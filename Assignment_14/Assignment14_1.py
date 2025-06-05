class Employee:
    def __init__(self,ename,eemp_id,esalary):
        self.name = ename
        self.emp_id = eemp_id
        self.salary = esalary

    def Display(self):
        print("Name : {}, ID : {}, Salary : {}".format(self.name,self.emp_id,self.salary))
        
def main():
    Obj = Employee("Rohit",101,500000)
    Obj.Display()

if __name__ == "__main__":
    main()