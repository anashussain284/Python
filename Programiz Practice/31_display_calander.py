"""
Python Program to Display Calendar
@link: https://www.programiz.com/python-programming/examples/display-calendar
"""
import calendar

yy = int(input("Enter year in 4 digit: "))
mm = int(input("Enter month in 2 digit: "))

print(calendar.month(yy, mm))