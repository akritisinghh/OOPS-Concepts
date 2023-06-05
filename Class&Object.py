class person1:
    def __init__(self, name, surname, yob):
        self._name1 = name #_Protected variable-->_
        self.__surname1 = surname # __Private notation--> __
        self.yob1 = yob #Public variable with no underscore

akki = person1("akriti","singh",1999)
print(akki._person1__surname1)  #to call private variable we need to call along with class name
print(akki._name1)