class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.enrolled={}
    def enrolleds(self,course,grade=None):
        self.enrolled[course]=grade
    def get_courses(self):
        return list(self.enrolled.keys())
    def get_grades(self):
        return list(self.enrolled.values())
    def __str__(self):
        return f"Student ID:{self.student_id},Name:{self.name}"
class Course:
    def __init__(self,course_id,course_name):
        self.course_id=course_id
        self.course_name=course_name
    def __str__(self):
        return f"Course ID:{self.course_id},course Name:{self.course_name}"
class Grades:
    def calculate_gpa(grades):
        if not grades:
            return 0.0
        total_points=0.0
        total_credits=0.0
        for grade in grades:
            if grade=='A':
                total_points+=4.0
            elif grade=="B":
                total_points+=3.0
            elif grade=='C':
                total_points+=2.0
            elif grade=='D':
                total_points+=1.0
            total_credits+=1
        return total_points/total_credits
# Creating students
student1 = Student(1, "Hi hlo")
student2 = Student(2, "whats up")
# Creating courses
course1 = Course("CSC101", "Introduction to Programming")
course2 = Course("MAT201", "Linear Algebra")
student1.enrolleds(course1,'A')
student1.enrolleds(course2,'B')
student2.enrolleds(course1,'A')
student2.enrolleds(course2,'A')
print(student1)
print(f"Enrolled courses:{[str(course) for course in student1.get_courses()]}")
print(f"Grades: {student1.get_grades()}")
print(f"GPA: {Grades.calculate_gpa(student1.get_grades())}")

print("\n")
print(student2)
print(f"Enrolled courses:{[str(course) for course in student2.get_courses()]}")
print(f"Grades: {student2.get_grades()}")
print(f"GPA: {Grades.calculate_gpa(student2.get_grades())}")
