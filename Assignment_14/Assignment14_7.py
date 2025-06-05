class Person:
    def __init__(self,pName,pAge):
        self.name = pName
        self.age = pAge

class Teacher(Person):
    def __init__(self,tName,tAge,tSubject,tSalary):
        super().__init__(tName,tAge)
        self.subject = tSubject
        self.salary = tSalary

    def Display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Subject : ",self.subject)
        print("Salary : ",self.salary)

def main():
    tObj = Teacher("Vipin",10,"Maths",3000)
    tObj.Display()


if __name__ == "__main__":
    main()        