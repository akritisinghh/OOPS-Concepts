# Polymorphism-Function is same and performing multiple task i.e. def test (a,b)-->print (test(3,4))-->print(test("Akriti ","Singh"))

class college:
    def students(self):
        print("Print students details ")

class class_type:
    def students(self):
        print("Print tha class type of students ")

def college_external(a):
    a.students()

c = college()
d = class_type()
college_external(c)
college_external(d)
