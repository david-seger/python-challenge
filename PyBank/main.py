
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

analysis_list = []
change_list = []
date_list = []
row_count =  0
difference_count = 0
total_profit_loss = 0
total_difference = 0
average_profit_loss = 0.00
greatest_increase_month = ''
greatest_increase = 0 
greatest_decrease_month = ''
greatest_decrease = 0


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
        row_count = row_count + 1
        total_profit_loss = total_profit_loss + int(row[1])
        analysis_list.append(int(row[1]))
        date_list.append(row[0])
# Now look for the greatest increase/decrease in the list we
# created while reading the csv file

for c in range (1, row_count) :
    difference = analysis_list[c] - analysis_list[c-1]
    change_list.append(difference)
    total_difference = total_difference + difference
    difference_count = difference_count + 1
    if difference > greatest_increase:
        greatest_increase=difference
        greatest_increase_month = date_list[c]
    elif difference < greatest_decrease:
        greatest_decrease = difference
        greatest_decrease_month = date_list[c]

average_profit_loss = total_difference / difference_count
average_profit_loss = round(average_profit_loss, 2)

#print results to terminals

print('Financial Analysis')
print('---------------------------------------------------------------')
print(f'Total Months . . : {row_count}')
print(f'Total  . . . . . : ${total_profit_loss}')
print(f'Average Change . : ${average_profit_loss}')
print(f'Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})')


#https://pythonexamples.org/python-write-string-to-text-file/
#this will write the necessary analysis line to a text file

analysis_file = open("analysis.txt", "w")

n=analysis_file.write('Financial Analysis\n')
n=analysis_file.write('---------------------------------------------------------------\n')
n=analysis_file.write(f'Total Months . . : {row_count}\n')
n=analysis_file.write(f'Total  . . . . . : ${total_profit_loss}\n')
n=analysis_file.write(f'Average Change . : ${average_profit_loss}\n')
n=analysis_file.write(f'Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})\n')
n=analysis_file.write(f'Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})\n')

analysis_file.close()