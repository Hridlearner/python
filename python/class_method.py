class Mobile:
    phone_type = 'smart'
    tution = 2000


    @classmethod
    def class_info(cls, ram, self):
        cls.ram= ram
        print(cls.phone_type, cls.ram, self.kk)

    def __init__(self):
        self.kk=20
        self.class_info('5gb', self)
        print(self.phone_type)

    def info(self):
        print(self.tution)#call class vriabe with instance

    def update_tution(self):
        self.tution = 3000    

#Mobile.class_info('2gb')
#print(Mobile.phone_type)
#print(Mobile.ram)

m=Mobile()
print(m.kk)
m.update_tution()
m.info()
#print(m.phone_type)
#print(m.ram)

