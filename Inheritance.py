class person:

    _name = "akki"
    __surname = "singh"
    yob = 1990

    def _age(self, current_year):   #protected function
        return current_year - self.yob
    def __age1(self,current_year):    #private function
        return current_year - self.yob

obj = person()
print(obj)
print(obj._age(2023))
print(obj._person__age1(2020))

# Inheritance-If I want to utilize all variable of a class in other class (child class)
class employee(person) :
    _name = "Ravi"
    __surname = "singh123"
    yob = 1989

obj1 = employee()
print(obj1._age(2023))
print(obj1._person__age1(2020))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)

