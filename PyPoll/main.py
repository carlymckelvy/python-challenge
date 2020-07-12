#Copy csv file to PyPoll folder
# import shutil
# newpath = shutil.copy("C:/Users/carly/Documents/bootcamp/myfork/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv","C:/Users/carly/Documents/bootcamp/myfork/python-challenge/PyPoll/Resources")

#Import modules
import os
import csv

#Create path to collect data
election_data = os.path.join("Resources", "election_data.csv")

#Assign values to variables
candidate = []
cand_votes0 = 0
cand_votes1 = 0
cand_votes2 = 0
cand_votes3 = 0
voter_count = 0
candidate_list = []




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

    #Find unique names within candidate list
    for new in candidate:
        if new not in candidate_list:
            candidate_list.append(new)

    #Count occurrence of each name within candidate list
    for row in candidate:
        if row == (candidate_list[0]):
            cand_votes0 = cand_votes0 + 1

        elif row == (candidate_list[1]):
            cand_votes1 = cand_votes1 + 1

        elif row == (candidate_list[2]):
            cand_votes2 = cand_votes2 + 1

        elif row == (candidate_list[3]):
            cand_votes3 = cand_votes3 + 1


#Create list of all candidate votes
vote_tally = [cand_votes0, cand_votes1, cand_votes2, cand_votes3]

#Convert vote numbers to percentages


#Zip candidate names and votes
final_tally = zip(candidate_list, vote_tally)
FINAL = dict(zip(candidate_list, vote_tally))

#print(FINAL)


     

    #Determine percentage of votes each candidate won
        


    #Determine winner of election based on popluar vote


    #Print election results
    # print("Election Results")
    # print("----------------------")
    # print(f"Khan:  {Khan_votes}")
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