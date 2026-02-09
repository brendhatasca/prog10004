########
# Name: Brendha Tasca
# Student ID: 991554242
# Date: February 2nd, 2026
# Summary: Simple program to get student letter grade from grade percentage.
########

def get_grade_percentage():
    # Gets grade percentage between 0 - 100 from user
    while True:
        percentage_str = input("Enter grade percentag (0 - 100): ")
        if len(percentage_str) != 0:
            # Checks if number entered is not an empty string and 
            # if it is a decimal number
            percentage_num = float(percentage_str)
            if 0 > percentage_num:
                print(f"Cannot accept negative numbers ({percentage_num}).")
                print("Please enter a percentage between 0 - 100.\n")
            elif percentage_num > 100:
                print(f"Cannot accept numbers over 100 ({percentage_num}).")
                print("Please enter a percentage between 0 - 100.\n")
            else: 
                return percentage_num
        else:
            print("Invalid input. Please try again.\n")


def get_letter_grade_from_percentage(percentage: float):
    # Converts percentage grade into equivalent letter grade

    if percentage >= 90:
        print("Student grade is A+")
    elif percentage >= 80:
        print("Student grade is A")
    elif percentage >= 75:
        print("Student grade is B+")
    elif percentage >= 70:
        print("Student grade is B")
    elif percentage >= 65:
        print("Student grade is C+")
    elif percentage >= 60:
        print("Student grade is C")
    elif percentage >= 80:
        print("Student grade is D")
    else:
        print("Student grade is F")

def main():
    # Gets grade percentage from user and prints equivalent letter grade.
    grade_percentage = get_grade_percentage()
    get_letter_grade_from_percentage(grade_percentage)


if __name__ == "__main__":
    main()