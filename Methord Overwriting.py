class college:
    def student(self):
        print("Details of all the students ")
    def achievers(self):
        print("List of all the achievers ")
    def hall_of_frame(self):
        print("Name of all the students from hall of frame ")

class college_vision(college):
    def student(self):    #methord Overwriting-in this case program will execute method which is rewritten in child class  
        print("these are final student list ")

cv = college_vision()
cv.student()