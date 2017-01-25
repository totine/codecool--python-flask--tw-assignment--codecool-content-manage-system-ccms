class UserInterface:

    @staticmethod
    def main_menu():
        options = ['Log in', 'Exit']
        UserInterface.print_options_list(options)
        try:
            user_choice = int(input('Chose action: '))
        except ValueError:
            print("Wrong input")
        return options[user_choice - 1]

    @staticmethod
    def login():
        user_name = input('Provide your username: ')
        user_password = input('Provide your password: ')
        return (user_name, user_password)

    @staticmethod
    def student_menu():
        options = ['Submit an assignment', 'View my grades', 'Log out']
        UserInterface.print_options_list(options)
        try:
            user_choice = int(input('Chose action: '))
        except ValueError:
            print("Wrong input")
        return options[user_choice - 1]

    @staticmethod
    def get_submit_data():
        title = input("Please provide title of submission: ")
        content = input("Please provide link to your assignment: ")
        date = input("What date is it today? ;p ") # Remember to import date
        assignment_title = input("Please provide title of assignment: ")
        owner_name = input("Please provide your name") # Use caller object next
        return title, content, date, assignment_title, owner_name

    @staticmethod
    def view_grade(student):
        submission_title = input("What submission are you interested in? ")
        grade = student.Student.get_grade(submission_title)
        if grade:
            print("Your score is :{}".format(grade))
        else:
            print("Your submission haven't been grade yet")

    @staticmethod
    def mentor_menu():
        options = ['Show students list', 'Add an assignment', 'Grade an assignment', 'Check attendance', 'Add student',
                   'Remove student', 'Edit student data', 'Log out']
        UserInterface.print_options_list(options)
        try:
            user_choice = int(input('Chose action: '))
        except ValueError:
            print("Wrong input")
        return options[user_choice - 1]

    @staticmethod
    def get_assignment_data():
        title = input("Please provide assignment title: ")
        content = input("Please provide assignment content: ")
        due_date = input("Please provide due date: ")
        max_points = input("Plese set max points for this assignment: ")
        return title, content, due_date, max_points

    @staticmethod
    def get_grade_assignment_data():
        points = input("How much points do you want to add? ")
        owner_name = input("Whose assignment is it? ")
        return points, owner_name

    @staticmethod
    def get_user_data():
        name = input("Please provide user name: ")
        mail = input("Please provide user e-mail: ")
        password = input("Please set user password: ")
        return name, mail, password

    @staticmethod
    def staff_menu():
        options = ['Show students list', 'Log out']
        UserInterface.print_options_list(options)
        try:
            user_choice = int(input('Chose action: '))
        except ValueError:
            print("Wrong input")
        return options[user_choice - 1]

    @staticmethod
    def boss_menu():
        options = ['Add a mentor', 'Remove a mentor', 'Edit mentor data', 'Show mentors list', 'Show students list',
                   'Log out']
        UserInterface.print_options_list(options)
        try:
            user_choice = int(input('Chose action: '))
        except ValueError:
            print("Wrong input")
        return options[user_choice - 1]

    @staticmethod
    def print_options_list(list):
        """print indices (each increased by 1) and elements from provided list as a column"""
        for index, option in enumerate(list):
            print('  (' + (str(index + 1)) + ') ' + str(option))

    @staticmethod
    def show_list(user_list):
        for user in user_list:
            print(user.User.get_name())