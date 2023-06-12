class Person :
    def __init__(akki, name,surname, email,DOB):
       akki.name1 = name
       akki.surname = surname
       akki.email = email
       akki.DOB = DOB

    def age(akki,current_year):
        return current_year-akki.DOB

akriti = Person("akriti ", "singh", "akriti@gmail.com", 1999)
ravi = Person("ravi","singh","ravi@gmail.com", 1989)
shivi = Person("shivi","Verma","shivi@gmail.com", 1987)
print(akriti.name1)
print(akriti.surname)
print(akriti.email)
print(akriti.DOB)
print(ravi.name1)
print(shivi.name1)
print(ravi.email)
print(type(akriti))
# concatenation of data
print(akriti.name1  + akriti.surname)
print(akriti.age(2023))