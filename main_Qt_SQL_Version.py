# By Karim Abboud

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QWidget, QLineEdit, QFormLayout, QMessageBox, QDialog, QComboBox,
    QTabWidget, QTableWidget, QTableWidgetItem,QDialogButtonBox
)
from PyQt5.QtCore import Qt

from Student import Student
from Instructor import Instructor
from Course import Course
from Data_Managment import *


instructor1 = Instructor("John", 25, "what@test.com", "1000")
instructor2 = Instructor("Jane", 30, "test@test.com", "1001")

course1 = Course("CSC101", "Introduction to Computer Science", instructor1)
course2 = Course("CSC102", "Introduction to Programming", instructor1)


students = get_all_students()
instructors = get_all_instructors()
courses = get_all_courses()
print(instructors)
print(courses)


class SchoolManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(100, 100, 800, 200) 

        central_widget = QWidget(self)
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the School Management System", self)
        welcome_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(welcome_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # Group 1: Forms and Registration
        form_layout = QHBoxLayout()
        student_button = QPushButton("Student Form")
        student_button.clicked.connect(self.open_student_form)

        instructor_button = QPushButton("Instructor Form")
        instructor_button.clicked.connect(self.open_instructor_form)

        course_button = QPushButton("Course Form")
        course_button.clicked.connect(self.open_course_form)

        register_student_button = QPushButton("Register Student for Course")
        register_student_button.clicked.connect(self.open_student_registration_form)

        assign_instructor_button = QPushButton("Assign Instructor to Course")
        assign_instructor_button.clicked.connect(self.open_instructor_assignment_form)

        form_layout.addWidget(student_button)
        form_layout.addWidget(instructor_button)
        form_layout.addWidget(course_button)
        form_layout.addWidget(register_student_button)
        form_layout.addWidget(assign_instructor_button)

        # Group 2: Display and Save/Load Data
        data_layout = QHBoxLayout()
        display_records_button = QPushButton("Display All Records")
        display_records_button.clicked.connect(self.open_display_all_records)

        save_button = QPushButton("Backup Data")
        save_button.clicked.connect(self.save_data)

        # load_button = QPushButton("Load Data")
        # load_button.clicked.connect(self.load_data)

        data_layout.addWidget(display_records_button)
        data_layout.addWidget(save_button)
        # data_layout.addWidget(load_button)

        # # Group 3: Export Data
        # export_layout = QHBoxLayout()
        # export_students_button = QPushButton("Export Students to CSV")
        # export_students_button.clicked.connect(self.export_students_to_csv)

        # export_instructors_button = QPushButton("Export Instructors to CSV")
        # export_instructors_button.clicked.connect(self.export_instructors_to_csv)

        # export_courses_button = QPushButton("Export Courses to CSV")
        # export_courses_button.clicked.connect(self.export_courses_to_csv)

        # export_layout.addWidget(export_students_button)
        # export_layout.addWidget(export_instructors_button)
        # export_layout.addWidget(export_courses_button)

        # Add all layouts to the main layout
        layout.addLayout(form_layout)
        layout.addLayout(data_layout)
        # layout.addLayout(export_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_student_form(self):
        form = StudentForm(self)
        form.exec_()

    def open_student_registration_form(self):
        form = StudentRegistrationForm(self)
        form.exec_()

    def open_instructor_form(self):
        form = InstructorForm(self)
        form.exec_()

    def open_instructor_assignment_form(self):
        form = InstructorAssignmentForm(self)
        form.exec_()

    def open_course_form(self):
        form = CourseForm(self)
        form.exec_()

    def open_display_all_records(self):
        form = DisplayAllRecords(self)
        form.exec_()

    def display_statistics(self):
        # Calculate statistics
        num_students = len(students)
        num_instructors = len(instructors)
        num_courses = len(courses)

        # Display a message box with the statistics
        QMessageBox.information(self, "Statistics", f"Total Students: {num_students}\n"
                                                    f"Total Instructors: {num_instructors}\n"
                                                    f"Total Courses: {num_courses}")
        
    def save_data(self):
        conn = connect()
        cursor = conn.cursor()

        try:
            # Clear existing data
            cursor.execute("TRUNCATE students, instructors, courses RESTART IDENTITY;")
            
            # Insert students
            for student in students:
                cursor.execute("""
                    INSERT INTO students (student_id, name, age, email)
                    VALUES (%s, %s, %s, %s);
                """, (student[0], student[1], student[2], student[3]))

            # Insert instructors
            for instructor in instructors:
                cursor.execute("""
                    INSERT INTO instructors (instructor_id, name, age, email)
                    VALUES (%s, %s, %s, %s);
                """, (instructor.instructor_id, instructor.name, instructor.age, instructor.email))
            
            # Insert courses
            for course in courses:
                cursor.execute("""
                    INSERT INTO courses (course_id, course_name, instructor_id)
                    VALUES (%s, %s, %s);
                """, (course.course_id, course.course_name, course.instructor.instructor_id))
            
            conn.commit()
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


    def load_data(self):
        students = get_all_students()
        instructors = get_all_instructors()
        courses = get_all_courses()


    def export_students_to_csv(self):
        export_students_to_csv(students)
        QMessageBox.information(self, "Success", "Students data exported to CSV successfully!")

    def export_instructors_to_csv(self):
        export_instructors_to_csv(instructors)
        QMessageBox.information(self, "Success", "Instructors data exported to CSV successfully!")

    def export_courses_to_csv(self):
        export_courses_to_csv(courses)
        QMessageBox.information(self, "Success", "Courses data exported to CSV successfully!")

        


class StudentForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Student")
        self.setGeometry(200, 200, 400, 300)

        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        # self.student_id_input = QLineEdit(self)

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Email:", self.email_input)
        # form_layout.addRow("Student ID:", self.student_id_input)

        add_button = QPushButton("Add Student", self)
        add_button.clicked.connect(self.add_student)

        form_layout.addWidget(add_button)

        self.setLayout(form_layout)

    def add_student(self):
        name = self.name_input.text()
        age = int(self.age_input.text())
        email = self.email_input.text()
        # student_id = self.student_id_input.text()

        if not name or not age or not email:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")

        else:
            try:
                stu = create_student(name, age, email)
                
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))
                return

            # Here you would handle adding the student, e.g., by saving it to a file or a list
            QMessageBox.information(self, "Success", f"Student {name} added successfully!")
    

class StudentRegistrationForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Register Student for Course")
        self.setGeometry(200, 200, 400, 300)

        form_layout = QFormLayout()

        students = get_all_students()
        courses = get_all_courses()


        # ComboBox for selecting student
        self.student_input = QComboBox(self)
        # Dictionary to map student names to Student objects
        self.student_map = {}

        # Populate ComboBox with student names and map them to the actual Student objects
        if students:
            for student in students:
                self.student_input.addItem(student[1])  # Add student name to combo box
                self.student_map[student[1]] = student  # Map the name to the Student object


        # ComboBox for selecting course
        self.course_input = QComboBox(self)
        # Dictionary to map course names to Course objects
        self.course_map = {}

        # Populate ComboBox with course names and map them to the actual Course objects
        if courses:
            for course in courses:
                self.course_input.addItem(course[1])  # Add course name to combo box
                self.course_map[course[1]] = course  # Map the name to the Course object

        # Add the input fields to the form
        form_layout.addRow("Student:", self.student_input)
        form_layout.addRow("Course:", self.course_input)

        # Register button
        register_button = QPushButton("Register", self)
        register_button.clicked.connect(self.register_student)

        form_layout.addWidget(register_button)

        self.setLayout(form_layout)

    def register_student(self):
        student_name = self.student_input.currentText()  # Get the selected student name
        course_name = self.course_input.currentText()  # Get the selected course name
        
        student = self.student_map.get(student_name)  # Retrieve the Student object
        course = self.course_map.get(course_name)  # Retrieve the Course object

        if not student or not course:
            QMessageBox.warning(self, "Input Error", "Please select a student and a course.")
        else:
            try:
                # Register the student for the selected course
                enroll_student_in_course(student[0], course[0])
                
                QMessageBox.information(self, "Success", f"Student {student_name} registered for course {course_name} successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))



class InstructorForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Instructor")
        self.setGeometry(200, 200, 400, 300)

        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        # self.instructor_id_input = QLineEdit(self)

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Email:", self.email_input)
        # form_layout.addRow("Instructor ID:", self.instructor_id_input)

        add_button = QPushButton("Add Instructor", self)
        add_button.clicked.connect(self.add_instructor)

        form_layout.addWidget(add_button)

        self.setLayout(form_layout)

    def add_instructor(self):
        name = self.name_input.text()
        age = int(self.age_input.text())
        email = self.email_input.text()
        # instructor_id = self.instructor_id_input.text()

        if not name or not age or not email:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
        else:
            try:
                # new_instructor = Instructor(name, age, email, instructor_id)
                # instructors.append(new_instructor)
                create_instructor(name, age, email)
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))
                return
            # Here you would handle adding the instructor
            QMessageBox.information(self, "Success", f"Instructor {name} added successfully!")

class StudentEditForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Student")
        self.setGeometry(200, 200, 300, 200)
        layout = QFormLayout(self)

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        # self.student_id_input = QLineEdit(self)

        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Email:", self.email_input)
        # layout.addRow("Student ID:", self.student_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)



class InstructorAssignmentForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Assign Instructor to Course")
        self.setGeometry(200, 200, 400, 300)

        instructors = get_all_instructors()
        courses = get_all_courses()

        form_layout = QFormLayout()

        # ComboBox for selecting instructor
        self.instructor_input = QComboBox(self)
        # Dictionary to map instructor names to Instructor objects
        self.instructor_map = {}

        # Populate ComboBox with instructor names and map them to the actual Instructor objects
        instructors = get_all_instructors()
        if instructors:
            for instructor in instructors:
                self.instructor_input.addItem(instructor[1])  # Add instructor name to combo box
                self.instructor_map[instructor[1]] = instructor  # Map the name to the Instructor object

        # ComboBox for selecting course
        self.course_input = QComboBox(self)
        # Dictionary to map course names to Course objects
        self.course_map = {}

        # Populate ComboBox with course names and map them to the actual Course objects
        if courses:
            for course in courses:
                self.course_input.addItem(course[1])  # Add course name to combo box
                self.course_map[course[1]] = course  # Map the name to the Course object

        # Add the input fields to the form
        form_layout.addRow("Instructor:", self.instructor_input)
        form_layout.addRow("Course:", self.course_input)

        # Assign button
        assign_button = QPushButton("Assign", self)
        assign_button.clicked.connect(self.assign_instructor)

        form_layout.addWidget(assign_button)

        self.setLayout(form_layout)

    def assign_instructor(self):
        instructor_name = self.instructor_input.currentText()  # Get the selected instructor name
        course_name = self.course_input.currentText()  # Get the selected course name

        instructor = self.instructor_map.get(instructor_name)  # Retrieve the Instructor object
        course = self.course_map.get(course_name)  # Retrieve the Course object

        if not instructor or not course:
            QMessageBox.warning(self, "Input Error", "Please select an instructor and a course.")
        else:
            try:
                # Assign the instructor to the selected course
                update_course(course[0], course[1], instructor[0])
                QMessageBox.information(self, "Success", f"Instructor {instructor_name} assigned to course {course_name} successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))
                return

class InstructorEditForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Instructor")
        self.setGeometry(200, 200, 300, 200)
        layout = QFormLayout(self)
        

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        # self.instructor_id_input = QLineEdit(self)

        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Email:", self.email_input)
        # layout.addRow("Instructor ID:", self.instructor_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)


class CourseForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Course")
        self.setGeometry(200, 200, 400, 300)

        form_layout = QFormLayout()

        # Inputs for Course ID and Course Name
        # self.course_id_input = QLineEdit(self)
        self.course_name_input = QLineEdit(self)

        # ComboBox for selecting instructor
        self.instructor_input = QComboBox(self)
        self.instructor_map = {}
        
        # Set instructor choices from provided instructors_list
        if instructors:
            for instructor in instructors:
                self.instructor_input.addItem(instructor[1])
                self.instructor_map[instructor[1]] = instructor

        # Add the input fields to the form
        # form_layout.addRow("Course ID:", self.course_id_input)
        form_layout.addRow("Course Name:", self.course_name_input)
        form_layout.addRow("Instructor:", self.instructor_input)

        # Add Course button
        add_button = QPushButton("Add Course", self)
        add_button.clicked.connect(self.add_course)

        form_layout.addWidget(add_button)

        self.setLayout(form_layout)

    def add_course(self):
        # course_id = self.course_id_input.text()
        course_name = self.course_name_input.text()
        instructor_name = self.instructor_input.currentText()
        instructor = self.instructor_map.get(instructor_name)

        if not course_name or not instructor:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
        else:
            try:
                create_course(course_name, instructor[0])
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))
                return
            # Success message
            QMessageBox.information(self, "Success", f"Course {course_name} added successfully!")

class CourseEditForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Course")
        self.setGeometry(200, 200, 300, 200)
        layout = QFormLayout(self)

        courses = get_all_courses()

        self.course_id_input = QLineEdit(self)
        self.course_name_input = QLineEdit(self)
        self.instructor_input = QLineEdit(self)

        layout.addRow("Course ID:", self.course_id_input)
        layout.addRow("Course Name:", self.course_name_input)
        layout.addRow("Instructor:", self.instructor_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)


class DisplayAllRecords(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Display All Records")
        self.setGeometry(200, 200, 800, 600)

        students = get_all_students()
        instructors = get_all_instructors()
        courses = get_all_courses()

        layout = QVBoxLayout(self)

        # Create tab widget
        self.tabs = QTabWidget(self)
        
        # Create a search layout
        search_layout = QFormLayout()

        # Search fields
        self.student_search_input = QLineEdit(self)
        self.instructor_search_input = QLineEdit(self)
        self.course_search_input = QLineEdit(self)

        search_layout.addRow("Search Students:", self.student_search_input)
        search_layout.addRow("Search Instructors:", self.instructor_search_input)
        search_layout.addRow("Search Courses:", self.course_search_input)

        # Add search layout to main layout
        layout.addLayout(search_layout)

        # Create tables
        self.student_table = QTableWidget()
        self.instructor_table = QTableWidget()
        self.course_table = QTableWidget()

        self.tabs.addTab(self.student_table, "Students")
        self.tabs.addTab(self.instructor_table, "Instructors")
        self.tabs.addTab(self.course_table, "Courses")

        layout.addWidget(self.tabs)

        # Add close button
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        # Add buttons for edit and delete
        self.edit_button = QPushButton("Edit", self)
        self.delete_button = QPushButton("Delete", self)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        # Set up the tables
        self.setup_tables()

        # Connect search inputs to update tables
        self.student_search_input.textChanged.connect(self.update_student_table)
        self.instructor_search_input.textChanged.connect(self.update_instructor_table)
        self.course_search_input.textChanged.connect(self.update_course_table)

        # Connect edit and delete buttons
        self.edit_button.clicked.connect(self.edit_record)
        self.delete_button.clicked.connect(self.delete_record)

        # Keep track of selected row
        self.selected_row = None
        self.current_table = None

        # Connect table selection changes
        self.student_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.student_table))
        self.instructor_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.instructor_table))
        self.course_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.course_table))

    def setup_tables(self):
        # Setup Students table
        self.student_table.setColumnCount(5)
        self.student_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Student ID", "Courses"])

        # Setup Instructors table
        self.instructor_table.setColumnCount(5)
        self.instructor_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Instructor ID", "Courses"])

        # Setup Courses table
        self.course_table.setColumnCount(4)
        self.course_table.setHorizontalHeaderLabels(["Course ID", "Course Name", "Instructor", "Enrolled Students"])

        # Initial population of tables
        self.update_student_table()
        self.update_instructor_table()
        self.update_course_table()

    def get_students_with_courses(self):
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT students.student_id, students.name, students.age, students.email, 
                    array_agg(courses.course_name) as registered_courses
                FROM students
                LEFT JOIN enrollments ON students.student_id = enrollments.student_id
                LEFT JOIN courses ON enrollments.course_id = courses.course_id
                GROUP BY students.student_id;
            """)
            students = cursor.fetchall()
            return students
        except Exception as e:
            print(f"Error retrieving students: {e}")
        finally:
            cursor.close()
            conn.close()



    def update_student_table(self):
        search_text = self.student_search_input.text().lower()
        students = self.get_students_with_courses() 
        
        # Set the number of rows in the table
        self.student_table.setRowCount(len(students))

        if not search_text:
            # Display all students
            for row, student in enumerate(students):
                self.student_table.setItem(row, 0, QTableWidgetItem(student[1]))  # Name
                self.student_table.setItem(row, 1, QTableWidgetItem(str(student[2])))  # Age
                self.student_table.setItem(row, 2, QTableWidgetItem(student[3]))  # Email
                self.student_table.setItem(row, 3, QTableWidgetItem(str(student[0])))  # Student ID
                self.student_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in student[4])))  # Registered Courses
                self.student_table.setRowHidden(row, False)
        else:
            # Filter and display based on search text
            for row, student in enumerate(students):
                if search_text in str(student[1]).lower() or search_text == str(student[0]):  # Check in name or student_id
                    self.student_table.setItem(row, 0, QTableWidgetItem(student[1]))  # Name
                    self.student_table.setItem(row, 1, QTableWidgetItem(str(student[2])))  # Age
                    self.student_table.setItem(row, 2, QTableWidgetItem(student[3]))  # Email
                    self.student_table.setItem(row, 3, QTableWidgetItem(str(student[0])))  # Student ID
                    self.student_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in student[4])))  # Registered Courses
                    self.student_table.setRowHidden(row, False)
                else:
                    self.student_table.setRowHidden(row, True)


    def get_instructors_with_courses(self):
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT instructors.instructor_id, instructors.name, instructors.age, instructors.email, 
                    array_agg(courses.course_name) as assigned_courses
                FROM instructors
                LEFT JOIN courses ON instructors.instructor_id = courses.instructor_id
                GROUP BY instructors.instructor_id;
            """)
            instructors = cursor.fetchall()
            return instructors
        except Exception as e:
            print(f"Error retrieving instructors: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_instructor_table(self):
        search_text = self.instructor_search_input.text().lower()
        instructors = self.get_instructors_with_courses()  # Retrieve instructors with their courses
        
        # Set the number of rows in the table
        self.instructor_table.setRowCount(len(instructors))
        
        if not search_text:
            # Display all instructors
            for row, instructor in enumerate(instructors):
                self.instructor_table.setItem(row, 0, QTableWidgetItem(instructor[1]))  # Name
                self.instructor_table.setItem(row, 1, QTableWidgetItem(str(instructor[2])))  # Age
                self.instructor_table.setItem(row, 2, QTableWidgetItem(instructor[3]))  # Email
                self.instructor_table.setItem(row, 3, QTableWidgetItem(str(instructor[0])))  # Instructor ID
                self.instructor_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in instructor[4])))  # Assigned Courses
                self.instructor_table.setRowHidden(row, False)
        else:
            # Filter and display based on search text
            for row, instructor in enumerate(instructors):
                if search_text in instructor[1].lower() or search_text in str(instructor[0]):  # Check in name or instructor_id
                    self.instructor_table.setItem(row, 0, QTableWidgetItem(str(instructor[1])))  # Name
                    self.instructor_table.setItem(row, 1, QTableWidgetItem(str(instructor[2])))  # Age
                    self.instructor_table.setItem(row, 2, QTableWidgetItem(instructor[3]))  # Email
                    self.instructor_table.setItem(row, 3, QTableWidgetItem(str(instructor[0])))  # Instructor ID
                    self.instructor_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in instructor[4])))  # Assigned Courses
                    self.instructor_table.setRowHidden(row, False)
                else:
                    self.instructor_table.setRowHidden(row, True)


    def get_courses_with_details(self):
        conn =connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT courses.course_id, courses.course_name, instructors.name as instructor_name,
                    array_agg(students.name) as enrolled_students
                FROM courses
                LEFT JOIN instructors ON courses.instructor_id = instructors.instructor_id
                LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
                LEFT JOIN students ON enrollments.student_id = students.student_id
                GROUP BY courses.course_id, instructors.name;
            """)
            courses = cursor.fetchall()
            return courses
        except Exception as e:
            print(f"Error retrieving courses: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_course_table(self):
        search_text = self.course_search_input.text().lower()
        courses = self.get_courses_with_details()  # Retrieve courses with details
        
        # Set the number of rows in the table
        self.course_table.setRowCount(len(courses))
        
        if not search_text:
            # Display all courses
            for row, course in enumerate(courses):
                self.course_table.setItem(row, 0, QTableWidgetItem(str(course[0])))  # Course ID
                self.course_table.setItem(row, 1, QTableWidgetItem(course[1]))  # Course Name
                self.course_table.setItem(row, 2, QTableWidgetItem(course[2] if course[2] else "No Instructor"))  # Instructor
                self.course_table.setItem(row, 3, QTableWidgetItem(", ".join(str(student) for student in course[3])))  # Enrolled Students
                self.course_table.setRowHidden(row, False)
        else:
            # Filter and display based on search text
            for row, course in enumerate(courses):
                if search_text in course[1].lower() or search_text in str(course[0]):  # Check in course_name or course_id
                    self.course_table.setItem(row, 0, QTableWidgetItem(str(course[0])))  # Course ID
                    self.course_table.setItem(row, 1, QTableWidgetItem(course[1]))  # Course Name
                    self.course_table.setItem(row, 2, QTableWidgetItem(course[2] if course[2] else "No Instructor"))  # Instructor
                    self.course_table.setItem(row, 3, QTableWidgetItem(", ".join(str(student) for student in course[3])))  # Enrolled Students
                    self.course_table.setRowHidden(row, False)
                else:
                    self.course_table.setRowHidden(row, True)



    def update_selected_row(self, table):
        selected_items = table.selectedItems()
        if selected_items:
            self.selected_row = selected_items[0].row()
            self.current_table = table
        else:
            self.selected_row = None

    def edit_record(self):
        if self.selected_row is not None and self.current_table is not None:
            if self.current_table == self.student_table:
                student = students[self.selected_row]
                form = StudentEditForm(self)
                form.name_input.setText(student[1])
                form.age_input.setText(str(student[2]))
                form.email_input.setText(student[3])
                # form.student_id_input.setText(student[0])
                if form.exec_() == QDialog.Accepted:
                    update_student(student[0], form.name_input.text(), int(form.age_input.text()), form.email_input.text())
                    # student.student_id = form.student_id_input.text()
                    self.update_student_table()
            elif self.current_table == self.instructor_table:
                instructor = instructors[self.selected_row]
                form = InstructorEditForm(self)
                form.name_input.setText(instructor[1])
                form.age_input.setText(str(instructor[2]))
                form.email_input.setText(instructor[3])
                # form.instructor_id_input.setText(instructor.instructor_id)
                if form.exec_() == QDialog.Accepted:
                    update_instructor(instructor[0], form.name_input.text(), int(form.age_input.text()), form.email_input.text())
                    # instructor.instructor_id = form.instructor_id_input.text()
                    self.update_instructor_table()
            elif self.current_table == self.course_table:
                course = courses[self.selected_row]
                form = CourseEditForm(self)
                form.course_id_input.setText(course.course_id)
                form.course_name_input.setText(course.course_name)
                form.instructor_input.setText(course.instructor.name if course.instructor else "No Instructor")
                if form.exec_() == QDialog.Accepted:
                    course.course_id = form.course_id_input.text()
                    course.course_name = form.course_name_input.text()
                    # Update course instructor if necessary
                    self.update_course_table()


    def delete_record(self):
        if self.selected_row is not None and self.current_table is not None:
            # Determine which table is currently selected
            if self.current_table == self.student_table:
                student_id = self.current_table.item(self.selected_row, 3).text()  # Assuming student_id is in column 3
                delete_student(student_id)  # Call SQL function to delete student
                self.update_student_table()  # Refresh the table

            elif self.current_table == self.instructor_table:
                instructor_id = self.current_table.item(self.selected_row, 3).text()  # Assuming instructor_id is in column 3
                delete_instructor(instructor_id)  # Call SQL function to delete instructor
                self.update_instructor_table()  # Refresh the table

            elif self.current_table == self.course_table:
                course_id = self.current_table.item(self.selected_row, 0).text()  # Assuming course_id is in column 0
                delete_course(course_id)  # Call SQL function to delete course
                self.update_course_table()  # Refresh the table

            # Reset selection
            self.selected_row = None
            self.current_table.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create an instance of the main window
    window = SchoolManagementSystem()

    # Show the window
    window.show()

    # Execute the application
    sys.exit(app.exec_())
