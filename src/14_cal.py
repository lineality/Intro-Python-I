# 14
# GGA
# 
# to do: figure out how to have input parameters into a .py file...
# 
"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.
This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# get user input "args" when the .py file is run
# sets variable 'args' to hold whatever number of inputs are entered
# e.g. in the form: 14_cal.py [month] [year] 
args = sys.argv

# inspection items
print(type(args))
print(type(args[1]))
print(type(args[2]))
print(len(args))
print(args)


# if no user input, the program sets current month
month = datetime.now().month
year = datetime.now().year

# Q: the first argument is the function itself?


# check to see how many inputs
if (len(args) > 3) or (len(args) == 1):
    # use build in function to make printed calendar
    tc = calendar.TextCalendar()
    # Print calendar for default month and year
    print(tc.prmonth(year, month))
    if len(args) > 3:
        print ("error, please use this format (no brakets): '14_cal.py month year'")

else:
    month_test = int(args[1])
    print("type is", type(month_test))
    if (month_test < 1) or (month_test > 12):
        print ("error, please use this format (no brakets): '14_cal.py month year'")
        
    else:
        month = int(args[1])
        year = int(args[2])
        # use build in function to make printed calendar
        tc = calendar.TextCalendar()
        # Print calendar for default month and year
        print(tc.prmonth(year, month))
