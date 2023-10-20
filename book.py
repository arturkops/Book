class Autor:
    def __init__(self,name,age,address,birth):
        self.name = name 
        self.age = age 
        self.address = address
        self.birth = birth
    
    def printData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
    
    def calc(self,actual_year):
        idade = actual_year - self.birth
        return idade 

class Book(Autor):
    def __init__(self, name, age, address,title,year,pages,price,editor):
        super().__init__(name, age, address)
        self.title = title
        self.year = year
        self.pages = pages 
        self.price = price 
        self.editor = editor

    def printData(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Pages: {self.pages}")
        print(f"Price: {self.price}")
        print(f"Editor: {self.editor}")

    