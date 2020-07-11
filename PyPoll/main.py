#Copy csv file to PyPoll folder
# import shutil
# newpath = shutil.copy("C:/Users/carly/Documents/bootcamp/myfork/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv","C:/Users/carly/Documents/bootcamp/myfork/python-challenge/PyPoll/Resources")

#Import modules
import os
import csv

#Create path to collect data
election_data = os.path.join("Resources", "election_data.csv")

#Assign values to variables
Voter_ID = []
County = []
candidate = []
voter_count = 0
current_row = 0
prev_row = 0
candidate_list = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0



#Read the csv file
with open(election_data, 'r') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    #Extract the header
    header = next(csvreader)

    #Loop through the data
    for row in csvreader:

        #Find total number of votes        
        voter_count = voter_count + 1

        #candidate_list
        candidate.append(row[2])
        

    for new in candidate:
        if new not in candidate_list:
            candidate_list.append(new)
    for new in candidate_list:
        print(new)


        # current_row = str(row[2])
        # prev_row = (current_row - 1)

        # if row[2] == prev_row[2]:
        #     continue

        # else: 
        #     candidate_list.append(row[2])

 

     
        #Create a list of candidates who recevied votes from index 2
        

    #     #Determine total number of votes each candidate won
    #     #For loop if index 2 = candidate name, then add to counter
    #     #elseif = diff name, add 
    #     if row[2] 

        

            
         
    

    #Determine unique list of candidates


    

    #Determine percentage of votes each candidate won
        


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