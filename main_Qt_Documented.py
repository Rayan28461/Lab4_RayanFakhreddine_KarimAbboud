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


student1 = Student("Smith", 15, "test@gmail.com", "2000")
student2 = Student("Doe", 20, "anything@mail.test", "2001")

instructor1 = Instructor("John", 25, "what@test.com", "1000")
instructor2 = Instructor("Jane", 30, "test@test.com", "1001")

course1 = Course("CSC101", "Introduction to Computer Science", instructor1)
course2 = Course("CSC102", "Introduction to Programming", instructor1)


students = [student1,student2]
instructors = [instructor1, instructor2]
courses = [course1, course2]


class SchoolManagementSystem(QMainWindow):
    """
    A GUI-based School Management System built using PyQt. This class provides functionalities for managing
    students, instructors, and courses through different forms and also supports saving, loading, and exporting data.

    Inherits:
        QMainWindow: The main window widget provided by PyQt.

    Methods:
        __init__(): Initializes the School Management System's main window, setting up buttons and layout for the UI.
        
        open_student_form(): Opens the form to add or edit student details.
        
        open_student_registration_form(): Opens the form to register students in courses.
        
        open_instructor_form(): Opens the form to add or edit instructor details.
        
        open_instructor_assignment_form(): Opens the form to assign instructors to courses.
        
        open_course_form(): Opens the form to add or edit course details.
        
        open_display_all_records(): Opens a window that displays all student, instructor, and course records.
        
        display_statistics(): Calculates and displays statistics about the total number of students, instructors, and courses.
        
        save_data(): Saves the student, instructor, and course data to respective files.
        
        load_data(): Loads student, instructor, and course data from respective files.
        
        export_students_to_csv(): Exports student data to a CSV file.
        
        export_instructors_to_csv(): Exports instructor data to a CSV file.
        
        export_courses_to_csv(): Exports course data to a CSV file.
    """

    def __init__(self):
        """
        Initializes the School Management System's main window, creates the layout, and adds buttons for:
        - Opening forms to manage students, instructors, and courses.
        - Registering students to courses.
        - Assigning instructors to courses.
        - Saving and loading data.
        - Exporting data to CSV.
        """
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(100, 100, 800, 200)

        # Main layout and central widget setup
        central_widget = QWidget(self)
        layout = QVBoxLayout()

        # Welcome Label
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

        save_button = QPushButton("Save Data")
        save_button.clicked.connect(self.save_data)

        load_button = QPushButton("Load Data")
        load_button.clicked.connect(self.load_data)

        data_layout.addWidget(display_records_button)
        data_layout.addWidget(save_button)
        data_layout.addWidget(load_button)

        # Group 3: Export Data
        export_layout = QHBoxLayout()
        export_students_button = QPushButton("Export Students to CSV")
        export_students_button.clicked.connect(self.export_students_to_csv)

        export_instructors_button = QPushButton("Export Instructors to CSV")
        export_instructors_button.clicked.connect(self.export_instructors_to_csv)

        export_courses_button = QPushButton("Export Courses to CSV")
        export_courses_button.clicked.connect(self.export_courses_to_csv)

        export_layout.addWidget(export_students_button)
        export_layout.addWidget(export_instructors_button)
        export_layout.addWidget(export_courses_button)

        # Add all layouts to the main layout
        layout.addLayout(form_layout)
        layout.addLayout(data_layout)
        layout.addLayout(export_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_student_form(self):
        """
        Opens the form for adding or editing student information.
        """
        form = StudentForm(self)
        form.exec_()

    def open_student_registration_form(self):
        """
        Opens the form to register a student for a course.
        """
        form = StudentRegistrationForm(self)
        form.exec_()

    def open_instructor_form(self):
        """
        Opens the form for adding or editing instructor information.
        """
        form = InstructorForm(self)
        form.exec_()

    def open_instructor_assignment_form(self):
        """
        Opens the form to assign an instructor to a course.
        """
        form = InstructorAssignmentForm(self)
        form.exec_()

    def open_course_form(self):
        """
        Opens the form for adding or editing course information.
        """
        form = CourseForm(self)
        form.exec_()

    def open_display_all_records(self):
        """
        Opens a dialog that displays all student, instructor, and course records.
        """
        form = DisplayAllRecords(self)
        form.exec_()

    def display_statistics(self):
        """
        Displays the total number of students, instructors, and courses in a message box.
        """
        # Calculate statistics
        num_students = len(students)
        num_instructors = len(instructors)
        num_courses = len(courses)

        # Display a message box with the statistics
        QMessageBox.information(self, "Statistics", f"Total Students: {num_students}\n"
                                                    f"Total Instructors: {num_instructors}\n"
                                                    f"Total Courses: {num_courses}")

    def save_data(self):
        """
        Saves the current student, instructor, and course data to files. Displays a success message on completion.
        """
        save_students_to_file(students)
        save_instructors_to_file(instructors)
        save_courses_to_file(courses)
        QMessageBox.information(self, "Success", "Data saved successfully!")

    def load_data(self):
        """
        Loads student, instructor, and course data from files. Displays a success message on completion.
        """
        global students, instructors, courses
        students = load_students_from_file()
        instructors = load_instructors_from_file()
        courses = load_courses_from_file()
        QMessageBox.information(self, "Success", "Data loaded successfully!")

    def export_students_to_csv(self):
        """
        Exports student data to a CSV file. Displays a success message on completion.
        """
        export_students_to_csv(students)
        QMessageBox.information(self, "Success", "Students data exported to CSV successfully!")

    def export_instructors_to_csv(self):
        """
        Exports instructor data to a CSV file. Displays a success message on completion.
        """
        export_instructors_to_csv(instructors)
        QMessageBox.information(self, "Success", "Instructors data exported to CSV successfully!")

    def export_courses_to_csv(self):
        """
        Exports course data to a CSV file. Displays a success message on completion.
        """
        export_courses_to_csv(courses)
        QMessageBox.information(self, "Success", "Courses data exported to CSV successfully!")

        


class StudentForm(QDialog):
    """
    A dialog form for adding a new student. The form allows users to input student details such as 
    name, age, email, and student ID. Once the data is entered, it can be added to the application.

    Attributes:
        name_input (QLineEdit): Input field for the student's name.
        age_input (QLineEdit): Input field for the student's age.
        email_input (QLineEdit): Input field for the student's email address.
        student_id_input (QLineEdit): Input field for the student's ID.
    
    Methods:
        add_student(): Collects data from the input fields, validates it, and adds a new student 
                       to the list if the input is valid.
    """

    def __init__(self, parent=None):
        """
        Initializes the StudentForm dialog, setting up the form layout and input fields 
        for student details, including name, age, email, and student ID. 
        Also adds a button to submit the form.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Add Student")
        self.setGeometry(200, 200, 400, 300)

        # Create and configure the form layout with input fields
        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.student_id_input = QLineEdit(self)

        # Add input fields to the layout
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Student ID:", self.student_id_input)

        # Add submit button to the layout
        add_button = QPushButton("Add Student", self)
        add_button.clicked.connect(self.add_student)

        # Add button to the layout
        form_layout.addWidget(add_button)

        # Set the layout for the dialog
        self.setLayout(form_layout)

    def add_student(self):
        """
        Collects input data from the form fields, validates the data, and creates a new Student 
        object. If any field is left empty or an error occurs during student creation, an error 
        message is shown.

        If all inputs are valid, the new student is added to the `students` list and a success 
        message is displayed.

        Raises:
            ValueError: If the age field contains non-numeric input, or other invalid data is provided.
        """
        name = self.name_input.text()
        age = int(self.age_input.text())
        email = self.email_input.text()
        student_id = self.student_id_input.text()

        # Validate that all fields are filled
        if not name or not age or not email or not student_id:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
        else:
            try:
                # Attempt to create a new Student object
                new_student = Student(name, age, email, student_id)
                students.append(new_student)
            except ValueError as e:
                # Show a warning if there is a problem with the input
                QMessageBox.warning(self, "Input Error", str(e))
                return

            # Display success message
            QMessageBox.information(self, "Success", f"Student {name} added successfully!")

class StudentRegistrationForm(QDialog):
    """
    A dialog form for registering a student for a course. The form allows users to select a 
    student and a course from dropdown menus (ComboBoxes) and register the student for the selected course.

    Attributes:
        student_input (QComboBox): A dropdown menu for selecting a student.
        student_map (dict): A dictionary mapping student names to their respective Student objects.
        course_input (QComboBox): A dropdown menu for selecting a course.
        course_map (dict): A dictionary mapping course names to their respective Course objects.

    Methods:
        register_student(): Handles the registration process by associating a selected student with a course.
    """

    def __init__(self, parent=None):
        """
        Initializes the StudentRegistrationForm dialog. The form consists of two ComboBoxes 
        (one for students and one for courses) and a button to register the selected student 
        for the selected course.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Register Student for Course")
        self.setGeometry(200, 200, 400, 300)

        # Create the form layout
        form_layout = QFormLayout()

        # ComboBox for selecting student
        self.student_input = QComboBox(self)
        self.student_map = {}  # Map student names to their Student objects

        # Populate ComboBox with student names and map them to Student objects
        if students:
            for student in students:
                self.student_input.addItem(student.name)  # Add student names to ComboBox
                self.student_map[student.name] = student  # Map the student name to the actual Student object

        # ComboBox for selecting course
        self.course_input = QComboBox(self)
        self.course_map = {}  # Map course names to their Course objects

        # Populate ComboBox with course names and map them to Course objects
        if courses:
            for course in courses:
                self.course_input.addItem(course.course_name)  # Add course names to ComboBox
                self.course_map[course.course_name] = course  # Map the course name to the actual Course object

        # Add the input fields to the form layout
        form_layout.addRow("Student:", self.student_input)
        form_layout.addRow("Course:", self.course_input)

        # Register button to submit the form
        register_button = QPushButton("Register", self)
        register_button.clicked.connect(self.register_student)

        # Add the register button to the form layout
        form_layout.addWidget(register_button)

        # Set the layout for the dialog
        self.setLayout(form_layout)

    def register_student(self):
        """
        Handles the registration process for a student in a course. The method retrieves the 
        selected student and course from their respective ComboBoxes, and registers the student 
        for the course by calling methods on both the Student and Course objects.

        If either a student or course is not selected, an error message is displayed.

        Raises:
            ValueError: If an issue occurs during the registration process, such as invalid input or failed registration.
        """
        # Get the selected student and course names from the ComboBoxes
        student_name = self.student_input.currentText()
        course_name = self.course_input.currentText()

        # Retrieve the Student and Course objects from their respective maps
        student = self.student_map.get(student_name)
        course = self.course_map.get(course_name)

        # Check if both student and course are selected
        if not student or not course:
            QMessageBox.warning(self, "Input Error", "Please select a student and a course.")
        else:
            try:
                # Register the student for the selected course
                student.register_course(course)
                course.add_student(student)

                # Display success message
                QMessageBox.information(self, "Success", f"Student {student_name} registered for course {course_name} successfully!")
            except ValueError as e:
                # Display error message in case of a registration issue
                QMessageBox.warning(self, "Input Error", str(e))


class InstructorForm(QDialog):
    """
    A dialog form for adding a new instructor. The form allows users to input instructor details 
    such as name, age, email, and instructor ID. Once the data is entered, it can be added to the application.

    Attributes:
        name_input (QLineEdit): Input field for the instructor's name.
        age_input (QLineEdit): Input field for the instructor's age.
        email_input (QLineEdit): Input field for the instructor's email address.
        instructor_id_input (QLineEdit): Input field for the instructor's ID.
    
    Methods:
        add_instructor(): Collects data from the input fields, validates it, and adds a new instructor 
                          to the list if the input is valid.
    """

    def __init__(self, parent=None):
        """
        Initializes the InstructorForm dialog, setting up the form layout and input fields 
        for instructor details, including name, age, email, and instructor ID.
        Also adds a button to submit the form.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Add Instructor")
        self.setGeometry(200, 200, 400, 300)

        # Create and configure the form layout with input fields
        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.instructor_id_input = QLineEdit(self)

        # Add input fields to the layout
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Instructor ID:", self.instructor_id_input)

        # Add submit button to the layout
        add_button = QPushButton("Add Instructor", self)
        add_button.clicked.connect(self.add_instructor)

        # Add button to the layout
        form_layout.addWidget(add_button)

        # Set the layout for the dialog
        self.setLayout(form_layout)

    def add_instructor(self):
        """
        Collects input data from the form fields, validates the data, and creates a new Instructor 
        object. If any field is left empty or an error occurs during instructor creation, an error 
        message is shown.

        If all inputs are valid, the new instructor is added to the `instructors` list and a success 
        message is displayed.

        Raises:
            ValueError: If the age field contains non-numeric input, or other invalid data is provided.
        """
        # Retrieve the values from the input fields
        name = self.name_input.text()
        age = int(self.age_input.text())
        email = self.email_input.text()
        instructor_id = self.instructor_id_input.text()

        # Validate that all fields are filled
        if not name or not age or not email or not instructor_id:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
        else:
            try:
                # Attempt to create a new Instructor object
                new_instructor = Instructor(name, age, email, instructor_id)
                instructors.append(new_instructor)
            except ValueError as e:
                # Show a warning if there is a problem with the input
                QMessageBox.warning(self, "Input Error", str(e))
                return

            # Display success message
            QMessageBox.information(self, "Success", f"Instructor {name} added successfully!")

class StudentEditForm(QDialog):
    """
    A dialog form for editing an existing student's information. The form allows users to modify
    details such as the student's name, age, email, and student ID.

    Attributes:
        name_input (QLineEdit): Input field for the student's name.
        age_input (QLineEdit): Input field for the student's age.
        email_input (QLineEdit): Input field for the student's email address.
        student_id_input (QLineEdit): Input field for the student's ID.
    
    Methods:
        accept(): Called when the user accepts the changes (via the "OK" button).
        reject(): Called when the user cancels the operation (via the "Cancel" button).
    """

    def __init__(self, parent=None):
        """
        Initializes the StudentEditForm dialog, setting up the form layout with input fields 
        for editing the student's name, age, email, and student ID. The dialog also includes 
        "OK" and "Cancel" buttons.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Edit Student")
        self.setGeometry(200, 200, 300, 200)

        # Create the form layout with input fields
        layout = QFormLayout(self)

        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.student_id_input = QLineEdit(self)

        # Add input fields to the layout
        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Student ID:", self.student_id_input)

        # Add "OK" and "Cancel" buttons to the form
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)  # Connect OK button to accept method
        buttons.rejected.connect(self.reject)  # Connect Cancel button to reject method
        layout.addWidget(buttons)

        # Set the layout for the dialog
        self.setLayout(layout)



