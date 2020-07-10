#Copy csv file to PyPoll folder
import shutil
newpath = shutil.copy("C:/Users/carly/Documents/bootcamp/myfork/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv","C:/Users/carly/Documents/bootcamp/myfork/python-challenge/PyPoll/Resources")

#Import modules
import os
import csv

#Create path to collect data
election_data = os.path.join("Resources", "election_data.csv")

#Assign values to variables


#Read the csv file
with open(election_data) as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    #Extract the header
    header = next(csvreader)

    #Loop through the data


        #Find total number of votes


        #Create list of candidates who recevied votes


        #Determine percentage of votes each candidate won


        #Determine total number of votes each candidate won


        #Determine winner of election based on popluar vote


    #Print election results
    # print("Financial Analysis")
    # print("----------------------")
    # print(f"Total Months:  {month_count}")
    # print(f"Total:  ${net_total}")
    # print(f"Average Change:  ${average_change}")
    # print(f"Greatest Increase in Profits:  {greatest_inc_month} (${greatest_inc})")
    # print(f"Greatest Decrease in Profits:  {greatest_dec_month} (${greatest_dec})")

    #  #Export text file
    # fa_file = os.path.join("Analysis", "financial_analysis.txt")
    
    # #Create txt file
    # with open(fa_file, "w+") as outfile:
    #     outfile.write("Financial Analysis\n")
    #     outfile.write("----------------------\n")
    #     outfile.write(f"Total Months:  {month_count}\n")
    #     outfile.write(f"Total:  ${net_total}\n")
    #     outfile.write(f"Average Change:  ${average_change}\n")
    #     outfile.write(f"Greatest Increase in Profits:  {greatest_inc_month} (${greatest_inc})\n")
    #     outfile.write(f"Greatest Decrease in Profits:  {greatest_dec_month} (${greatest_dec})\n")