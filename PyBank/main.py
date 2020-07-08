import os
import csv

#Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Define the data and have it accept the 'budget_data' as its sole parameter
def print_analysis(budget_data):

    #Assign values to variables
    date = int(budget_data[0])
    profit = int(budget_data[1])

    #Find total number of months in dataset
    #entire_period = last date - first date
    entire_period = 

    #Find net total of profit/loss over entire period
    #net_total = first profit - last profit


    #Determine average of changes in profit/loss over entire period
    #change = net_total / entire_period

    #Determine greatest increase (date and amout) over entire period
    #

    #Determine greatest decrease (date and amount) over entire period
    #

    #Print financial analysis with all stats

