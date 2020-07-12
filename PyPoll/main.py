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
cand0 = format(round(((cand_votes0 / voter_count) * 100), 3), '.3f')
cand1 = format(round(((cand_votes1 / voter_count) * 100), 3), '.3f')
cand2 = format(round(((cand_votes2 / voter_count) * 100), 3), '.3f')
cand3 = format(round(((cand_votes3 / voter_count) * 100), 3), '.3f')

#Creat list of percentages
cand_perc = [cand0, cand1, cand2, cand3]

#Zip list together
zipped = zip(candidate_list, cand_perc, vote_tally)
FINAL = list(zipped)


#Determine winner of election based on popluar vote
winner_vote = max(vote_tally)
winner_ind = vote_tally.index(winner_vote)
winner_cand = candidate_list[winner_ind]


# election results
print("Election Results")
print("----------------------")
for c in FINAL:
    print(f"{c[0]}:  {c[1]}% ({c[2]})")
print("----------------------")
print(f"Winner:  {winner_cand}")
print("----------------------")


#Export text file
election_file = os.path.join("Analysis", "election_analysis.txt")

#Create txt file
with open(election_file, "w+") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------\n")
    for c in FINAL:
        outfile.write(f"{c[0]}:  {c[1]}% ({c[2]})\n")
    outfile.write("----------------------\n")
    outfile.write(f"Winner:  {winner_cand}\n")
    outfile.write("----------------------\n")
