class dada:
    
    def __init__(self, nm , id, age):
        self.nm =nm
        self.id = id
        self.age = age
    
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))
        
d =dada("niruma", 1, 123)

print(d.__doc__)
print(d.__dict__)
print(d.__module__)
print(d.__format__)
print(d.__dir__)
