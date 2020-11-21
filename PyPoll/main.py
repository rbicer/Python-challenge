import os
import csv

# Variables
PercentVotes= []
Candidates= []
NumberVotes=[]
TotalVotes= 0
poll_Dic= {}
WinnerVote= 0
WinnerPerson=[]
winner=[]

#path to collect data from Resources folder
csvpath = os.path.join("Resources", "election_data.csv") 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header= next(csvreader)
       
    # Read each row of data after the header
    for row in csvreader:
    
        #The total number of votes cast
        TotalVotes=TotalVotes+1

        #A complete list of candidates who received votes
        if row[2] in poll_Dic.keys():
            poll_Dic[row[2]]= poll_Dic[row[2]] +1

        else: 
            poll_Dic[row[2]]= 1  

        #The percentage of votes each candidate won
    for key, value in poll_Dic.items():
        NumberVotes.append(value)
        Candidates.append(key)

    for x in NumberVotes:
        PercentVotes.append((round((x/TotalVotes*100),3)))

    dataZipper=zip(Candidates, PercentVotes, NumberVotes)
       
    #The winner of the election based on popular vote
    Winnervote=max(NumberVotes)
    WinnerPerson=NumberVotes.index(Winnervote)
    winner= Candidates[WinnerPerson]

#Print Outcomes
print("ELECTION RESULTS")
print('-'* 31)
print("Total Votes:", str(TotalVotes))
print('-'*31)
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {PercentVotes[i]:.3f}% ({NumberVotes[i]})")
print('-'*31)
print("Winner:", winner)
print('-'*31)

#Text Files
output =open('output.txt', 'w')
text1= "ELECTION RESULTS"
text2= "-"*31
text3= "Total Votes:" + str(TotalVotes)
text4= "-"*31
output.write("{}\n{}\n{}\n{}\n".format(text1,text2,text3,text4))
dataZipper=zip(Candidates, PercentVotes, NumberVotes)
for i in range(len(Candidates)):
    text5=f"{Candidates[i]}: {PercentVotes[i]:.3f}% ({NumberVotes[i]})"
    output.write("{}\n".format(text5))
text6= "-"*31
text7="Winner:"+winner
text8= "-"*31
output.write("{}\n{}\n{}\n".format(text6,text7,text8))


