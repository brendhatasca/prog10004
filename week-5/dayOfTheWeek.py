########
# Name: Brendha Tasca
# Student ID: 991554242
# Date: February 2nd, 2026
# Summary: Simple program to get day of the week given number
# input by user.
########

def get_number():
    # Gets a number between 1 - 7 from the user
    while True:
        numb = int(input("Please enter a number (1-7): "))
        if 0 <= numb <= 7:
            return numb
        print("Invalid input. Please choose a number between 1-7.")

def get_day_of_the_week():
    # Get a day of the week from the user 
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("Please enter day of the week: ").lower().strip()
        if day in days_of_the_week:
            return day
        elif len(day) == 0:
            print("Name cannot be empty. Please enter a day of the week.")
            continue
        print("Not a valid input. Please enter a day of the week.")

def num_to_day(numb):
    # Prints day of the week for the given number.

    if numb == 1:
        print("It's Monday.")
    elif numb == 2: 
        print("It's Tuesday.")
    elif numb == 3:
        print("It's Wednesday.")
    elif numb == 4:
        print("It's Thursday.")
    elif numb == 5:
        print("It's Friday")
    else:
        print("It's the weekend.")

def day_to_num(day):
    # Prints the day-of-week number for the given day.

    if day == "monday":
        print(1)
    elif day == "tuesday":
        print(2)
    elif day == "wednesday":
        print(3)
    elif day == "thursday":
        print(4)
    elif day == "friday":
        print(5)
    elif day == "saturday":
        print(6)
    else:
        print(7)

def get_user_action():
    # Gets choice of action from user
    print("1. Get day of the week from number")
    print("2. Get number from the day of the week")

    OPTIONS = (1, 2)
    while True:
        action = input("Please select an action: ")
        if len(action) != 0 and action.isdigit():
            action_numb = int(action)
            if action_numb in OPTIONS:
                return action_numb
        else:
            print("Please choose a valid action from the menu.")
        # print("Not a valid action. Please select one from the menu.")

def main():
    action_num = get_user_action()
    if action_num == 1:
        num = get_number()
        num_to_day(num)
    elif action_num == 2:
        day = get_day_of_the_week()
        day_to_num(day)

if __name__ == "__main__":
    main()