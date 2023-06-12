class Person :
    ##Constuctor-init(pass data in class)-an method through which pass data in class
    ##Self in def (first variable is always a pointer) is pointer it points everything to the classes
    def __init__(self, name,surname, email,DOB):
       self.name1 = name
       self.surname = surname
       self.email = email
       self.DOB = DOB

akriti_var = Person("akriti", "singh", "akriti@gmail.com", 1999)
ravi = Person("ravi","singh","ravi@gmail.com", 1989)
shivi = Person("shivi","Verma","shivi@gmail.com", 1987)
print(akriti_var.name1)
print(akriti_var.surname)
print(akriti_var.email)
print(akriti_var.DOB)
print(ravi.name1)
print(shivi.name1)
print(ravi.email)
print(type(akriti_var))