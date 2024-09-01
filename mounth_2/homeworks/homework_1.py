class Person:
    def __init__(self, fullname:str, age:int, is_married:bool):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'{self.fullname} is {self.age} and {"not " if not self.is_married else ""}married.')

class Student(Person):
    def __init__(self, fullname:str, age:int, is_married:bool, marks:dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average_mark(self) -> float:
        """
        return student's average mark
        """
        return round(sum(self.marks.values()) / len(self.marks), 2)


class Teacher(Person):
    base_salary = 20000

    def __init__(self, fullname:str, age:int, is_married:bool, experience:int):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self) -> int:
        """
        return teacher's salary, 
        if experience more than 3 year's he's get bonus 5% for every next year
        """
        if self.experience > 3:
            salary_multiplier = 1 + 0.05 * (self.experience - 3)
        else:
            salary_multiplier = 1

        return round(Teacher.base_salary * salary_multiplier)

def create_students() -> list:
    """
    return list of 3 students
    """
    return [
        Student('Akel', 15, False, {'math':5, 'russian':3, 'IT': 5, 'physyc': 4}),
        Student('Droki', 18, False, {'math':4, 'russian':4, 'IT': 5, 'physyc': 4, 'geometry': 4, 'english': 4}),
        Student('Safiya', 17, False, {'math':3, 'russian':3, 'physyc': 4})
    ]


math_teacher = Teacher('Mr.Alex', 26, True, 5)
math_teacher.introduce_myself()
print(f'{math_teacher.fullname}\'s salary is {math_teacher.get_salary()}.')

students = create_students()
for student in students:
    print()
    student.introduce_myself()
    for work, mark in student.marks.items():
        print(f'{work}: {mark}')
    print(f'Average grade: {student.get_average_mark()}')