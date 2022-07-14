class Student:
    def __init__(self, name, courses, grades):
        self.name = name
        self.courses = courses
        self.grades = grades

    def gpa(self):
        sum = 0
        for grade in self.grades:
            sum = sum + grade
        gpa = sum / len(self.grades)
        return gpa

    def shared_classes(self, other):
        courses = []
        for self_course in self.courses:
            for other_course in other.courses:
                if (self_course == other_course):
                    courses.append(self_course)
                    
        if (courses == []):
            courses = "They have no classes in common."
        else:
            courses = "Classes in common: " + str(courses)
        return courses



aaaa = Student("AAAA", ["A", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa"], [12,50])
rob = Student("Rob", ["Geometry", "Math"], [40,50])
alice = Student("Alice", ["Calculus", "Computer Science"], [-0,50])
jacob = Student("Alice", ["Calculus", "Computer"], [-0,50])