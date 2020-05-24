class Student:

    def __init__(self, name, ID):
        self.name = name
        self.ID =  ID
        self.age= self.get_age()

    def get_age(self):
        pass

s = Student('hrid',500)