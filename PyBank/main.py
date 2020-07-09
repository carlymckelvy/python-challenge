import os
import csv

#Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#Assign values to variables
month_count = 0
# start_profit = 0
# end_profit = 0
# net_total = 0
# greatest_inc = 0
# greates_dec = 0
   
#Read in the csv file
with open(budget_csv) as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    #Extract header row
    header = next(csvreader)
    
    #Loop through the data
    for row in csvreader:
    
        #Find number of lines
        month_count += 1
    print(month_count)


    #Define the function and have it accept file
# def print_analysis(budget):
#     date = str(budget[0])
#     profit_loss = int(budget[1])
  
#     #Find number of months
#     month_count = len(date)
#     print(month_count)

    #Find net total of profit/loss over entire period
    #net_total = start profit - end profit


    #Determine average of changes in profit/loss over entire period
    #change = net_total / month_count

    #Determine greatest increase (date and amout) over entire period
    #

    #Determine greatest decrease (date and amount) over entire period
    #




  


   
    #Print financial analysis with all stats
    # print("Financial Analysis")
    # print("----------------------")
    # print(f"Total Months:  {}")
    # print(f"TotalL  {}")
    # print(f"Average Change:  {}")
    # print(f"Greatest Increase in Profits:  {}")
    # print(f"Greates Decrease in Profits:  {}")