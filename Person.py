#By Karim Abboud
import re

class Person:
    def __init__(self, name: str, age: int, email: str):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self._validate_email(email)

        self.name = name
        self.age = age
        self._email = email

    def _validate_email(self, email: str):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email address: {email}")
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self._email
        }

    # Create a Person instance from a dictionary (for deserialization)
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['email'])

    # Validation for the data
    @classmethod
    def validate_data(cls, data):
        if not isinstance(data.get('name'), str) or not data.get('name'):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(data.get('age'), int) or data.get('age') <= 0:
            raise ValueError("Age must be a positive integer.")
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, data.get('email')):
            raise ValueError(f"Invalid email address: {data.get('email')}")

     
