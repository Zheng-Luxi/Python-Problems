class Person:
    def __init__( self, name, age ):
        self.name = name
        self.age = age
    
    def introduce(self):
        if self.name == 'Baby Fish':
            print( "Hello, I am Shan Bei and I am 250 years old." )
        else:
            print( "Hello, I am %s, and I am %d " % ( self.name, self.age ) )

class Student(Person):
    def __init__( self, name, age ):
        super().__init__( name, age )
    
    def study(self):
        if self.name == 'Baby Fish':
            print( "Hello, I am playing and I don't want to study!" )
        else:
            print( "Hello, I am studying hard now!" )


babyFish = Student( "Baby Fish", 14 )
intelligent = Student( "Intelligent", 14 )

print( "Baby Fish introduce:" )
babyFish.introduce()

print("-----------------")

print( "Intelligent introduce:" )
intelligent.introduce()

print("-----------------")
print( "Baby Fish study:" )
babyFish.study()

print("-----------------")
print( "Intelligent study:" )
intelligent.study()