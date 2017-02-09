import sqlite3


class User:
    """Parent class for all user instances - represents all users"""

    def __init__(self, user_id, name, mail, password):
        """Attributes for all users - id, name, e-mail, password"""
        self.id = user_id
        self.name = name
        self.mail = mail
        self.password = password
        User.user_list.append(self)

    @classmethod
    def get_user_list(cls):
        """Returns list with all users instances"""
        return cls.user_list

    def get_name(self):
        """Returns user instance name"""
        return self.name

    def get_id(self):
        """Returns user instance id"""
        return self.id

    def get_mail(self):
        """Returns user instance mail"""
        return self.mail

    def get_password(self):
        """Returns user instance password"""
        return self.password

    def get_class_name(self):
        """Returns user instance subclass name"""
        return self.__class__.__name__

    def set_name(self, new_name):
        """Sets users name"""
        self.name = new_name

    def set_mail(self, new_mail):
        """Sets users mail"""
        self.mail = new_mail

    def set_password(self, new_password):
        """Sets users password"""
        self.password = new_password

    @classmethod
    def remove_user(cls, user_id):
        """Removes user instance from user list"""
        DB.delete_user_record(user_id)
        DB.delete_user_attendance_record(user_id)
        DB.delete_user_submission_record(user_id)


class Student(User):
    """Class that represent students"""

    def __init__(self, name, mail, password):
        """Student has additional attributes - grade list, attendance list, submission list"""
        super().__init__(user_id, self, name, mail, password)
        self.grade_list = []
        self.attendance_list = []  # collect all attendance instances
        self.submission_list = []  # collect all submissions sending by student

    @classmethod
    def add_student(cls, name, mail, password):
        """Adds news student instance and appends its to student list"""
        cls.student_list.append(Student(name, mail, password))

    @classmethod
    def get_student_list(cls):
        """Returns list with students"""
        student_list = []
        con = sqlite3.connect('Data/ccms.db')
        table = con.execute("SELECT * FROM `users`;")
        for row in table:
            student_list.append(cls(*row[1:]))
        return student_list

    @classmethod
    def get_student(cls, name):
        """Searching in student list and returns student instance with given name"""
        for student in cls.student_list:
            if student.name == name:
                return student

    @classmethod
    def get_grade(cls, name, assignment_title):
        """Returns grade from assignment with title 'assignment_title' submit by student with name 'name'"""
        for student in cls.student_list:
            if student.name == name:
                for submission in student.submission_list:
                    if assignment_title:
                        return submission.points
                    else:
                        print('there is no such submission added by {}'.format(student.name))
            else:
                print('there is no such student in students list')


class Employee(User):
    """Class that represent employees"""
    pass


class Mentor(Employee):
    """Class that represent mentors"""

    def __init__(self, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_mentor(cls, name, mail, password):
        """Adds news mentor instance and appends its to mentors list"""
        cls.mentor_list.append(Mentor(name, mail, password))

    @classmethod
    def get_list_mentor(cls):
        """Returns list with mentors"""
        return cls.mentor_list

    @classmethod
    def get_mentor(cls, name):
        """Searching in mentor list and returns mentor instance with given name"""
        for mentor in cls.mentor_list:
            if mentor.name == name:
                return mentor


class Boss(Employee):
    """Class that represent boss"""

    def __init__(self, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_boss(cls, name, mail, password):
        """Adds news boss instance and appends its to boss list"""
        cls.boss_list.append(Boss(name, mail, password))

    @classmethod
    def remove_boss(cls, name):
        """Removes boss instance from boss list"""
        for boss in cls.boss_list:
            if boss.name == name:
                cls.boss_list.remove(boss)

    @classmethod
    def get_boss_list(cls):
        """Returns list with boss instances"""
        return cls.boss_list

    @classmethod
    def get_boss(cls, name):
        """Searching in boss list and returns boss instance with given name"""
        for boss in cls.boss_list:
            if boss.name == name:
                return boss


class Staff(Employee):
    """Class that represent staff employees"""

    def __init__(self, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_staff(cls, name, mail, password):
        """Adds news staff instance and appends its to staff list"""
        cls.staff_list.append(Staff(name, mail, password))

    @classmethod
    def get_staff_list(cls):
        """Returns list with staff instances"""
        return cls.staff_list

    @classmethod
    def get_staff(cls, name):
        """Searching in staff list and returns staff instance with given name"""
        for staff in cls.staff_list:
            if staff.name == name:
                return staff
