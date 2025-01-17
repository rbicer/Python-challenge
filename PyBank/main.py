# Creates file paths across Operating Systems
import os
# Module for reading CSV files    
import csv

# Variables
greatest_increase_date = []
greatest_increase_value= 0
total_months = 0
average_change = 0
greatest_decrease_date= []
greatest_decrease_value = 0
total_Profits_Losses = 0
change_in_revenue= []
dates= []

#path to collect data from Resources folder
csvpath = os.path.join("Resources", "budget_data.csv") 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header= next(csvreader)
       
    
    # Read each row of data after the header
    for row in csvreader:
    
        # The total number of months included in the dataset
        total_months= total_months +1

        # The net total amount of "Profit/Losses" over the entire period
        total_Profits_Losses= total_Profits_Losses+int(row[1])
        
        
        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        dates.append(row[0])

        if (total_months == 1):
            previousProfitLoss = int(row[1])
        else:
            change_Profit_Losses= int(row[1]) - previousProfitLoss
            change_in_revenue.append(change_Profit_Losses)

            previousProfitLoss = int(row[1])

        # The greatest increase in profits (date and amount) over the entire period
            greatest_increase_value= max(change_in_revenue)
            greatest_index_value= change_in_revenue.index(greatest_increase_value)
            greatest_index_date= dates[greatest_index_value+1]
        

        #  The greatest decrease in losses (date and amount) over the entire period
            greatest_decrease_value= min(change_in_revenue)
            lowest_index_value= change_in_revenue.index(greatest_decrease_value)
            lowest_index_date= dates[lowest_index_value+1]


#print outcomes 
print("Financial Analysis")
print("________________________")
print("Total Months: ", str(total_months))
print("Total Profit: $", str(total_Profits_Losses))
#print("Changes in Profit Loss: $", str(change_in_revenue)) #This is a test
print("Average Change: $", str(round(sum(change_in_revenue)/len(change_in_revenue),2)))
print("Greatest Increase in Profits: ", greatest_index_date, "$", str(max(change_in_revenue)))
print("Greatest Decrease in Profits: ", lowest_index_date, "$", str(min(change_in_revenue)))

# Text File ``
output =open('output.txt', 'w') 
# Lines in the Text File
text1= "Financial Analysis"
text2= "----------------------"
text3= "Total Months: " + str(total_months)
text4= "Total Profits Losses: $" + str(total_Profits_Losses)
text5= "Average Change: $" + str(round(sum(change_in_revenue)/len(change_in_revenue),2))
text6= "Greatest Increase in Profits: " + greatest_index_date +"  " + "$" + str(greatest_increase_value)
text7= "Greatest Decrease in Profits: " +  lowest_index_date+ "  " + "$" + str(greatest_decrease_value)
output.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n" .format(text1,text2,text3,text4,text5,text6,text7))