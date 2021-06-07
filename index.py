class TeachGroup:
    def __init__(self, title, students):
        self.title = title
        self.students = students


class Student(TeachGroup):

    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address
