class Vehicle:
    def start(self):
        print("Type of Vehicle is : ")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car")

def main():
    vObj = Vehicle()
    cObj = Car()

    cObj.start()

if __name__ == "__main__":
    main()    

