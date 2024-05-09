from datetime import date

class Individual():
    def __init__(self, name, birthday=None):
        self.name = name
        self.birthday = birthday

    def get_name(self):
        return self.name

    def add_birthday(self, birthday):
        self.birthday = birthday
        return self.birthday

    def get_age(self):
        if self.birthday is None:
            return 'Not Available'
        else:
            a = date.today()
            a1 = a.year
            age = a1 - self.birthday.year
            return age

    def __str__(self):
        return str(self.name)

class AU_Employee(Individual):
    New_emp = 1
    def __init__(self, name):
        super().__init__(name)

    def get_unique_id(self):
        self.id = AU_Employee.New_emp
        AU_Employee.New_emp += 1
        return self.id

class Faculty(AU_Employee):
    def __init__(self, name):
        super().__init__(name)

class EN_Faculty(Faculty):
    def __init__(self, name, classroom_year, birthday=None):
        super().__init__(name)
        self.classroom_year = classroom_year
        self.birthday = birthday

    def assign_class(self, batch):
        self.batch = batch

class Design_Faculty(Faculty):
    def __init__(self, name, classroom_year, birthday=None):
        super().__init__(name)
        self.classroom_year = classroom_year
        self.birthday = birthday

    def assign_class(self, batch):
        self.batch = batch

class Roster_AU():
    def __init__(self):
        self.faculty1 = {}
        self.courses = {}

    def add_faculty(self, faculty):
        if faculty.name not in self.faculty1:
            self.faculty1[faculty.name] = []

    def add_course(self, faculty, course):
        if faculty.name not in self.faculty1:
            raise ValueError('No Faculty Found.')
        self.faculty1[faculty.name].append(course)

    def get_courses(self, faculty):
        if faculty.name not in self.faculty1:
            raise ValueError('No Faculty Found.')
        return sorted(self.faculty1[faculty.name])

obj = Individual("OJASVI", date(2004, 12, 24))
print(obj.get_name())
print(obj.get_age())
faculty1 = Faculty("gaurav")
faculty2 = EN_Faculty("navni", "2023", date(1666, 11, 5))
faculty2.assign_class("BTECH-1")
obj1 = Roster_AU()
obj1.add_faculty(faculty1)
obj1.add_faculty(faculty2)
obj1.add_course(faculty1, "HINDI")
obj1.add_course(faculty1, "ENGLISH")
obj1.add_course(faculty2, "PHYSICS")
obj1.add_course(faculty2, "CHEMISTRY")
faculty1_courses = obj1.get_courses(faculty1)
print(faculty1_courses)
faculty2_courses = obj1.get_courses(faculty2)
print(faculty2_courses)
