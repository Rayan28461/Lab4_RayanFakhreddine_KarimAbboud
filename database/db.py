# Rayan Fakhreddine

import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    # Optionally read from schema.sql file if you have SQL statements there
    with open('src/database/schema/schema.sql', 'r') as f:
        schema = f.read()

    # Execute the schema SQL (e.g., CREATE TABLE statements)
    cursor.executescript(schema)

    # Commit the changes
    conn.commit()

    print('Tables created successfully')

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        print('Connection failed')

    print('Connection established successfully')
    return conn

# CRUD Operations for Students
def create_student(student_id, name, age, email):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (student_id, name, age, email) VALUES (?, ?, ?, ?)', 
                   (student_id, name, age, email))
    conn.commit()
    print('Student created successfully')

def read_students():
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    print('fetched')
    return cursor.fetchall()

def update_student(student_id, name, age, email):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name=?, age=?, email=? WHERE student_id=?', 
                   (name, age, email, student_id))
    conn.commit()

def delete_student(student_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id=?', (student_id,))
    conn.commit()

# CRUD Operations for Instructors
def create_instructor(instructor_id, name, age, email):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO instructors (instructor_id, name, age, email) VALUES (?, ?, ?, ?)', 
                   (instructor_id, name, age, email))
    conn.commit()

def read_instructors():
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM instructors')
    print('fetched')
    return cursor.fetchall()

def update_instructor(instructor_id, name, age, email):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE instructors SET name=?, age=?, email=? WHERE instructor_id=?', 
                   (name, age, email, instructor_id))
    conn.commit()

def delete_instructor(instructor_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM instructors WHERE instructor_id=?', (instructor_id,))
    conn.commit()

# CRUD Operations for Courses
def create_course(course_id, course_name, instructor_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO courses (course_id, course_name, instructor_id) VALUES (?, ?, ?)', 
                   (course_id, course_name, instructor_id))
    conn.commit()

def read_courses():
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    print('fetched')
    return cursor.fetchall()

def update_course(course_id, course_name, instructor_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE courses SET course_name=?, instructor_id=? WHERE course_id=?', 
                   (course_name, instructor_id, course_id))
    conn.commit()

def delete_course(course_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM courses WHERE course_id=?', (course_id,))
    conn.commit()

# CRUD Operations for Registrations
def create_registration(student_id, course_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO registrations (student_id, course_id) VALUES (?, ?)', 
                   (student_id, course_id))
    conn.commit()

def read_registrations():
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registrations')
    return cursor.fetchall()

def delete_registration(student_id, course_id):
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM registrations WHERE student_id=? AND course_id=?', 
                   (student_id, course_id))
    conn.commit()

# Method to fetch the student count for each course
def get_student_count_per_course():
    conn = sqlite3.connect('src/database/school_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT courses.course_name, courses.course_id, instructors.name, COUNT(registrations.student_id) AS student_count
        FROM courses
        LEFT JOIN registrations ON courses.course_id = registrations.course_id
        LEFT JOIN instructors ON courses.instructor_id = instructors.instructor_id
        GROUP BY courses.course_id;
    ''')
    return cursor.fetchall()
