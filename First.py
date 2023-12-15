from datetime import datetime, date, time, timezone
import Dataentry
import Initial_set_up
import os, sys
import pandas as pd
import reporting as r

print(f'Current date with time: {datetime.now()}')
dd = date.today().isoformat()
print("Ddd is", dd)
#file_name = Initial_set_up.initial_input(dd=date.today().isoformat())
#Dataentry.daily_input(file_name, dd=date.today().isoformat())
print("CWD is", os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("CWD is NOW", os.getcwd())
   # Get the input from the user

if os.path.exists("sample.csv"):
    file_name = "sample.csv"
    print("File exists")
else:
    file_name = "sample.csv"
    Initial_set_up.initial_input(file_name,dd)
    # Save the input to a file
print("Your csv file name is", file_name, "and it is in the directory", os.getcwd())
print("This csv file is your database of drinks")
print()
print("Now we go to the main menu")
print()
while True:
    print()
    print("Choice #1 is a placeholder for a filename, I have already hardcoded the file name to sample.csv")
    print("Press 2 To enter your daily drinks")
    print("Press 3 To Report out your drinking history.")
    print("Press 4 to get out of this.")
    x = int(input("enter your choice here:"))

    if x == 1:
        print()
    elif x == 2:
        Dataentry.daily_input(file_name, dd)
        print("ok SO FAR SO GOOD")
    elif x == 3:
        print("Now we go to the reporting.py module")
        data = r.read_data_from_csv(file_name)
        r.report_out_as_dictated_by_user()
    elif x == 4:
        break

    else:
        print("Invalid number or something else")

    # break
  
