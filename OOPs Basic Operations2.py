class Person :
    def __init__(akki, name,surname,email,DOB):
       akki.name1 = name
       akki.surname = surname
       akki.email = email
       akki.DOB = DOB

    def __init__(akki, name,surname):
       akki.name1 = name
       akki.surname = surname

    def age(akki,current_year):             #if we take multiple constuctor to pass the data then program will consider last one
        return current_year

akriti = Person("akriti ", "singh")
ravi = Person("ravi","singh")
shivi = Person("shivi","Verma")
print(akriti.name1)
print(akriti.surname)
print(ravi.name1)
print(shivi.name1)
print(type(akriti))
# concatenation of data
print(akriti.name1  + akriti.surname)
print(akriti.age(2023))