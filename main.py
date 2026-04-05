from input_handler import get_student_data
from calculator import calculate_total, calculate_average
from grader import get_grade
from messages import get_performance_message


def main():
    name, marks = get_student_data()

    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    grade = get_grade(average)
    message = get_performance_message(grade)

    print("\n----- STUDENT RESULT -----")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)
    print("Performance Message:", message)


main()
