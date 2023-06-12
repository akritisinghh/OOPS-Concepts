class person:
    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        print("take an email id as input ",email_id)

    def ask_name(self):
        name= input("Please enter your name ")
        return name

    def DOB_name(self):
        DOB = input("please enter your DOB ")
        return DOB

akriti = person()
ravi = person()
parul = person()
shivank = person()

akriti.email_id_input("akriti@gmail.com")
print(akriti.ask_name())
print(ravi.DOB_name())
print(akriti.age(2023,2000))