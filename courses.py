class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Student(Person):
    def __init__(self, firstname, lastname, teaches):
        super().__init__(firstname, lastname)
        self.teaches = teaches


class Teachers(Person):
    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname)
        self.skills = skills


class Courses(object):
    def __init__(self, name, duration, disciplines, teachers, students):
        pass