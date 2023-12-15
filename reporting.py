import requests
from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd
import csv
import os

def read_data_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def report_out_as_dictated_by_user():
    print("Here we now pull up a file to manipulate as directed by the user")   
    while True:
        print()
        print("Choose #1 to see your history as you entered it.")
        print("Choose #2 report by a date range")
        print("Choose #3 To delete your file")
        print("Choose #4 to get out of this.")
        x = int(input("enter your choice here:"))
        if x == 1:
            results = read_data_from_csv("sample.csv")
            s = pd.DataFrame(results[1:], columns=results[0]) # this formats the data into a table using pandas
            print("Here is your history as you entered it:")
            print(s.to_string(index=False)) # this prints the table without the index        
            
        elif x == 2:
            print("We reach out for the def report_by_date_range")
            report_by_date_range()
            #wb, ws = report_by_date_range()
            #print(wb)
            #print(ws)
        elif x == 3:
            print("We reach out for the def delete_file")
            print("Read the next stuff carefully")
            delete_file()

        elif x == 4:
            break

        else:
            print("Invalid number")

def report_by_date_range():
    #First, I get the dates to bound the report from the user
    beg_date = "2023-12-01" #input("Enter the beginning date of the range you want to see: ")
    end_date = "2023-12-31" #input("Enter the ending date of the range you want to see: ")
    #Second, I have been saving everything as 'sample.csv' so I want to ensure it is all there
    if os.path.exists("sample.csv"):
        file_name = "sample.csv"
        print(os.getcwd())
        print("File exists")
    else:
        print("File does not exist")
        return
    #Third, I want to change that csv file to an excel file, so I can use pandas to manipulate it
    
    pd.read_csv('sample.csv').to_excel('report.xlsx')
    path = os.path.join(os.getcwd(), 'report.xlsx')
    print("Path is", path)
    #wb = load_workbook(path)
    #ws = wb.active

    #Fourth - we sort the data by date
    xl = pd.ExcelFile('report.xlsx')
    df = xl.parse("Sheet1")
    df = df.sort_values(by="Date")
    print("Before we filter by date:  ",df)
    print()
    #Fifth - we filter the data by date range
    print("The date range is", beg_date, "to", end_date)
    df = df[(df['Date'] >= beg_date) & (df['Date'] <= end_date)]
    print(df)

def delete_file():
    print("We are now going to delete the file")
    if os.path.exists("sample.csv"):
        print("###################################################")
        print("Do you really, really want to delete the file?")
        print("###################################################")
        print("Press 1 to delete the file")
        print("Press 2 to get out of this")
        x = int(input("enter your choice here:"))
        if x == 1:
            os.remove("sample.csv")
            print("File deleted")
        elif x == 2:
            return
    else:
        print("File does not exist")
        return
