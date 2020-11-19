import os         #starting with the csv libraries
import csv

budget_dataCSV = os.path.join("budget_data.csv") #path to my csv file

monthsTotal=0
Profits_Losses_Total=0
changes=0
profits=[]
dates=[]

with open(budget_dataCSV, newline = " ") as csvFile:  #open the csv file
    csvreader=csv.reader(csvFile, delimiter = " , ")


    