class InstructorAssignmentForm(QDialog):
    """
    A dialog form for assigning an instructor to a course. The form allows users to select an 
    instructor and a course from drop-down lists (ComboBoxes) and assign the instructor to the course.

    Attributes:
        instructor_input (QComboBox): Drop-down list for selecting an instructor.
        instructor_map (dict): A mapping of instructor names to Instructor objects.
        course_input (QComboBox): Drop-down list for selecting a course.
        course_map (dict): A mapping of course names to Course objects.
    
    Methods:
        assign_instructor(): Handles the assignment of the selected instructor to the selected course, 
                             and displays success or error messages based on input validation.
    """

    def __init__(self, parent=None):
        """
        Initializes the InstructorAssignmentForm dialog, setting up input fields for selecting an instructor 
        and a course. Populates the ComboBox widgets with available instructors and courses. Provides 
        an "Assign" button to complete the assignment.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Assign Instructor to Course")
        self.setGeometry(200, 200, 400, 300)

        # Form layout for the input fields
        form_layout = QFormLayout()

        # ComboBox for selecting an instructor
        self.instructor_input = QComboBox(self)
        # Dictionary to map instructor names to Instructor objects
        self.instructor_map = {}

        # Populate ComboBox with instructor names and map them to Instructor objects
        if instructors:
            for instructor in instructors:
                self.instructor_input.addItem(instructor.name)  # Add instructor name to ComboBox
                self.instructor_map[instructor.name] = instructor  # Map the name to the Instructor object

        # ComboBox for selecting a course
        self.course_input = QComboBox(self)
        # Dictionary to map course names to Course objects
        self.course_map = {}

        # Populate ComboBox with course names and map them to Course objects
        if courses:
            for course in courses:
                self.course_input.addItem(course.course_name)  # Add course name to ComboBox
                self.course_map[course.course_name] = course  # Map the name to the Course object

        # Add input fields to the form layout
        form_layout.addRow("Instructor:", self.instructor_input)
        form_layout.addRow("Course:", self.course_input)

        # Button to assign instructor to course
        assign_button = QPushButton("Assign", self)
        assign_button.clicked.connect(self.assign_instructor)

        # Add button to form layout
        form_layout.addWidget(assign_button)

        # Set the layout for the dialog
        self.setLayout(form_layout)

    def assign_instructor(self):
        """
        Assigns the selected instructor to the selected course. If the user doesn't select a valid 
        instructor or course, an error message is displayed. Otherwise, the instructor is assigned 
        to the course, and a success message is shown.

        Raises:
            ValueError: If an error occurs during the assignment process (handled and displayed in a message box).
        """
        # Get selected instructor and course names
        instructor_name = self.instructor_input.currentText()
        course_name = self.course_input.currentText()

        # Retrieve the Instructor and Course objects from the mappings
        instructor = self.instructor_map.get(instructor_name)
        course = self.course_map.get(course_name)

        # Validate that both instructor and course are selected
        if not instructor or not course:
            QMessageBox.warning(self, "Input Error", "Please select an instructor and a course.")
        else:
            try:
                # Assign the instructor to the selected course
                course.assign_instructor(instructor)
                instructor.assign_course(course)
                
                # Display success message
                QMessageBox.information(self, "Success", f"Instructor {instructor_name} assigned to course {course_name} successfully!")
            except ValueError as e:
                # Handle and display any errors that occur during the assignment
                QMessageBox.warning(self, "Input Error", str(e))
                return

class InstructorEditForm(QDialog):
    """
    A dialog form for editing an instructor's details. The form allows users to update
    the instructor's name, age, email, and instructor ID.

    Attributes:
        name_input (QLineEdit): Input field for the instructor's name.
        age_input (QLineEdit): Input field for the instructor's age.
        email_input (QLineEdit): Input field for the instructor's email address.
        instructor_id_input (QLineEdit): Input field for the instructor's unique ID.
    
    Methods:
        None (handles form submission using the built-in accept and reject methods).
    """

    def __init__(self, parent=None):
        """
        Initializes the InstructorEditForm dialog, setting up input fields for editing the 
        instructor's name, age, email, and ID. Provides OK and Cancel buttons for submitting 
        or canceling the changes.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Edit Instructor")
        self.setGeometry(200, 200, 300, 200)
        
        # Create a layout for the form inputs
        layout = QFormLayout(self)

        # Input fields for instructor details
        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.instructor_id_input = QLineEdit(self)

        # Add input fields to the form layout
        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Instructor ID:", self.instructor_id_input)

        # Create dialog buttons for submission (OK) and cancellation (Cancel)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)  # Accept the form (submit)
        buttons.rejected.connect(self.reject)  # Reject the form (cancel)

        # Add buttons to the layout
        layout.addWidget(buttons)

        # Set the layout for the dialog
        self.setLayout(layout)


