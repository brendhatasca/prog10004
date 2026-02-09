def isLeapYear(year):
    # Check if given year is a leap year

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
    
def main():
    # Ask user to input an year and returns true or false 
    # depending if it is a leap year or not

    year = int(input("Enter a year: "))
    print(isLeapYear(year))

main()