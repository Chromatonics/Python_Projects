from abc import ABC, abstractmethod

class Lass(ABC):
    def greet(self):
        print('Hello!')
    @abstractmethod
    def ing(self):
        pass

class Cla(Lass):
    def ing(self):
        print('World!')

obj = Cla()
obj.greet()
obj.ing()
