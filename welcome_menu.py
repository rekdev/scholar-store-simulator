def show_welcome_menu():
    """
    Shows a welcome greet, asks for a student name and lastly returns it. 

    Returns:
        str: Student's name.
    """

    print("""+++SCHOLAR STORE+++
    Welcome, please fill the required information.""")

    student_name = input("Input the client name: ")

    return student_name
