#By Karim Abboud

from Person import Person

class Instructor(Person):
    def __init__(self, name:str, age: str, email: str, instructor_id: str, assigned_courses = None):
        if assigned_courses is None:
            assigned_courses = []
        if not isinstance(instructor_id, str) or not instructor_id:
            raise ValueError("Instructor ID must be a non-empty string.")
        super().__init__(name, age, email)
        
        self.instructor_id = instructor_id
        self.assigned_courses = assigned_courses

    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)

    def __str__(self) -> str:
        return f"{self.name} ({self.instructor_id})"
    
    # Serialize the instructor object to a dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self._email,
            'instructor_id': self.instructor_id,
            'assigned_courses': self.assigned_courses  # Serialize courses as a list of course names/IDs
        }

    # Create an Instructor instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        # Ensure that the parent class data is validated before passing it to the constructor
        Person.validate_data(data)
        return cls(data['name'], data['age'], data['email'], data['instructor_id'], data.get('assigned_courses', []))

    # Validation for Instructor-specific data
    @classmethod
    def validate_data(cls, data):
        # Validate parent class data
        Person.validate_data(data)
        if not isinstance(data.get('instructor_id'), str) or not data.get('instructor_id'):
            raise ValueError("Instructor ID must be a non-empty string.")
        if not isinstance(data.get('assigned_courses', []), list):
            raise ValueError("Assigned courses must be a list.")