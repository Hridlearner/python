class Stundent:

    school_name = 'UPB'

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.age = None
        self.height= self.get_height()
        self.age_info = self.age_func()
        self.total_mark=None

    def info(self):
        print(self.name, self.id, self.age)

    def set_age(self, age):
        self.age=age

    def age_func(self):
        self.set_age(50)
        #print(self.age)

    def get_height(self):
        self.house_number = 243
        return 165


    def marks(self, math, phy, che):
        self.total_mark = math +phy+che
        print(self.total_mark)
        print(self.house_number)
    #only access class variables, 
    @classmethod
    def school(cls):
        print(cls.school_name)     

s = Stundent('hrid', 155)

s.info()
#s.marks(10,12,13)
print(s.total_mark)
print(s.house_number)
#s.age()
#class method can be accessed both wazs bz class or by instance
#Stundent.school()
#s.school()


#i can create a set variable anytime in another function as well, but it is good to create the variable in init as none or defauls 
#value and update later according to the function ouput

print(s.__repr__)
