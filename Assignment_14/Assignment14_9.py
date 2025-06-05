class Product:

    def __init__(self,pName,pPrice):
        self.Name = pName
        self.Price = pPrice

    def __eq__(self, other):                         # Dunder Method
        if isinstance(other, Product):
            if other.Price == self.Price:
                return True
        return False


def main():
    pObj1 = Product("Java",100)
    pObj2 = Product("Python",100)

    print(pObj1 == pObj2)


if __name__ == "__main__":
    main()