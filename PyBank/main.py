
# PyBank
# Analyze financial records and calculate:
#   Total number of months included in dataset
#   Net Total Amount of 'Profit/Losses' over entire period
#   Average of the changes of 'Profit/Losses' over the entire period
#   The GreatestIncrease in profits (date/amount) over the entire period
#   The GreatestDecrease in losses (date/amount) over the entire period

import os
import csv

#define variables

total_months =  0                       # Count of Months in csv
prior_profit_loss = 0                   # Prior Month P/L
total_profit_loss = 0                   # Total P/L
average_change_profit_loss = 0.00       # Avg chg in P/L for periods
greatest_increase_month = ''            # Greatest increase - Month
greatest_increase = 0                   # Greatest increase - Dollar
greatest_decrease_month = ''            # Greatest decrease - Month
greatest_decrease = 0                   # Greatest decrease - Dollar
difference = 0                          # Diff between curr/prior month p/l

# Get the path for the budget data file

budget_data = os.path.join('Resources', 'budget_data.csv')

# read through the budget data file

with open(budget_data) as bankfile:

    # this defines teh csv.reader using bankfile and tells it the delimiter
    csvreader = csv.reader(bankfile, delimiter=',')
    # Read the header row first as we don't needd that in our list

    csv_header = next(csvreader)
 
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

        # Now calculate difference in current p/l - prior p/l
        # Keep running total of cumulative p/l
         
        if total_months > 1 :
            difference =  current_profit_loss - prior_profit_loss
            cumulative_profit_loss += difference
        else:
            cumulative_profit_loss=0
        
        prior_profit_loss = current_profit_loss
        
        # Check difference to see if this is the greatest increase
        # or decrease so far and if it is store the values
        if difference > greatest_increase:
            greatest_increase=difference
            greatest_increase_month = row[0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_month = row[0]

# Calculate Average Change in P/L
average_change_profit_loss =  round((cumulative_profit_loss / (total_months-1)),2)

# Define output into one variable formatted with all data this will
# allow us to write it once to the terminal and then to the output 
# text file

output = (
    f'\nFinancial Analysis\n'
    f'---------------------------------------------------------------\n'
    f'Total Months . . : {total_months}\n'
    f'Total  . . . . . : ${total_profit_loss}\n'
    f'Average Change . : ${average_change_profit_loss}\n'
    f'Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})\n'
    f'Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})\n')

#print results to terminals

print(output)

# Get the path for the analysis text file

analysis_file = os.path.join('Analysis', 'analysis.txt')

analysis_writer = open(analysis_file, "w")

n=analysis_writer.write(output)

analysis_writer.close()