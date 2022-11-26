import mysql.connector as sql
from mysql.connector import Error

    



class Person:
    def __init__(self,name,age,idd,phone):
        self.name = name
        self.age = age
        self.idd = idd
        self.phone = phone
        # self.role = role
        
    
    def get_details(self):
        print(f'''
              Name : {self.name}
              Age : {self.age}
              Phone : {self.phone}
                ''')
                
class Admin(Person):
    db = False
    courses_base =[]
    def __init__(self, name, age, idd, phone):
        super().__init__(name, age, idd, phone)

    def create_newdata_base(self,dbname):
        if not Admin.db:
            my_cursor.execute(f'CREATE DATABASE {dbname}')
            print("data base created succesfully")
            Admin.db = True
        
        
    def create_course_base(self,course_name):
    
            if course_name not in Admin.courses_base:
                my_cursor.execute(f'USE College')
                create_table = f"CREATE TABLE {course_name}( nums INT AUTO_INCREMENT PRIMARY KEY , student_name VARCHAR(255) , hours int  )" 
                my_cursor.execute(create_table)
                Admin.courses_base.append(course_name)
                print(f"{course_name} base created succesfully")
        
            
    def Previliges(self):
        operation = ""
        print(''''What you can do:
0-Create new database
1-create_course_base
2-Add_student_course
3-Delete_student_course''')
        user_choice=int(input("choose operation number "))
        # if user_choice == 1:
            # operation="create_course_base(course_name,credit_hours)"
        return user_choice
    def Add_student_course(self,studentt_name,course):
        my_cursor.execute(f'USE College')
        insert = f'INSERT INTO {course}  VALUES(0,{studentt_name} , 3)'
        my_cursor.execute(insert)
        print("Student added Succesfully")
        
            

class Student(Person):
    def __init__(self,name,age,idd,phone,year):
        self.year = year
        super().__init__(name, age, idd, phone)
        
    def enroll_course(self,course):
        self.course = course
        print("Course Added succseffully")

    def get_average_gpa():
        pass

class doctor(Person):
    def __init__(self, name, age, idd, phone,specialization):
        super().__init__(name, age, idd, phone)
        self.specialization = specialization
    
    
    def get_details(self):    
        print(f'''
              Name : {self.name}
              Age : {self.age}
              Phone : {self.phone}
                ''')


    def view_student_details(Student):
        print(Student.get_details())





try:
    mydb = sql.connect(
        host="localhost",
        user = "root",
        passwd = "yasser!20",
        use_pure = True
    )
    print(mydb)
except Error as e:
    print(e)

my_cursor = mydb.cursor()



name = ""
age = None
idd = ""
phone = ""

def user_info():
    global name,age,idd,year
    name = input("Name: ")
    idd = input("ID: ")
    age=int(input("Age: "))
    phone = input("Phone: ")


adm = Admin("ahmed", 20, 30, 99)
# adm.create_newdata_base("college")
# adm.create_course_base("Math")
adm.Add_student_course("ahmed", "math")
    

# user = input("Please Enter user type: ")
# # Done = False
# if user.lower() == "admin":
#     user_info()
#     Admin1 = Admin(name, age, idd, phone)
#     operation = Admin1.Previliges()
# #     while True:
#     if operation ==0:
#         db= input("Database Name: ")
#         Admin1.create_newdata_base(db)
#     elif operation == 1:
#         Course = input("Enter Course Name: ")
#         Admin1.create_course_base(Course)
#         # Done = input("End to exit No to continue: ")
# #         if Done.lower() == "end":
# #             break
# #         else:
# #             operation = int(input("operation num:"))
    
