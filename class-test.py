
#sample person class with constructor as __init__ , getters and setters and exception handling
class Person :
    ' sample person class'
    
    # defining constructor 
    # need to pass self as a param to all the class methods
    def __init__(self, age = 0 , id = 0 ) :
        if type(age) not in [int] or type(id) not in [int] :
                raise Exception('age must be int') 
        self.__age = age
        self.__id = id
    
    def GetAge(self) :
        return self.__age
    
    def GetId(self) :
        return self.__id

    def SetAge(self,val) :
        if(type(val) not in [int] ) :
            raise Exception('age must be int') 
        self.__age = val       

    def SetId(self,val) :
        if(type(val) not in [int]) :
            raise Exception('id must be int')
        self.__id = val    

    def printPerson(self) :
        print('the age of the person is {0} and the id of the person is {1}'.format(self.GetAge(), self.GetId()))

try:
    c = Person()
    c.SetAge(22)
    print(c.GetAge(), c.GetId())
    c.printPerson()

except Exception as e :
    print(e)    