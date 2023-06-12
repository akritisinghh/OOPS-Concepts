# Data Abstraction -where we hide data behind class
class college :
    __students = "CS"

    def students(self):
        print("print the class of students " , college.__students)

i = college()
i.students()
print(i._college__students)

list()