import datetime


class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Teachers(Person):
    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname)
        self.skills = None
        self.set_skills(skills)

    def set_skills(self, skills):
        self.skills = skills


class Courses(object):
    def __init__(self, name, duration, disciplines, teachers, students):
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
