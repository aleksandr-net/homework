import datetime


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
    def __init__(self, name, duration=None, disciplines=None, teachers=None, students=None):
        self.name = name
        self.duration = duration
        self.disciplines = disciplines
        self.teachers = teachers
        self.students = students


    def set_duration(self, start_date, end_date):
        pass


    def set_discipline(self, name):
        pass


    def set_teachers(self, teacher):
        pass


    def set_students(self, student):
        pass

class Discipline(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
