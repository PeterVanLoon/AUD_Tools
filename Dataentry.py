from datetime import datetime, date, time, timezone
import csv
import os
import sys
from datetime import date

opd = 0.6   # ounces of pure alcohol in a standard drink

def daily_input(file_name,dd):
    print("Please enter the following information:")
    #print(ddinput)
    ddinput = input("Enter today's date in this format: YYYY-MM-DD:")
    dd = date.fromisoformat(ddinput)
    print(dd)
    dt = input("Type of drink:")
    print()
    do = float(input("Ounces of drink:"))
    #print(type(do))
    print()
    dabv = float(input("Drink's ABV:"))
    #print(type(dabv))
    #print('{:.2f}%'.format(dabv))
    print()
    dalc = round(do * dabv, 2)
    #print(type(dalc))
    print()
    dperday = round(dalc / opd,2)
    print("Number of standard drinks this date: ", dperday)

    print()
    with open(file_name, "a",newline='') as file:
        fieldnames = ["Date", "Type of Drink", "Ounces of Drink", "Drink's ABV", "Drink's Alcohol Content", "Number of Standard Drinks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({"Date": dd, "Type of Drink": dt, "Ounces of Drink": do, "Drink's ABV": dabv, "Drink's Alcohol Content": dalc, "Number of Standard Drinks": dperday})
        print(file_name)
        file.close()

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        print("Here is the information you entered:")
        for row in reader:
            print(row["Date"], row["Type of Drink"], row["Ounces of Drink"], row["Drink's ABV"], row["Drink's Alcohol Content"], row["Number of Standard Drinks"])
        file.close()    


     
   
   
   
   
   
'''
    print("CWD is", os.getcwd())
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("CWD is NOW", os.getcwd())
    # Get the input from the user
    file_name = input("Please enter the name of the file you would like to save this information to: ")
    # Save the input to a file
    with open(file_name, "w") as file:
        fieldnames = ["Date", "Type of Drink", "Ounces of Drink", "Drink's ABV", "Drink's Alcohol Content", "Number of Standard Drinks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        print(file_name)
        file.close()
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["Date"], row["Type of Drink"], row["Ounces of Drink"], row["Drink's ABV"], row["Drink's Alcohol Content"], row["Number of Standard Drinks"])
        file.close()
"""
'''####'''
#dailyinput()