# Rayan Fakhreddine

import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, filedialog
from tkinter import ttk  # Import ttk for Treeview
import pickle  # For saving and loading data

from database.db import *
from Student import Student
from Course import Course
from Instructor import Instructor

def parse_students():
    """
    Parses students data from the database.

    :return: A list of Student objects.
    :rtype: list[Student]
    """
    students = read_students()
    return [Student(*student) for student in students] 
    
def parse_courses():
    """
    Parses courses data from the database.

    :return: A list of Course objects.
    :rtype: list[Course]
    """
    courses = read_courses()
    return [Course(*course) for course in courses]

def parse_instructors():
    """
    Parses instructors data from the database.

    :return: A list of Instructor objects.
    :rtype: list[Instructor]
    """
    instructors = read_instructors()
    return [Instructor(*instructor) for instructor in instructors]

class SchoolManagementGUI:
    """
    GUI class for the School Management System.

    :param root: The root Tkinter window.
    :type root: tk.Tk
    """
    
    def __init__(self, root):
        """
        Initializes the SchoolManagementGUI with UI elements and data.

        :param root: The root window for the GUI.
        :type root: tk.Tk
        """
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("600x600")

        self.available_courses: list[Course] = parse_courses()  
        self.available_instructors: list[Instructor] = parse_instructors()  
        self.available_students: list[Student] = parse_students() 

        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the main UI elements for the school management system.
        """
        label = tk.Label(self.root, text="Welcome to the School Management System", font=("Arial", 16))
        label.pack(pady=20)

        student_button = tk.Button(self.root, text="Add Student", command=self.open_student_form)
        student_button.pack(pady=10)

        instructor_button = tk.Button(self.root, text="Add Instructor", command=self.open_instructor_form)
        instructor_button.pack(pady=10)

        course_button = tk.Button(self.root, text="Add Course", command=self.open_course_form)
        course_button.pack(pady=10)

        register_button = tk.Button(self.root, text="Register Student for Course", command=self.open_registration_form)
        register_button.pack(pady=10)

        records_button = tk.Button(self.root, text="Display All Records", command=self.display_records)
        records_button.pack(pady=10)

        save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        save_button.pack(pady=10)

        load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        load_button.pack(pady=10)

    def open_student_form(self):
        """
        Opens a form for adding a new student to the system.
        """
        student_form = tk.Toplevel(self.root)
        student_form.title("Add Student")
        student_form.geometry("400x300")

        tk.Label(student_form, text="Name").pack()
        name_entry = tk.Entry(student_form)
        name_entry.pack()

        tk.Label(student_form, text="Age").pack()
        age_entry = tk.Entry(student_form)
        age_entry.pack()

        tk.Label(student_form, text="Email").pack()
        email_entry = tk.Entry(student_form)
        email_entry.pack()

        tk.Label(student_form, text="Student ID").pack()
        student_id_entry = tk.Entry(student_form)
        student_id_entry.pack()

        def frontend_create_student():
            """
            Function to create a student from the form input and save it to the database.
            """
            name = name_entry.get()
            age = int(age_entry.get())
            email = email_entry.get()
            student_id = student_id_entry.get()

            new_student = create_student(student_id, name, age, email)
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            student_form.destroy()

        submit_button = tk.Button(student_form, text="Create Student", command=frontend_create_student)
        submit_button.pack(pady=10)

    def open_instructor_form(self):
        """
        Opens a form for adding a new instructor to the system.
        """
        instructor_form = tk.Toplevel(self.root)
        instructor_form.title("Add Instructor")
        instructor_form.geometry("400x300")

        tk.Label(instructor_form, text="Name").pack()
        name_entry = tk.Entry(instructor_form)
        name_entry.pack()

        tk.Label(instructor_form, text="Age").pack()
        age_entry = tk.Entry(instructor_form)
        age_entry.pack()

        tk.Label(instructor_form, text="Email").pack()
        email_entry = tk.Entry(instructor_form)
        email_entry.pack()

        tk.Label(instructor_form, text="Instructor ID").pack()
        instructor_id_entry = tk.Entry(instructor_form)
        instructor_id_entry.pack()

        def frontend_create_instructor():
            """
            Function to create an instructor from the form input and save it to the database.
            """
            name = name_entry.get()
            age = int(age_entry.get())
            email = email_entry.get()
            instructor_id = instructor_id_entry.get()

            new_instructor = create_instructor(instructor_id, name, age, email)
            messagebox.showinfo("Success", f"Instructor {name} added successfully!")
            instructor_form.destroy()
        
        submit_button = tk.Button(instructor_form, text="Create Instructor", command=frontend_create_instructor)
        submit_button.pack(pady=10)

    def open_course_form(self):
        """
        Opens a form for adding a new course to the system.
        """
        course_form = tk.Toplevel(self.root)
        course_form.title("Add Course")
        course_form.geometry("400x300")

        tk.Label(course_form, text="Course Name").pack()
        course_name_entry = tk.Entry(course_form)
        course_name_entry.pack()

        tk.Label(course_form, text="Course ID").pack()
        course_id_entry = tk.Entry(course_form)
        course_id_entry.pack()

        tk.Label(course_form, text="Select Instructor").pack()
        instructor_var = StringVar(course_form)
        instructor_var.set("Select an instructor")
        instructor_names = [instructor.name for instructor in self.available_instructors]
        instructor_menu = OptionMenu(course_form, instructor_var, *instructor_names)
        instructor_menu.pack()

        def frontend_create_course():
            """
            Function to create a course from the form input and save it to the database.
            """
            course_name = course_name_entry.get()
            course_id = course_id_entry.get()
            instructor_name = instructor_var.get()

            for instructor in self.available_instructors:
                if instructor.name == instructor_name:
                    new_course = create_course(course_id, course_name, instructor.instructor_id)
                    messagebox.showinfo("Success", f"Course {course_name} added successfully!")
                    break
            course_form.destroy()

        submit_button = tk.Button(course_form, text="Create Course", command=frontend_create_course)
        submit_button.pack(pady=10)

    def open_registration_form(self):
        """
        Opens a form for registering a student for a course.
        """
        registration_form = tk.Toplevel(self.root)
        registration_form.title("Register Student for Course")
        registration_form.geometry("400x300")

        tk.Label(registration_form, text="Select Student").pack()
        student_var = StringVar(registration_form)
        student_var.set("Select a student")
        student_names = [student.name for student in self.available_students]
        student_menu = OptionMenu(registration_form, student_var, *student_names)
        student_menu.pack()

        tk.Label(registration_form, text="Select Course").pack()
        course_var = StringVar(registration_form)
        course_var.set("Select a course")
        course_names = [course.course_name for course in self.available_courses]
        course_menu = OptionMenu(registration_form, course_var, *course_names)
        course_menu.pack()

        def frontend_register_student():
            """
            Function to register a student for a selected course and save the registration to the database.
            """
            student_name = student_var.get()
            course_name = course_var.get()

            for student in self.available_students:
                if student.name == student_name:
                    student_id = student.student_id
                    break

            for course in self.available_courses:
                if course.course_name == course_name:
                    course_id = course.course_id
                    break

            create_registration(course_id, student_id)
            messagebox.showinfo("Success", f"{student_name} registered for {course_name} successfully!")
            registration_form.destroy()
        
        submit_button = tk.Button(registration_form, text="Register Student", command=frontend_register_student)
        submit_button.pack(pady=10)

    def display_records(self):
        """
        Displays all students, instructors, and courses in a tabbed interface.
        """
        self.available_students = parse_students()
        self.available_instructors = parse_instructors()
        self.available_courses = parse_courses()

        records_window = tk.Toplevel(self.root)
        records_window.title("All Records")
        records_window.geometry("600x400")

        tab_control = ttk.Notebook(records_window)

        # Create tabs for students, instructors, and courses
        students_tab = ttk.Frame(tab_control)
        instructors_tab = ttk.Frame(tab_control)
        courses_tab = ttk.Frame(tab_control)

       
        # Add tabs to the notebook
        tab_control.add(students_tab, text="Students")
        tab_control.add(instructors_tab, text="Instructors")
        tab_control.add(courses_tab, text="Courses")
        tab_control.pack(expand=1, fill="both")

        # Treeview for displaying student records
        student_tree = ttk.Treeview(students_tab, columns=("ID", "Name", "Age", "Email"), show="headings")
        student_tree.heading("ID", text="Student ID")
        student_tree.heading("Name", text="Name")
        student_tree.heading("Age", text="Age")
        student_tree.heading("Email", text="Email")
        student_tree.pack(fill="both", expand=True)

        for student in self.available_students:
            student_tree.insert("", "end", values=(student.student_id, student.name, student.age, student.email))

        # Treeview for displaying instructor records
        instructor_tree = ttk.Treeview(instructors_tab, columns=("ID", "Name", "Age", "Email"), show="headings")
        instructor_tree.heading("ID", text="Instructor ID")
        instructor_tree.heading("Name", text="Name")
        instructor_tree.heading("Age", text="Age")
        instructor_tree.heading("Email", text="Email")
        instructor_tree.pack(fill="both", expand=True)

        for instructor in self.available_instructors:
            instructor_tree.insert("", "end", values=(instructor.instructor_id, instructor.name, instructor.age, instructor.email))

        # Treeview for displaying course records
        course_tree = ttk.Treeview(courses_tab, columns=("ID", "Course Name", "Instructor"), show="headings")
        course_tree.heading("ID", text="Course ID")
        course_tree.heading("Course Name", text="Course Name")
        course_tree.heading("Instructor", text="Instructor")
        course_tree.pack(fill="both", expand=True)

        for course in self.available_courses:
            instructor_name = next(instructor.name for instructor in self.available_instructors if instructor.instructor_id == course.instructor_id)
            course_tree.insert("", "end", values=(course.course_id, course.course_name, instructor_name))

    def save_data(self):
        """
        Saves all student, instructor, and course records to a file using pickle.
        """
        filename = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
        if not filename:
            return

        data = {
            "students": self.available_students,
            "instructors": self.available_instructors,
            "courses": self.available_courses
        }
        
        with open(filename, "wb") as file:
            pickle.dump(data, file)
            messagebox.showinfo("Success", "Data saved successfully!")

    def load_data(self):
        """
        Loads student, instructor, and course records from a file using pickle.
        """
        filename = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
        if not filename:
            return

        with open(filename, "rb") as file:
            data = pickle.load(file)

        self.available_students = data.get("students", [])
        self.available_instructors = data.get("instructors", [])
        self.available_courses = data.get("courses", [])
        messagebox.showinfo("Success", "Data loaded successfully!")
