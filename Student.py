#By Karim Abboud

from Person import Person
import json

class Student(Person):
    def __init__(self, name: str, age: int, email: str, student_id: str, registered_courses = None):
        if registered_courses is None:
            registered_courses = []
        if not isinstance(student_id, str) or not student_id:
            raise ValueError("Student ID must be a non-empty string.")
        super().__init__(name, age, email)
        
        self.student_id = student_id
        self.registered_courses = registered_courses

    def register_course(self, course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)

    def __str__(self) -> str:
        return self.name + " (" + self.student_id + ")"
    
    # Serialize the student object to a dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self._email,
            'student_id': self.student_id,
            'registered_courses': self.registered_courses  # Serialize courses as a list of course names/IDs
        }

    # Create a Student instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        # Ensure that the parent class data is validated before passing it to the constructor
        Person.validate_data(data)
        return cls(data['name'], data['age'], data['email'], data['student_id'], data.get('registered_courses', []))

    # Validation for Student-specific data
    @classmethod
    def validate_data(cls, data):
        # Validate parent class data
        Person.validate_data(data)
        if not isinstance(data.get('student_id'), str) or not data.get('student_id'):
            raise ValueError("Student ID must be a non-empty string.")
        if not isinstance(data.get('registered_courses', []), list):
            raise ValueError("Registered courses must be a list.")