class TeachGroup:
    def __init__(self, title, student):
        self.title = title
        self.student = student


class Student(TeachGroup):

    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address
