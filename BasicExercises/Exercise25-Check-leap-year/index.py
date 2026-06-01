#PROBLEM: Write a program that takes a year as input and determines if it is a leap year.
#A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
#Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
#PURPOSE: This exercise is vital for mastering “Complex Conditional Logic.” A leap year isn’t just “every 4 years”; there are specific exceptions for century years. This forces the programmer to use nested if statements or compound logical operators (and/or).

def check_leap_year(year):
    if ( year % 4 == 0 and year % 100 == 0) or year % 400 !=0 :
        print(f"{year} is a Leap Year")
    else:
        print(f'{year} is not a Leap Year')

check_leap_year(2024)