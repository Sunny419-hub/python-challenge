# Import the necessary dependencies
import os
import csv
#Function that returns the arithmetic average of the changes in "Profit/Losses"
def average(changes_acum,total_mon):
    return (changes_acum) / (total_mon-1)
# Read in a .csv file
csv_file = os.path.join("Resources", "budget_data.csv")
#Improved Reading using CSV module
with open("budget_data.csv") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Assign your values to variables with descriptive names
    total = 0
    total_mon = 0
    last_pfls = 0
    new_pfls = 0
    changes_act = 0
    changes_acum = 0
    
    # Read each row of data after the header
    for row in csvreader:
        # Calculating the net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])
        # Calculating total number of months included in the dataset
        total_mon = total_mon + 1
        # Calculating the changes in "Profit/Losses" over the entire period   
        if (last_pfls)!= 0:
            new_pfls = int (row[1])
            changes_act = int (new_pfls) - int (last_pfls)
            changes_acum = int (changes_acum) + int (changes_act)
        last_pfls = int (row[1])

    #print(average(total,total_mon))
    #print(total)
    #print(total_mon)
    print(average(changes_acum,total_mon-1))