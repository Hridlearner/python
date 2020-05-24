class Student:
    uni = 'UPB'
    def __init__(self, name, ID):
        self.name = name
        self.ID =  ID
        self.age= self.get_age()

    def get_age(self):
        pass
    
    #if we dont use any class or instance variable in a function
    #its better to write as a static method
    @staticmethod   
    def get_info(x,y):
        print(x,y)
        #print(self.name)
    

s = Student('hrid',500)
s.get_info(50,6,)