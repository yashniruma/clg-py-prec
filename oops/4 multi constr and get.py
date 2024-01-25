class dada:
    def __init__(self):
        print("this is the 1")
        
    def se(self):
        print("this is the 2")
        
    def th(self):
        print("this is the 3")
    
    
    def info(self):
        print("1. for 1")
        print("2. for 2")
        print("3. for 3")
        
        s= int(input("Enter Choice :- \t "))
        
        if s==1:
            self.__init__()
            
        elif s==2:
            self.se()
            
        elif s==3:
            self.th()
           
d= dada()
d.info()
        