class s:
    def __init__(self , name , id , age) :
        self.name = name
        self.id=id
        self.age = age
        
        
q = s("dada", 1, 24)

# prints the attribute name of the object s  
print(getattr(q,'name')) 

#  setattr in name
setattr(q,"name","dada_niru")

print(getattr(q,'name'))    # print(q.name)

# prints true if the s class contains the attribute with name id  
  
print(hasattr(q, 'id'))

# deletes the attribute age  
delattr(q, 'age') 

print(q.age) 




  


        