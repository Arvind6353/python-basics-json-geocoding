class Person :

    def __init__(self, age, name):
        self.__age = age
        self.__name = name

    def GetAge(self) :
        return self.__age
    
    def GetName(self) :
        return self.__name

    def SetName(self, val):
        self.__name = val

    def SetAge(self, val) :
        self.__age = val


class Student(Person) :
    
    def __init__(self, age , name , id) :
        self.__id = id
        # invoke parent class constructor in 2 ways
        super(self.__class__, self).__init__(age,name)
        # Person.__init__(self,age,name)

    def GetId(self) :
        return self.__id 

    def SetId(self, val) :
        self.__id = val

    # overriding print for the object of this class
    def __str__(self) :
        return ' the name is ' + self.GetName() +' -- the age is '+ str(self.GetAge()) + ' -- id is '+ str(self.GetId())

s = Student(22,'arvind',0)
# the name is arvind -- the age is 22 -- id is 0
        
print(s)


        

    