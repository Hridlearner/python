from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('runnung')

#com = Computer()
com1 = Laptop()
com1.process()




        