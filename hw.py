# There are 4 classes(blueprints for creating instances), Student, Mentor and 2 childs of Mentor > Lecturer & Reviewer
class Student:
    # This method for initializing attributes of the class
    # 'self' for accessing attributes and methods of the class (представляет экземпляр самого обьекта)
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}      
    # Данный метод, для начала проверяет, что является ли переменная - экземпляром лектора
    # Ведет ли лектор Х курс и через self - является ли студент Х курса. Если так, то соответсвенно выставляется отценка от студента
    def lec_feedback(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.feedback:
                lecturer.feedback[course] += [rate]
            else:
                lecturer.feedback[course] = [rate]
        else:
            return 'Ошибка'
    # Метод для подсчета ср. оценки
    def calculate_average_grade(self):
        total = 0
        l = [sum(i) / len(i) for i in self.grades.values()]
        for k in range(len(l)):
            total += l[k] 
        return (total / len(l))
    # Метод для unpacking`a листа курсов
    def unpacking(forlist):
        return ','.join(map(str, forlist))
    # Данный метод для строкового представления обьекта    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average_grade():.1f}\nКурсы в процессе изучения: {", ".join(str(i) for i in self.courses_in_progress)}\nЗавершенные курсы: {", ".join(str(i) for i in self.finished_courses)}'
    # Compare one student with another (magic method)
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() < other.calculate_average_grade()
    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() > other.calculate_average_grade()
    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() <= other.calculate_average_grade()
    def __ge__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() >= other.calculate_average_grade()
    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() == other.calculate_average_grade()
    def __ne__(self, other):
        if not isinstance(other, Student):
            return 'Нужно выбрать студентов для сравнения'
        return self.calculate_average_grade() != other.calculate_average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# Таким образом, родитель класса Lecturer - является Mentor, поэтому (указывается названание класса)
# С помощью super() - мы берем метод у родителям и расширяем функционал для лектора       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.feedback = {}
        
    def average_feedback(self):
        total = 0
        l = [sum(i) / len(i) for i in self.feedback.values()]
        for k in range(len(l)):
            total += l[k] 
        return (total / len(l))

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_feedback():.1f}'
    # compare average of one lecturer with another
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() < other.average_feedback()
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() > other.average_feedback()
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() <= other.average_feedback()
    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() >= other.average_feedback()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() == other.average_feedback()
    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нужно выбрать лекторов для сравнения'
        return self.average_feedback() != other.average_feedback()
    
class Reviwers(Mentor):
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
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Instances/экземпляры    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git', 'Java']
best_student.finished_courses += ['Введение в программирование']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

reviewing_teacher = Reviwers('Iam', 'Reviewer')
reviewing_teacher.courses_attached += ['Python', 'Java']

reviewing_teacher.rate_hw(best_student, 'Python', 8)
reviewing_teacher.rate_hw(best_student, 'Python', 9)
reviewing_teacher.rate_hw(best_student, 'Python', 10)

reviewing_teacher.rate_hw(best_student, 'Java', 7)
reviewing_teacher.rate_hw(best_student, 'Java', 8)
reviewing_teacher.rate_hw(best_student, 'Java', 7)

another_student = Student('Aguero', 'Thomson', 'Male')
another_student.courses_in_progress += ['Java', 'Python']

reviewing_teacher.rate_hw(another_student, 'Python', 8)
reviewing_teacher.rate_hw(another_student, 'Python', 9)
reviewing_teacher.rate_hw(another_student, 'Python', 8)

reviewing_teacher.rate_hw(another_student, 'Java', 4)
reviewing_teacher.rate_hw(another_student, 'Java', 5)
reviewing_teacher.rate_hw(another_student, 'Java', 6)

one_lecturer = Lecturer('Ivanko', 'AndrewLec')
one_lecturer.courses_attached += ['Java']

second_lecturer = Lecturer('Jon', 'PolandLec')
second_lecturer.courses_attached += ['Java']

another_student.lec_feedback(one_lecturer, 'Java', 10)
another_student.lec_feedback(one_lecturer, 'Java', 8)
another_student.lec_feedback(one_lecturer, 'Java', 7)

best_student.lec_feedback(second_lecturer, 'Java', 10)
best_student.lec_feedback(second_lecturer, 'Java', 9)
best_student.lec_feedback(second_lecturer, 'Java', 7)
# Instances/экземпляры 

print(reviewing_teacher, one_lecturer, best_student, '', sep='\n\n')
print(one_lecturer > second_lecturer, one_lecturer < second_lecturer, best_student <= another_student, best_student >= another_student, '\n')
print(f'Инфо Студенты: {best_student.grades} и {another_student.grades}\nИнфо Лекторы: {one_lecturer.feedback} и {second_lecturer.feedback}\n')

# Studnets class instances
x = [best_student, another_student]
y = 'Python'
def cal_average_hw_of_students(sci, coursename):
    total = 0
    for i in range(len(sci)):
        if coursename in sci[i].grades:
            x = sci[i].grades[coursename]
            total += sum(x)/len(x)
        else:
            return 'Неверно указан курс'
    return f'Средняя оценка за домашнее задания по всем студентам: {total / len(sci):.1f}'
print(cal_average_hw_of_students(x,y))

# Lecturers class instances
z = [one_lecturer, second_lecturer]
k = 'Java'
def cal_average_fb_of_lecturers(lci, coursename):
    total = 0
    for i in range(len(lci)):
        if coursename in lci[i].feedback:
            x = lci[i].feedback[coursename]
            total += sum(x)/len(x)
        else:
            return 'Неверно указан курс'
    return f'Средняя оценка за лекции по лекторам: {total / len(lci):.1f}'
print(cal_average_fb_of_lecturers(z,k))
