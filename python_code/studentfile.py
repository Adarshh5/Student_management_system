
from student import Database

class Student:

    def __init__(self):
        self.db = Database()

    def add_student(self):
        first_name = input("Enter name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        try:
            sql ="INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)"
            val = (first_name, last_name, email)
            self.db.mycursor.execute(sql, val)
            self.db.mydb.commit()
        except:
            print("error.")
        else:
            print(f"Student {first_name} added successfully.")
            print("1 record inserted, ID:", self.db.mycursor.lastrowid)

    def Student_Details(self):

        get_error = 0
        student_full_data = []
        try:
            student_id = int(input(" enter student_id: "))
            try:
                self.db.mycursor.execute(f"SELECT first_name, last_name, email FROM students WHERE student_id = {student_id}")
                myresult = self.db.mycursor.fetchone()
                student_full_data.append(myresult)
            except Exception as e:
                print(f"Not found {e}")
            else:
                try:
                        self.db.mycursor.execute(
                        f"SELECT course_id FROM courses_enrolled WHERE student_id = {student_id}")
                        myresult_ = self.db.mycursor.fetchone()
                        self.db.mycursor.execute(
                        f"SELECT  course_name, credits FROM courses WHERE course_id = {myresult_[0]}")
                        myresult_1 = self.db.mycursor.fetchone()
                        myresult_1 = myresult_ + myresult_1
                        student_full_data.append(myresult_1)

                except Exception as e:
                    get_error = 1
                    pass

                if get_error == 1:
                    for i in student_full_data:
                        print(f" name: {i[0]} {i[1]}, email : {i[2]}")
                else:
                    student_persnol_information = student_full_data[0]
                    print(f" name: {student_persnol_information[0]} {student_persnol_information[1]},   email : {student_persnol_information[2]}")
                    for i in range(1, len(student_full_data)):
                        print(f" enrolled_courses: [id: {student_full_data[i][0]}, name: {student_full_data[i][1]}, credits: {student_full_data[i][2]}] ")

        except:
            print(" somthing rong mybe id number")



class Course:

    def __init__(self):
        self.db = Database()
    def add_course(self):
        course_name = input("enter course name: ")
        credits = int(input("Enter credits: "))
        try:
            sql ="INSERT INTO courses (course_name, credits) VALUES (%s, %s)"
            val = (course_name, credits)
            self.db.mycursor.execute(sql, val)
            self.db.mydb.commit()
        except:
            print("error.")
        else:
            print(f"course {course_name} added successfully.")


    def enrolled_student_in_course(self):
        student_id =int(input("Enter student_id; "))
        course_id = int(input("Enter course_id; "))

        try:
            self.db.mycursor.execute(f"SELECT first_name FROM students WHERE student_id ={student_id}")
            myresult = self.db.mycursor.fetchone()
            self.db.mycursor.execute(f"SELECT course_name FROM courses WHERE course_id ={course_id}")
            myresult1 = self.db.mycursor.fetchone()
        except Exception as e:
            print(f"rong id  ..{e}")
        else:
            if myresult and myresult1:
                try:
                    sql = "INSERT INTO courses_enrolled (student_id, course_id) VALUES (%s, %s)"
                    val = (student_id, course_id)
                    self.db.mycursor.execute(sql, val)
                    self.db.mydb.commit()
                except Exception as e:
                    print(f"error  ..{e}")
                else:
                    print(f"student{myresult[0]} enrolled in {myresult1[0]} ")
            else:
                print("somthing rong mybe course_id or student_id")



class Grade:
    def __init__(self):
        self.db = Database()

    def add_grade(self):
        student_id = int(input("Enter student_id: "))

        try:
            self.db.mycursor.execute(f"SELECT first_name FROM students WHERE student_id ={student_id}")
            name = self.db.mycursor.fetchone()
        except Exception as e:
            print(f"not_match_error..{e}")
        else:
            if name:
                course_id = int(input("Enter course_id: "))
                try:
                    self.db.mycursor.execute(f"SELECT course_id FROM courses_enrolled WHERE student_id ={student_id}")
                    myresult = self.db.mycursor.fetchone()
                except Exception as e:
                    print(f"not_match_error..{e}")
                else:
                    if myresult:
                        if int(myresult[0]) == course_id:
                            grade = input("Enter grade: ")
                            try:
                                sql = "INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)"
                                val = (student_id, course_id, grade)
                                self.db.mycursor.execute(sql, val)
                                self.db.mydb.commit()
                            except Exception as e:
                                print(f"adding_error {e}")
                            else:
                                print(f"Grade {grade} assigned to student {student_id} for course {course_id}.")

                        else:
                            print(f"your given id is rong  and this is right id {myresult[0]}.")
                    else:
                        print("student is not enrolled in course")

            else:
                print("rong id")




class menu(Student, Course, Grade):

    def __init__(self):
        # super().__init__()  # keval isse bhi kam ban jayega
        Student.__init__(self)
        Course.__init__(self)
        Grade.__init__(self)

    def Action(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Enroll Student in Course")
            print("4. Assign Grade")
            print("5. View Student Details")
            print("6. Exit")
            choice = int(input("Enter number: "))

            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.add_course()
            elif choice == 3:
                self.enrolled_student_in_course()
            elif choice == 4:
                self.add_grade()
            elif choice == 5:
                self.Student_Details()
            elif choice == 6:
                exit()






obj = menu()
obj.Action()