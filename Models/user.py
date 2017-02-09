from db import DB


class User:
    """Parent class for all user instances - represents all users"""

    def __init__(self, user_id, name, mail, password):
        """Attributes for all users - id, name, e-mail, password"""
        self.id = user_id
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def get_user_by_id(cls, user_id):
        """
        Returns user object.
        :return:
            user: object
        """
        return cls.create_user(user_id)

    @classmethod
    def get_user_list_by_role(cls, role):
        """
        Returns list with user objects
        :return:
            user_list: list
        """
        return cls.create_user_list_by_role(role)

    @classmethod
    def get_user_list_by_id_list(cls, id_list):
        """
        Returns list with user objects
        :return:
            user_list: list
        """
        return cls.create_user_list_by_id_list(id_list)

    @classmethod
    def create_user(cls, user_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_user_record_by_user_id(user_id)
        return User(*args[0])

    @classmethod
    def create_user_list_by_role(cls, role):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        users_data = DB.read_user_record_list_by_role(role)
        return [User(*user) for user in users_data]

    @classmethod
    def create_user_list_by_id_list(cls, id_list):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        users_data = DB.read_user_record_list_by_id(id_list)
        return [User(*user) for user in users_data]

    @classmethod
    def add_user(cls, name, mail, password):
        values = (name, mail, password, cls.get_class_name().lower())
        new_user_id = DB.create_user_record(values)
        new_user = cls.get_user_by_id(new_user_id)
        return new_user

    @classmethod
    def get_class_name(cls):
        """Returns user instance subclass name"""
        return cls.__name__

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
        DB.update_name(self.get_id(), new_name)

    def set_mail(self, new_mail):
        """Sets users mail"""
        self.mail = new_mail
        DB.update_mail(self.get_id(), new_mail)

    def set_password(self, new_password):
        """Sets users password"""
        self.password = new_password
        DB.update_password(self.get_id(), new_password)

    @classmethod
    def remove_user(cls, user_id):
        """Removes user instance from user list"""
        DB.delete_user_record(user_id)
        DB.delete_user_attendance_record(user_id)
        DB.delete_user_submission_record(user_id)


class Student(User):
    """Class that represent students"""

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


class Mentor(Employee):
    """Class that represent mentors"""


class Boss(Employee):
    """Class that represent boss"""


class Staff(Employee):
    """Class that represent staff employees"""
