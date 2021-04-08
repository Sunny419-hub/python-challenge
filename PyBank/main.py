# Import the necessary dependencies
import os
import csv
#Function that returns the arithmetic average of the changes in "Profit/Losses"
def average(changes_acum,total_mon):
    return int (changes_acum) / (total_mon-1)

#Function that returns the maximum value
def increase(increase,new,date2,date_increase2):
  if increase > new:
    return increase,date_increase2
  else:
    return new,date2
#Function that returns the minimun value
def decrease(decrease,new,date2,date_decrease2):
  if decrease < new:
    return decrease, date_decrease2
  else:
    return new, date2
    
# Read in a .csv file
csv_file = os.path.join("Resources", "budget_data.csv")
#Improved Reading using CSV module
with open(csv_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Assign your values to variables with descriptive names
    total = 0
    total_mon = 0
    last_pfls = 0
    new_pfls = 0
    changes_act = 0
    changes_acum = 0
    increase2 = 0
    new = 0
    decrease2 = 0
    date_increase2 = ''
    date_decrease2 = ''

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
        # Calculating the Greatest Increase and Decrease in Profits   
        new = changes_act 
        increase2,date_increase2 = increase(int (increase2),int (new),row[0],date_increase2)
        decrease2,date_decrease2 = decrease(int (decrease2),int (new),row[0],date_decrease2)
           
# Specify the file to write to
#output_path = os.path.join("c:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyBank","new.txt")
output_path = os.path.join("c:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyBank\\analysis","new.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
  txtwriter = csv.writer(txtfile, delimiter=',')
  txtwriter.writerow(["Financial Analysis"])
  txtwriter.writerow(["----------------------------"])
  #print(total_mon)
  txtwriter.writerow([f"Total Months: {total_mon}"])
  #print(total)
  txtwriter.writerow([f"Total: ${total}"])
  #print(average(changes_acum,total_mon))
  txtwriter.writerow([f"Average Change: ${round(average(changes_acum,(total_mon)),2)}"])
  #print(increase2) #print(date_increase2)
  txtwriter.writerow([f"Greatest Increase in Profits: {date_increase2} ${increase2}"])
  #print(decrease2) #print(date_decrease2)
  txtwriter.writerow([f"Greatest Decrease in Profits: {date_decrease2} ${decrease2}"])

with open(output_path, 'r') as txtfile:
  lines = txtfile.read()
  print(lines)