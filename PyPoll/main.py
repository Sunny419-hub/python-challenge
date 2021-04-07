# Import the necessary dependencies
import os
import csv

# Read in a .csv file
csv_file = os.path.join("PyPoll", "Resources", "election_data.csv")

# Lists to store data
candidate_list = []

candidate_found = {}

#Improved Reading using CSV module
with open(csv_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # Assign your values to variables with descriptive names
    total_votes = 0
 
# Read each row of data after the header
    for row in csvreader:
        # Calculating the The total number of votes cast
      total_votes = total_votes + 1
      if row[2] not in candidate_list:
        candidate_list.append(row[2])
      candidate_found.setdefault(row[2],0) 
      candidate_found[row[2]] += 1

    # Making the candidate list      
    #for candidate in candidate_list:
        # Assigning value to the dictionary
        #candidate_found [row[2]] = 0
        #print(candidate)
     
    #for row in csvreader:
    #  if row[2] in candidate_list:
    #     candidate_found.setdefault(row[2],0) 
    #     candidate_found[row[2]] += 1
      
    #print (candidate_found)
    for n, v in candidate_found.items():
      print(n, (v/total_votes)*100,"%", (v))

    Winner = max(list(candidate_found.values()))
    
    print("Winner:", list(candidate_found.keys())[list(candidate_found.values()).index(Winner)])
# Specify the file to write to
###output_path = os.path.join("c:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyBank","new.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
###with open(output_path, 'w', newline='') as txtfile:
  ###txtwriter = csv.writer(txtfile, delimiter=',')
  ###txtwriter.writerow(["Election Results"])
  ###txtwriter.writerow(["-------------------------"])
  ###txtwriter.writerow(["[f"Total Votes: {total_votes}"]"])

###with open(output_path, 'r') as txtfile:
  ###lines = txtfile.read()
  ###print(lines)