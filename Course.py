#By Karim Abboud

from Instructor import Instructor
from Student import Student

class Course:
    from typing import List
    
    def __init__(self, course_id: str, course_name: str, instructor: Instructor, enrolled_students: List[Student] = None):
        if enrolled_students is None:
            enrolled_students = []
        if not isinstance(course_id, str) or not course_id:
            raise ValueError("Course ID must be a non-empty string.")
        if not isinstance(course_name, str) or not course_name:
            raise ValueError("Course name must be a non-empty string.")
        if not isinstance(instructor, Instructor):
            raise ValueError("Instructor must be a valid Instructor object.")
        
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = enrolled_students

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise ValueError("Only valid Student objects can be added to the course.")
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def __str__(self):
        return f"{self.course_id}"
    
    def assign_instructor(self, instructor: Instructor):
        if not isinstance(instructor, Instructor):
            raise ValueError("Only valid Instructor objects can be assigned to the course.")
        self.instructor = instructor

    # Serialize the course object to a dictionary
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'instructor': self.instructor.to_dict(),  # Serialize the instructor object
            'enrolled_students': [student.to_dict() for student in self.enrolled_students]  # Serialize each student in the course
        }

    # Create a Course instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        # Create Instructor and Student objects from serialized data
        instructor = Instructor.from_dict(data['instructor'])
        students = [Student.from_dict(student_data) for student_data in data['enrolled_students']]
        return cls(data['course_id'], data['course_name'], instructor, students)

    # Validation for Course-specific data
    @classmethod
    def validate_data(cls, data):
        if not isinstance(data.get('course_id'), str) or not data.get('course_id'):
            raise ValueError("Course ID must be a non-empty string.")
        if not isinstance(data.get('course_name'), str) or not data.get('course_name'):
            raise ValueError("Course name must be a non-empty string.")
        Instructor.validate_data(data.get('instructor'))
        if not isinstance(data.get('enrolled_students', []), list):
            raise ValueError("Enrolled students must be a list.")