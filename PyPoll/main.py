import os
import csv

# Variables
PercentVotes= []
Candidates= []
NumberVotes=[]
TotalVotes= 0

#path to collect data from Resources folder
csvpath = os.path.join("Resources", "election_data.csv") 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header= next(csvreader)
       
    # Read each row of data after the header
    for row in csvreader:
        print(f"CSV Header: {csv_header}")

        #The total number of votes cast
        TotalVotes=TotalVotes+1

        #A complete list of candidates who received votes

        #The percentage of votes each candidate won

        #The total number of votes each candidate won

        #The winner of the election based on popular vote