class CourseForm(QDialog):
    """
    A dialog form for adding a new course to the system. The form allows users to input
    a course ID, course name, and assign an instructor from a list of available instructors.

    Attributes:
        course_id_input (QLineEdit): Input field for the course's unique ID.
        course_name_input (QLineEdit): Input field for the course's name.
        instructor_input (QComboBox): Dropdown for selecting an instructor.
        instructor_map (dict): Dictionary mapping instructor names to Instructor objects.

    Methods:
        add_course(): Validates input and adds a new course to the list of courses.
    """

    def __init__(self, parent=None):
        """
        Initializes the CourseForm dialog, providing fields to enter the course ID, 
        course name, and select an instructor. Sets up the layout and connects the 
        "Add Course" button to the add_course method.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Add Course")
        self.setGeometry(200, 200, 400, 300)

        # Create form layout and input fields
        form_layout = QFormLayout()

        # Input fields for Course ID and Course Name
        self.course_id_input = QLineEdit(self)
        self.course_name_input = QLineEdit(self)

        # ComboBox for selecting an instructor
        self.instructor_input = QComboBox(self)
        self.instructor_map = {}

        # Populate ComboBox with instructors from a predefined list
        if instructors:
            for instructor in instructors:
                self.instructor_input.addItem(instructor.name)
                self.instructor_map[instructor.name] = instructor

        # Add input fields to the form layout
        form_layout.addRow("Course ID:", self.course_id_input)
        form_layout.addRow("Course Name:", self.course_name_input)
        form_layout.addRow("Instructor:", self.instructor_input)

        # Create and add "Add Course" button
        add_button = QPushButton("Add Course", self)
        add_button.clicked.connect(self.add_course)
        form_layout.addWidget(add_button)

        # Set the form layout
        self.setLayout(form_layout)

    def add_course(self):
        """
        Adds a new course to the system by retrieving the course ID, course name, 
        and selected instructor from the input fields. Validates that all fields 
        are filled, then creates a new Course object and appends it to the courses list.

        Displays a success message upon successful addition, or a warning if fields are missing or invalid.

        Raises:
            ValueError: If the provided inputs are invalid (e.g., non-unique course ID).
        """
        course_id = self.course_id_input.text()
        course_name = self.course_name_input.text()
        instructor_name = self.instructor_input.currentText()
        instructor = self.instructor_map.get(instructor_name)

        if not course_id or not course_name or not instructor:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
        else:
            try:
                new_course = Course(course_id, course_name, instructor)
                courses.append(new_course)
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", str(e))
                return

            # Display success message
            QMessageBox.information(self, "Success", f"Course {course_name} added successfully!")
class CourseEditForm(QDialog):
    """
    A dialog form for editing an existing course. Allows the user to modify the course ID, 
    course name, and instructor details.

    Attributes:
        course_id_input (QLineEdit): Input field for the course's unique ID.
        course_name_input (QLineEdit): Input field for the course's name.
        instructor_input (QLineEdit): Input field for the instructor's name.

    Methods:
        None (the form accepts or rejects user input via dialog buttons).
    """

    def __init__(self, parent=None):
        """
        Initializes the CourseEditForm dialog, providing fields to edit the course ID, 
        course name, and instructor. Sets up the layout and connects the dialog buttons 
        for accepting or rejecting the input.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Edit Course")
        self.setGeometry(200, 200, 300, 200)

        # Create form layout and input fields
        layout = QFormLayout(self)

        # Input fields for Course ID, Course Name, and Instructor
        self.course_id_input = QLineEdit(self)
        self.course_name_input = QLineEdit(self)
        self.instructor_input = QLineEdit(self)

        # Add input fields to the form layout
        layout.addRow("Course ID:", self.course_id_input)
        layout.addRow("Course Name:", self.course_name_input)
        layout.addRow("Instructor:", self.instructor_input)

        # Dialog buttons for OK and Cancel
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)  # OK button will accept and save changes
        buttons.rejected.connect(self.reject)  # Cancel button will reject changes
        layout.addWidget(buttons)

        # Set the form layout
        self.setLayout(layout)


