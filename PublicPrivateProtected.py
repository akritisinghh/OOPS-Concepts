#from test2 import person #importing one class only from test2
from utils.utill1 import person2
# or import utils.utill1
#  package-->directory/folder , module--> python file in file we have class objects and components


obj = person2("ram", "verma",1986)
print(obj.yob1)
print(obj._name1)

class person1:
    def __init__(self, name, surname, yob):
        self._name1 = name #_Protected variable-->_
        self.__surname1 = surname # __Private notation--> __
        self.yob1 = yob #Public variable with no underscore

akki = person1("akriti","singh",1999)
print(akki._person1__surname1)  #to call private variable we need to call along with class name
print(akki._name1)