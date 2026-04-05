
def get_student_data():
    name = input("Enter student name: ")
    maths = float(input("Enter Maths marks: "))
    english = float(input("Enter English marks: "))
    science = float(input("Enter Science marks: "))
    kiswahili = float(input("Enter Kiswahili marks: "))
    social_studies = float(input("Enter Social Studies marks: "))

    marks = [maths, english, science, kiswahili, social_studies]
    return name, marks