class DisplayAllRecords(QDialog):
    """
    A dialog form for displaying and managing all records in the system, including students, instructors, 
    and courses. The form allows searching, editing, and deleting records.

    Attributes:
        tabs (QTabWidget): A tab widget to switch between Students, Instructors, and Courses tables.
        student_table (QTableWidget): A table to display student records.
        instructor_table (QTableWidget): A table to display instructor records.
        course_table (QTableWidget): A table to display course records.
        student_search_input (QLineEdit): Input field for searching students.
        instructor_search_input (QLineEdit): Input field for searching instructors.
        course_search_input (QLineEdit): Input field for searching courses.
        edit_button (QPushButton): Button for editing the selected record.
        delete_button (QPushButton): Button for deleting the selected record.
        selected_row (int): Index of the currently selected row in the table.
        current_table (QTableWidget): The currently selected table (students, instructors, or courses).

    Methods:
        setup_tables(): Initializes the tables and populates them with records.
        update_student_table(): Updates the student table based on the search query.
        update_instructor_table(): Updates the instructor table based on the search query.
        update_course_table(): Updates the course table based on the search query.
        update_selected_row(table): Updates the selected row index when a new row is selected in a table.
        edit_record(): Opens the edit dialog for the selected student, instructor, or course record.
        delete_record(): Deletes the selected student, instructor, or course record.
    """

    def __init__(self, parent=None):
        """
        Initializes the DisplayAllRecords dialog. Sets up the interface with search fields, tables for displaying 
        records, and buttons for editing and deleting records.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Display All Records")
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout(self)

        # Create a tab widget and search layout
        self.tabs = QTabWidget(self)
        search_layout = QFormLayout()

        # Input fields for searching Students, Instructors, and Courses
        self.student_search_input = QLineEdit(self)
        self.instructor_search_input = QLineEdit(self)
        self.course_search_input = QLineEdit(self)

        search_layout.addRow("Search Students:", self.student_search_input)
        search_layout.addRow("Search Instructors:", self.instructor_search_input)
        search_layout.addRow("Search Courses:", self.course_search_input)

        layout.addLayout(search_layout)

        # Create tables for Students, Instructors, and Courses
        self.student_table = QTableWidget()
        self.instructor_table = QTableWidget()
        self.course_table = QTableWidget()

        # Add tables to tabs
        self.tabs.addTab(self.student_table, "Students")
        self.tabs.addTab(self.instructor_table, "Instructors")
        self.tabs.addTab(self.course_table, "Courses")
        layout.addWidget(self.tabs)

        # Add Close button
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        # Add buttons for Edit and Delete actions
        self.edit_button = QPushButton("Edit", self)
        self.delete_button = QPushButton("Delete", self)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        # Setup the tables and their headers
        self.setup_tables()

        # Connect search inputs to their respective table update functions
        self.student_search_input.textChanged.connect(self.update_student_table)
        self.instructor_search_input.textChanged.connect(self.update_instructor_table)
        self.course_search_input.textChanged.connect(self.update_course_table)

        # Connect Edit and Delete buttons
        self.edit_button.clicked.connect(self.edit_record)
        self.delete_button.clicked.connect(self.delete_record)

        # Track the selected row and table
        self.selected_row = None
        self.current_table = None

        # Connect table row selection changes
        self.student_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.student_table))
        self.instructor_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.instructor_table))
        self.course_table.itemSelectionChanged.connect(lambda: self.update_selected_row(self.course_table))

    def setup_tables(self):
        """
        Sets up the student, instructor, and course tables with the appropriate number of columns and headers. 
        Populates the tables with existing data.
        """
        # Setup Students table
        self.student_table.setColumnCount(5)
        self.student_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Student ID", "Courses"])

        # Setup Instructors table
        self.instructor_table.setColumnCount(5)
        self.instructor_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Instructor ID", "Courses"])

        # Setup Courses table
        self.course_table.setColumnCount(4)
        self.course_table.setHorizontalHeaderLabels(["Course ID", "Course Name", "Instructor", "Enrolled Students"])

        # Populate the tables with data
        self.update_student_table()
        self.update_instructor_table()
        self.update_course_table()

    def update_student_table(self):
        """
        Updates the student table with data from the students list, filtered by the search query. 
        Shows only the rows that match the search criteria.
        """
        search_text = self.student_search_input.text().lower()
        self.student_table.setRowCount(len(students))

        for row, student in enumerate(students):
            match = search_text in student.name.lower() or search_text in student.student_id.lower()
            self.student_table.setItem(row, 0, QTableWidgetItem(student.name))
            self.student_table.setItem(row, 1, QTableWidgetItem(str(student.age)))
            self.student_table.setItem(row, 2, QTableWidgetItem(student._email))
            self.student_table.setItem(row, 3, QTableWidgetItem(student.student_id))
            self.student_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in student.registered_courses)))
            self.student_table.setRowHidden(row, not match)

    def update_instructor_table(self):
        """
        Updates the instructor table with data from the instructors list, filtered by the search query. 
        Shows only the rows that match the search criteria.
        """
        search_text = self.instructor_search_input.text().lower()
        self.instructor_table.setRowCount(len(instructors))

        for row, instructor in enumerate(instructors):
            match = search_text in instructor.name.lower() or search_text in instructor.instructor_id.lower()
            self.instructor_table.setItem(row, 0, QTableWidgetItem(instructor.name))
            self.instructor_table.setItem(row, 1, QTableWidgetItem(str(instructor.age)))
            self.instructor_table.setItem(row, 2, QTableWidgetItem(instructor._email))
            self.instructor_table.setItem(row, 3, QTableWidgetItem(instructor.instructor_id))
            self.instructor_table.setItem(row, 4, QTableWidgetItem(", ".join(str(course) for course in instructor.assigned_courses)))
            self.instructor_table.setRowHidden(row, not match)

    def update_course_table(self):
        """
        Updates the course table with data from the courses list, filtered by the search query. 
        Shows only the rows that match the search criteria.
        """
        search_text = self.course_search_input.text().lower()
        self.course_table.setRowCount(len(courses))

        for row, course in enumerate(courses):
            match = search_text in course.course_name.lower() or search_text in course.course_id.lower()
            self.course_table.setItem(row, 0, QTableWidgetItem(course.course_id))
            self.course_table.setItem(row, 1, QTableWidgetItem(course.course_name))
            self.course_table.setItem(row, 2, QTableWidgetItem(course.instructor.name if course.instructor else "No Instructor"))
            self.course_table.setItem(row, 3, QTableWidgetItem(", ".join(str(student) for student in course.enrolled_students)))
            self.course_table.setRowHidden(row, not match)

    def update_selected_row(self, table):
        """
        Updates the selected_row attribute when a row in any table is selected.

        Args:
            table (QTableWidget): The table where the row was selected.
        """
        selected_items = table.selectedItems()
        if selected_items:
            self.selected_row = selected_items[0].row()
            self.current_table = table
        else:
            self.selected_row = None

    def edit_record(self):
        """
        Opens the edit dialog for the selected student, instructor, or course record based on the currently selected 
        row and table. Updates the corresponding data upon dialog acceptance.
        """
        if self.selected_row is not None and self.current_table is not None:
            if self.current_table == self.student_table:
                student = students[self.selected_row]
                form = StudentEditForm(self)
                form.name_input.setText(student.name)
                form.age_input.setText(str(student.age))
                form.email_input.setText(student._email)
                form.student_id_input.setText(student.student_id)
                if form.exec_() == QDialog.Accepted:
                    student.name = form.name_input.text()
                    student.age = int(form.age_input.text())
                    student._email = form.email_input.text()
                    student.student_id = form.student_id_input.text()
                    self.update_student_table()
            elif self.current_table == self.instructor_table:
                instructor = instructors[self.selected_row]
                form = InstructorEditForm(self)
                form.name_input.setText(instructor.name)
                form.age_input.setText(str(instructor.age))
                form.email_input.setText(instructor._email)
                form.instructor_id_input.setText(instructor.instructor_id)
                if form.exec_() == QDialog.Accepted:
                    instructor.name = form.name_input.text()
                    instructor.age = int(form.age_input.text())
                    instructor._email = form.email_input.text()
                    instructor.instructor_id = form.instructor_id_input.text()
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
                    self.update_course_table()

    def delete_record(self):
        """
        Deletes the selected student, instructor, or course record based on the currently selected row and table. 
        Updates the corresponding table after deletion.
        """
        if self.selected_row is not None and self.current_table is not None:
            if self.current_table == self.student_table:
                del students[self.selected_row]
                self.update_student_table()
            elif self.current_table == self.instructor_table:
                del instructors[self.selected_row]
                self.update_instructor_table()
            elif self.current_table == self.course_table:
                del courses[self.selected_row]
                self.update_course_table()

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
