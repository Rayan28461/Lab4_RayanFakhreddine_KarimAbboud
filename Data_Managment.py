# By Karim Abboud

import json
from Person import Person
from Student import Student
from Instructor import Instructor
from Course import Course
import csv
import psycopg2

def export_students_to_csv(student_list, filename="students.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["Name", "Age", "Email", "Student ID", "Courses"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in student_list:
            writer.writerow({
                "Name": student.name,
                "Age": student.age,
                "Email": student._email,
                "Student ID": student.student_id,
                "Courses": ", ".join(str(course) for course in student.registered_courses)
            })
    print(f"Student data exported to {filename}.")

def export_instructors_to_csv(instructor_list, filename="instructors.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["Name", "Age", "Email", "Instructor ID", "Courses"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for instructor in instructor_list:
            writer.writerow({
                "Name": instructor.name,
                "Age": instructor.age,
                "Email": instructor._email,
                "Instructor ID": instructor.instructor_id,
                "Courses": ", ".join(str(course) for course in instructor.assigned_courses)
            })
    print(f"Instructor data exported to {filename}.")

def export_courses_to_csv(course_list, filename="courses.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["Course ID", "Course Name", "Instructor", "Enrolled Students"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for course in course_list:
            writer.writerow({
                "Course ID": course.course_id,
                "Course Name": course.course_name,
                "Instructor": course.instructor.name if course.instructor else "No Instructor",
                "Enrolled Students": ", ".join(str(student) for student in course.enrolled_students)
            })
    print(f"Course data exported to {filename}.")


def save_persons_to_file(person_list, filename="persons.json"):
    data = [person.to_dict() for person in person_list]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Person data saved to {filename}.")

def load_persons_from_file(filename="persons.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        person_list = [Person.from_dict(person_data) for person_data in data]
        print(f"Person data loaded from {filename}.")
        return person_list
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return []
    except ValueError as e:
        print(f"Error loading person data: {e}")
        return []

def save_students_to_file(student_list, filename="students.json"):
    data = [student.to_dict() for student in student_list]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Student data saved to {filename}.")

def load_students_from_file(filename="students.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        student_list = [Student.from_dict(student_data) for student_data in data]
        print(f"Student data loaded from {filename}.")
        return student_list
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return []
    except ValueError as e:
        print(f"Error loading student data: {e}")
        return []

def save_instructors_to_file(instructor_list, filename="instructors.json"):
    data = [instructor.to_dict() for instructor in instructor_list]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Instructor data saved to {filename}.")

def load_instructors_from_file(filename="instructors.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        instructor_list = [Instructor.from_dict(instructor_data) for instructor_data in data]
        print(f"Instructor data loaded from {filename}.")
        return instructor_list
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return []
    except ValueError as e:
        print(f"Error loading instructor data: {e}")
        return []

def save_courses_to_file(course_list, filename="courses.json"):
    data = [course.to_dict() for course in course_list]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Course data saved to {filename}.")

def load_courses_from_file(filename="courses.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        course_list = [Course.from_dict(course_data) for course_data in data]
        print(f"Course data loaded from {filename}.")
        return course_list
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return []
    except ValueError as e:
        print(f"Error loading course data: {e}")
        return []










############### SQL DATABASE FUNCTIONS ####################
# The following functions are used to interact with a PostgreSQL database.
def connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="School_Management_435L"
        )
        print("Connected to database.")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def create_student(name, age, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (name, age, email) 
            VALUES (%s, %s, %s) RETURNING student_id;
        """, (name, age, email))
        student_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Student {name} created with ID {student_id}.")
        return student_id
    except Exception as e:
        print(f"Error creating student: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def create_instructor(name, age, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO instructors (name, age, email) 
            VALUES (%s, %s, %s) RETURNING instructor_id;
        """, (name, age, email))
        instructor_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Instructor {name} created with ID {instructor_id}.")
        return instructor_id
    except Exception as e:
        print(f"Error creating instructor: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def create_course(course_name, instructor_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO courses (course_name, instructor_id) 
            VALUES (%s, %s) RETURNING course_id;
        """, (course_name, instructor_id))
        course_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Course {course_name} created with ID {course_id}.")
        return course_id
    except Exception as e:
        print(f"Error creating course: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def enroll_student_in_course(student_id, course_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO enrollments (student_id, course_id) 
            VALUES (%s, %s);
        """, (student_id, course_id))
        conn.commit()
        print(f"Student {student_id} enrolled in course {course_id}.")
    except Exception as e:
        print(f"Error enrolling student: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def get_all_students():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        return students
    except Exception as e:
        print(f"Error retrieving students: {e}")
    finally:
        cursor.close()
        conn.close()

def get_all_instructors():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM instructors;")
        instructors = cursor.fetchall()
        return list(instructors)
    except Exception as e:
        print(f"Error retrieving instructors: {e}")
    finally:
        cursor.close()
        conn.close()


def get_all_courses():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM courses;")
        courses = cursor.fetchall()
        return list(courses)
    except Exception as e:
        print(f"Error retrieving courses: {e}")
    finally:
        cursor.close()
        conn.close()

def get_enrollments_by_course(course_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT students.student_id, students.name 
            FROM enrollments 
            JOIN students ON enrollments.student_id = students.student_id
            WHERE enrollments.course_id = %s;
        """, (course_id,))
        enrollments = cursor.fetchall()
        for enrollment in enrollments:
            print(enrollment)
    except Exception as e:
        print(f"Error retrieving enrollments: {e}")
    finally:
        cursor.close()
        conn.close()

def update_student(student_id, name=None, age=None, email=None):
    conn = connect()
    cursor = conn.cursor()
    try:
        if name:
            cursor.execute("UPDATE students SET name = %s WHERE student_id = %s;", (name, student_id))
        if age:
            cursor.execute("UPDATE students SET age = %s WHERE student_id = %s;", (age, student_id))
        if email:
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (email, student_id))
        conn.commit()
        print(f"Student {student_id} updated successfully.")
    except Exception as e:
        print(f"Error updating student: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_instructor(instructor_id, name=None, age=None, email=None):
    conn = connect()
    cursor = conn.cursor()
    try:
        if name:
            cursor.execute("UPDATE instructors SET name = %s WHERE instructor_id = %s;", (name, instructor_id))
        if age:
            cursor.execute("UPDATE instructors SET age = %s WHERE instructor_id = %s;", (age, instructor_id))
        if email:
            cursor.execute("UPDATE instructors SET email = %s WHERE instructor_id = %s;", (email, instructor_id))
        conn.commit()
        print(f"Instructor {instructor_id} updated successfully.")
    except Exception as e:
        print(f"Error updating instructor: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def update_course(course_id, course_name=None, instructor_id=None):
    conn = connect()
    cursor = conn.cursor()
    try:
        if course_name:
            cursor.execute("UPDATE courses SET course_name = %s WHERE course_id = %s;", (course_name, course_id))
        if instructor_id:
            cursor.execute("UPDATE courses SET instructor_id = %s WHERE course_id = %s;", (instructor_id, course_id))
        conn.commit()
        print(f"Course {course_id} updated successfully.")
    except Exception as e:
        print(f"Error updating course: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def delete_student(student_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM enrollments WHERE student_id = %s;", (student_id,))
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        print(f"Student {student_id} deleted.")
    except Exception as e:
        print(f"Error deleting student: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def delete_instructor(instructor_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM courses WHERE instructor_id = %s;", (instructor_id,))
        cursor.execute("DELETE FROM instructors WHERE instructor_id = %s;", (instructor_id,))
        conn.commit()
        print(f"Instructor {instructor_id} deleted.")
    except Exception as e:
        print(f"Error deleting instructor: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def delete_course(course_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM enrollments WHERE course_id = %s;", (course_id,))
        cursor.execute("DELETE FROM courses WHERE course_id = %s;", (course_id,))
        conn.commit()
        print(f"Course {course_id} deleted.")
    except Exception as e:
        print(f"Error deleting course: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
