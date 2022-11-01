import statistics
from statistics import mean


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # self.lecturer_assessment = lecturer_assessment
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        # rate_student_average = {key: sum(value) / len(value) for key, value in self.grades.items()}
        for key, value in self.grades.items():
           avg_student = mean(value)
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_student}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        return some_student

    def avg_student(self):
        for key, value in self.grades.items():
            avg_student_done = mean(value)
        return avg_student_done

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def rate_lector(self, student, course, lecturer_assessment):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.student_grades:
                self.student_grades[course] += [lecturer_assessment]
            else:
                self.student_grades[course] = [lecturer_assessment]
        else:
            return 'Ошибка'

    def avg_lecture(self):
        for key, value in self.student_grades.items():
            avg_lecture_done = sum(value) / len(value)
        return avg_lecture_done

    def __str__(self):
        # rate_lector_average = {key: sum(value) / len(value) for key, value in self.student_grades.items()}
        for key, value in self.student_grades.items():
            avg_lecture = mean(value)
        # some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка по курсу от студентов: {avg_lecture}'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка по курсу от студентов: {avg_lecture}'

    def __lt__(self, other):
        return self.avg_lecture() < other.avg_student()

    def __gt__(self, other):
        return self.avg_lecture() > other.avg_student()

    def __ge__(self, other):
        return self.avg_lecture() >= other.avg_student()

    def __le__(self, other):
        return self.avg_lecture() <= other.avg_student()
    # def __lt__(self, other):
    #     for key, value in self.student_grades:
    #         avg_lect = mean(value)
    #     for key, value in other.grades:
    #         avg_stud = mean(value)
    #     return avg_lect < avg_stud
    # def __lt__(self, other):
    #     return {key: sum(value) / len(value) for key, value in self.grades.values()} < {key: sum(value) / len(value) for key, value in self.student_grades.values()}
    # def __lt__(self, Student):
    #     for key, value in self.student_grades.items():
    #         avg_lecture = mean(value)
    #     for key, value in self.grades.items():
    #        avg_student = mean(value)
    #     if not isinstance(Student, Lecturer):
    #         if avg_student < avg_lecture:
    #             return print('Lector is winer')
    #         else:
    #             return print('Student is winer')
    #     else:
    #         return 'Not a Student!'

class Reviewer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return some_reviewer


best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lector = Lecturer('Head', 'basher')
cool_lector.courses_attached += ['Python']

cool_reviewer = Reviewer('shrek', 'lypovskiy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lector.rate_lector(best_student, 'Python', 9)
cool_lector.rate_lector(best_student, 'Python', 8)

print(best_student.grades)
print(cool_lector.student_grades)
print(cool_lector)
print(cool_reviewer)
print(best_student)
print(cool_lector < best_student)
print(cool_lector > best_student)

