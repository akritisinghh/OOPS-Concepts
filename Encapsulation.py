# Encapsulation

class college :
    def __init__(self):
        self.students1 = "Data Science"

    def students(self):
        print(self.students1)

c = college()
c.students()   #function
c.students1 = "Data Analytics"
c.students()

class college1 :
    def __init__(self):
        self.__students1 = "Data Science"

    def students(self):
        print(self.__students1)  # or _college1__students1

   # def student_change(self):
       # self.__students1 ="BIG DATA"
    def student_change(self,new_value):
        self.__students1 =new_value

c1 = college1()
c1.students()
c1.__students1 = "big data"
c1.students()
c1.student_change("BIG DATA1")
c1.students()

# Encapsulation -User can not modify value of variables directly through object assignment. Values of variables can be changed by function/methods
#Abstraction- Hiding a variable behind the class 