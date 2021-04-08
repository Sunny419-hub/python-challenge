import os
import csv
from datetime import date, time, datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Lists to store data
emp_id = []
first_name = []
last_name = []
dob2 = []
ssn2 = []
found_state = []

# Set path for file
csv_file = os.path.join("Resources", "employee_data.csv")
with open(csv_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #Add the emp_id
        emp_id.append(row[0])
        
        #The Name column should be split into separate First Name and Last Name columns.
        first_name.append(row[1].split()[0])
        last_name.append(row[1].split()[1])
        
        #The DOB data should be re-written into MM/DD/YYYY format.
        dob = datetime.strptime(row[2], '%Y-%m-%d')
        dob2.append(dob.strftime('%m/%d/%Y'))

        #The SSN data should be re-written such that the first five numbers are hidden from view.
        ssn = row[3].split('-')[2]
        ssn2.append("***-**-"+ str(ssn))

        #The State data should be re-written as simple two-letter abbreviations.
        State = row[4]
        found_state.append(us_state_abbrev[State])

        
    # Zip lists together
    cleaned_csv = zip(emp_id, first_name, last_name, dob2, ssn2, found_state)

    # Set variable for output file
    output_file = os.path.join("c:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyBoss\\analysis","employee_data_converted.csv")

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
        # Write in zipped rows
        writer.writerows(cleaned_csv)

    with open(output_file, 'r') as txtfile:
        lines = txtfile.read()
        print(lines)