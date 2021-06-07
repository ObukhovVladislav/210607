class TeachGroup:
    def __init__(self, title):
        self.title = title
        self.students = []


class Student:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address


student_1 = Student('Иванов Иван Иванович', '10.02.2002', 'г.Курган. центр')
student_2 = Student('Сергеев Сергей Сергеевич', '10.02.2002', 'г.Курган. центр')
group_1 = TeachGroup('ИСИП-33')

group_1.__add__(student_1)
group_1.__add__(student_2)
# print()
group_1.__del__(student_1)
group_1.__del__(student_2)
