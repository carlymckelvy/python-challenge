import os
import csv

#Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#Assign values to variables
month_count = 0
net_total = 0
change = 0
current_value = 0
month_change = 0
prev_value = 0
months = []
change_list = []
average_change = 0
total_change = 0
total_months = 0
greatest_inc = 0
greatest_dec = 0
   
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

        #Find net total of profit/loss over entire period
        net_total = net_total + int(row[1])
   
        #Determine average of changes in profit/loss over entire period
        current_value = int(row[1])
        change += current_value

        #If no change, continue
        if month_count == 1:
            prev_value = current_value
            continue
    
        #Otherwise, calculate change in value
        else:
            change = current_value - prev_value

            #Append to months list
            months.append(row[0])

            #Append to change list
            change_list.append(change)
        
            #Set for next loop
            prev_value = current_value

    #Sum of change list
    total_change = sum(change_list)

    #Calculate average change over time (subtract 1 for # of changes, not months)
    average_change = round((total_change/(month_count - 1)), 2)
    
    #Determine greatest increase (date and amout) over entire period
    greatest_inc = max(change_list)
    greatest_inc_index = change_list.index(greatest_inc)  
    greatest_inc_month = months[greatest_inc_index]

    #Determine greatest decrease (date and amount) over entire period
    greatest_dec = min(change_list)
    greatest_dec_index = change_list.index(greatest_dec)
    greatest_dec_month = months[greatest_dec_index]


   
    #Print financial analysis with all stats
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months:  {month_count}")
    print(f"Total:  ${net_total}")
    print(f"Average Change:  ${average_change}")
    print(f"Greatest Increase in Profits:  {greatest_inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits:  {greatest_dec_month} (${greatest_dec})")

    
    #Export text file
    fa_file = os.path.join("Analysis", "financial_analysis.txt")
    
    #Create txt file
    with open(fa_file, "w+") as outfile:
        outfile.write("Financial Analysis\n")
        outfile.write("----------------------\n")
        outfile.write(f"Total Months:  {month_count}\n")
        outfile.write(f"Total:  ${net_total}\n")
        outfile.write(f"Average Change:  ${average_change}\n")
        outfile.write(f"Greatest Increase in Profits:  {greatest_inc_month} (${greatest_inc})\n")
        outfile.write(f"Greatest Decrease in Profits:  {greatest_dec_month} (${greatest_dec})\n")
    