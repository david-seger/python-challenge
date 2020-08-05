# Polling Data Challenge
# Read election_data.csv from the resources directory.  The dataset
# is in 3 columns - Voter Id, County, Candidate.
# Analyze votes and calculate :
#   Total number of votes cast
#   Complete list of candidates that received votes
#   The percentage of votes for each candidate won
#   The total number of votes for each candidate won
#   The winner of the election based on popular vote
#   Output should be sent to the terminal and to a .txt file

import os
import csv

total_votes = 0
candidate = dict()
candidate_name = ''
winner_name = ''
total_candidate_votes = 0
percent_of_votes = 0.000
formatted_percent = ''


election_data = os.path.join('Resources', 'election_data.csv')

# read through the budget data file

with open(election_data) as electionfile:

    # this defines teh csv.reader using election and tells it the delimiter
    csvreader = csv.reader(electionfile, delimiter=',')

    # Read the header row first as we don't needd that in our list
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name in candidate:
            #if candidate already in dictionary add 1 to vote count
            candidate[candidate_name] = candidate[candidate_name] + 1
        else:
            #if candidate not in dictionary default the name and vote count of 1
            candidate[candidate_name] = 1

# Print Election Results

print('Election Results')
print('-------------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------------')

# Iterate over key/value pairs in dict and print them
for key, value in candidate.items():
    percent_of_votes = (value/total_votes) * 100
    #https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
    print(key, ': ', "{:.3f}".format(percent_of_votes), '%   (', value, ')')
    if value > total_candidate_votes:
        winner_name = key
        total_candidate_votes = value

print('-------------------------------')
print(f'Winner: {winner_name}')
print('-------------------------------')    
