class Dog():
    #class attributes
    specie = 'mammal'
    
    # initialize class object
    def __init__(self, oruko, age):
        self.name = oruko
        self.age = age
        
        #create instance method
    def sound(self, sound):
        self.sound = sound
        return (self.sound)
        
    def addAge(self):
        self.age = self.age + 1
        print(f"The age of {wilder.name} is {wilder.age}")
