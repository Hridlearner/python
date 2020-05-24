class Mobile:
    phone_type = 'smart'
    tution = 2000


    @classmethod
    def class_info(cls, ram, self):
        cls.ram= ram
        print(cls.phone_type, cls.ram, cls.tution)

    def __init__(self):
        self.kk=20
        self.class_info('5gb', self)
        print(self.phone_type)

    def info(self):
        print(self.tution)#call class vriabe with instanc
    @classmethod
    def update_tution(cls):
        cls.tution = 3000    

#Mobile.class_info('2gb')
#print(Mobile.phone_type)
#print(Mobile.ram)

m=Mobile()
print(m.kk)
Mobile.update_tution() #call class method by usisng class name (conventional)
m.info()

m2 = Mobile()
#print(m.phone_type)
#print(m.ram)

