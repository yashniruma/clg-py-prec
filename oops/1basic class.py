class car:
    def __init__(self, name , year):
        self.name=name
        self.year= year
        
    def display(self):
        print("Name : ",self.name," Year :",self.year)
        
# make a class object and pass the two values than call the display()
c =car("mox", 111)
c.display()
        