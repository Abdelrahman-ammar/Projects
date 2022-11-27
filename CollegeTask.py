class Person:
    def __init__(self,name,nationalid,phone,address,gender):
        self.name = name
        self.nationalid = nationalid
        self.phone = phone
        self.address = address
        self.gender = gender
    def get_details(self):
            return f'''Name:{self.name}
                        phone:{self.phone}
                        nationalid:{self.nationalid}
                        gender: {self.gender}
                        ***************'''

all_students = []    
class student(Person):
    cs_nums = [] #to know how many students we have in each department
    is_nums =[]
    se_nums=[]
    bio_nums =[]
    
    def __init__(self, name, nationalid, phone, address,academic_code,grade,gender,dept):
        assert len(academic_code)== 16 , 'please enter a right code consists of 16 digits' 
        self.academic_code = academic_code
        self.grade = grade
        self.dept = dept
        super().__init__(name, nationalid, phone, address,gender)
        if self.dept.lower() == 'cs':
            student.cs_nums.append(self)
        elif self.dept.lower() == 'se':
            student.se_nums.append(self)
        elif self.dept.lower() == 'is':
            student.is_nums.append(self)
        elif self.dept.lower() == 'bio':
           student.bio_nums.append(self)
        all_students.append(self)

    def get_academic_code(self):
        return self.academic_code
    def set_academic_code(self,code):
        self.academic_code = code
    def get_certificate(self):
        return f'Congratulations for graduation MR:{self.name} ,Hope life goes well for you'
   
    def enroll_course(self,course):
        if course in student_affair_emp.courses:
            return f'You are now enrolled in {course}'
        else:
            return f'''{course} isn\'t available to enroll in
                      **************'''
    
    def pay_bill(self):
        bill = 2500
        return f'you payed the bill {bill} ,{self.name}'
    
    def transfer_college(self,trans_college):
        return f'you want to transfer to another college {trans_college}'
    def absent(self,num_of_absents):
        available_abs = 4
        if num_of_absents > available_abs:
            return 'an alert is going to be send to you , you exceeded the abs available'
        else:
            return f'you were absent {num_of_absents} you still have {available_abs - num_of_absents} before alert is sent to you'
    @classmethod
    def previliges(cls):
        print('''Here is a list of what you can do:
              1-Get or Set your academic code
              2-Get your Certificate
              3-Enroll course
              4-Pay your Bills
              5-Transfer to another college
              6-Absent Times''')
              
    
    
class student_affair_emp(Person):
    courses = ['Math','Physics','Algorithms','Machine Learning']
    def __init__(self, name, nationalid, phone, address,employeeid,salary,hours,gender):
        self.salary = salary
        self.hours = hours
        self.employeeid = employeeid
        super().__init__(name, nationalid, phone, address,gender)
        
    def update_put_course(self,course,year):
        if year == 1:
            if course in student_affair_emp.courses:
                return f'{course} exists already'
            else:
                student_affair_emp.courses.append(course)
                return f'''{course} is added succefully
                        ************'''
        elif year==2:
            student_affair_emp.courses.append(course)
            return f'{course} is added'
    def register_student(Student):
        return f'{Student.name} is now registered'
    def update_grades(self,Student,new_grade):
        Student.grade = new_grade
        print(f'{Student.name} grade\'s has been updated')

    def delete_student(self,name):
        for i in range(all_students.__len__()):
            if all_students[i].name == name:
                del all_students[i]
                print(f'student {name} has been deleted')
                break
                 
                
    @classmethod
    def previliges(cls):
        print('''Here is a list of what you can do:
              1-Update or Put a new course
              2-Register Student
              3-Update Student Grades
              4-Delete Student with name
              ''')
              
            
class doctor(Person):
    def __init__(self, name, nationalid, phone, address,salary,gender):
        super().__init__(name, nationalid, phone, address,gender)
        self.salary = salary
    def view_student_profile(self,Student):
        print(f"{Student.name} profile: ")
        return Student.get_details()
    def kick_student_out(self):
        return 'Don\'t attend this session any more'
    def teach_course(self,course):
        return f'teaching {course}'
    def view_stud_in_dept(self,dept):
        if dept.lower() == 'cs':
            return len(student.cs_nums)
        elif dept.lower() == 'se':
            return len(student.se_nums)
        elif dept.lower() == 'is':
            return len(student.is_nums)
        elif dept.lower() == 'bio':
            return len(student.bio_nums)
    @classmethod
    def previliges(cls):
         print('''Here is a list of what you can do:
               0-Get doctor details
               1-View Student profile
               2-Kick student out
               3-Teach course
               4-View number of the students in the depatarment you teach
               ''')
    
    
class department:
    def __init__(self,dept):
        self.dept = dept
    def show_numberOFstudents(self):
        if self.dept.lower() == 'cs':
            return len(student.cs_nums)
        elif self.dept.lower() == 'se':
            return len(student.se_nums)
        elif self.dept.lower() == 'is':
            return len(student.is_nums)
        elif self.dept.lower() == 'bio':
            return len(student.bio_nums)
    def show_description(self):
        if self.dept.lower() == 'cs':
            return 'This is Computer Science departement, best place to learn more about algorithms and machine learning, how computer works and much more'
        elif self.dept.lower() =='is':
            return 'This is Information System department, Here you can learn all about systems and how to implement it from scratch'
        elif self.dept.lower() =='se':
            return 'Welcome to Software Enginnering department , We give you here all what you will need to know about se , how to build software systems and how it works and much more advanced things'
        elif self.dept.lower() =='bio':
            return 'This is Bio Informatics department,Here you will learn how biology and computer science is combined together to help people and improving their medical life'
        




s1 = student('mohammed', '30120', '0106693', 'Egypt', '423947292jr2134y', 99, 'male','cs')
s2 = student('ali', '30120', '234', 'Egypt', '423947292jr2134y', 99, 'male','is')
s3 = student('yasser', '30120', '234', 'Egypt', '423947292jr2134y', 99, 'male','is')

ahmed = student_affair_emp('ahmed', '123', '124', 'Egypt', '3020293343', 3434 , 23,'male')
student_affair_emp.previliges()
print("*************")
print(ahmed.update_put_course('Electronics',2))
print(ahmed.get_details())
print(s1.enroll_course('Database'))


d1 = doctor('rafaat', '1234', '0123734', 'Egypt', 3200,'male')
print(d1.kick_student_out())


print(d1.view_student_profile(s1))
print(d1.get_details())
de1 = department('cs')
print(de1.show_numberOFstudents())
print("*********")
print(de1.show_description())
print("*********")
de2 = department('is')
print(de2.show_numberOFstudents())
print("*********")
ahmed.delete_student('ali')
print("*************")



