import csv
import os
from datetime import date
def initial_input(file_name,dd):

    # Save the input to a file
    with open(file_name, "w") as file:
        fieldnames = ["Date", "Type of Drink", "Ounces of Drink", "Drink's ABV", \
                      "Drink's Alcohol Content", "Number of Standard Drinks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"Date": "Date", "Type of Drink": "Type of Drink", "Ounces of Drink": "Ounces", \
                         "Drink's ABV": "ABV Percentage", "Drink's Alcohol Content": "Total Alcohol Ounces", \
                            "Number of Standard Drinks": "Effective Number of Drinks"})
        print(file_name)
        file.close()


    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        print("Here the Header of the file you entered:")
        for row in reader:
            print(row["Date"], row["Type of Drink"], row["Ounces of Drink"], row["Drink's ABV"], row["Drink's Alcohol Content"], row["Number of Standard Drinks"])
        file.close()    
    return file_name
