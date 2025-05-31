class BookStore:
    NoOfBooks = 0

    def __init__(self,uName,uAuthor):
        self.Name = uName
        self.Author = uAuthor
        BookStore.NoOfBooks +=1

    def Display(self):
        print("{} by {}. Number of Books : {}".format(self.Name,self.Author,BookStore.NoOfBooks))

def main():

    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2= BookStore("C Programming","Dennis Richie")
    Obj2.Display()

if __name__ == "__main__":
    main()