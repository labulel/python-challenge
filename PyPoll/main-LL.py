import os
import csv
csvpath = os.path.join("Resources","03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")
#Import and read csvfile:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header:
    csv_header = next(csvreader)
    #set starting value of running votes count:
    votes_count = 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    #create a list of candidates:
    candidates = [] 
    #create a dictionary of candidates and votes received:
    candidate_votes ={}
    #loop through the rows in the csv file:
    for row in csvreader:
        #update the running votes count:
        votes_count = votes_count+1
        if row[2] == "Khan":
            khan_count = khan_count + 1
        if row[2] == "Correy":
            correy_count = correy_count + 1
        if row[2] == "Li":
            li_count = li_count + 1
        if row[2] == "O'Tooley":
            otooley_count = otooley_count + 1
        
        #update the dictionary with candidates and their votes count:
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]]=0
        else:
            votes = candidate_votes[row[2]]+1
            candidate_votes[row[2]] = votes
    
    #define the winning candidate name as a string:
    winning_candidate = ""
    #set the starting point of the winner total votes count:
    winning_count = 0
    #looping through the candidiate_votes dictionary to identify the candidiate with the max vote count:
    for i in candidate_votes:
        if candidate_votes[i] > winning_count:
            winning_candidate = i
            winning_count = candidate_votes[i]
    
    #calculate the total votes per candidate and percentage of total votes:
    khan_percent = "{0:.2f}".format((khan_count/votes_count)*100)
    correy_percent = "{0:.2f}".format((correy_count/votes_count)*100)
    li_percent = "{0:.2f}".format((li_count/votes_count)*100)
    otooley_percent = "{0:.2f}".format((otooley_count/votes_count)*100)

#print summary results:
print ("Election Results")
print ("-------------------------")
print(f"Total Votes: {votes_count}")
print(f"Khan: {khan_percent}% {khan_count}")
print(f"Correy: {correy_percent}% {correy_count}")
print(f"Li: {li_percent}% {li_count}")
print(f"O'Tooley: {otooley_percent}% {otooley_count}")
print(f"Winner: {winning_candidate}")

#write results to a new txt file:       
PyPoll = os.path.join("..","PyPoll","Analysis","PyPoll_analysis.txt")
with open(PyPoll,"w") as csvfile:
    csvfile.write("Election Results\n")
    csvfile.write("-------------------------\n")
    csvfile.write(f"Total Votes: {votes_count}\n")
    csvfile.write(f"Khan: {khan_percent}% {khan_count}\n")
    csvfile.write(f"Correy: {correy_percent}% {correy_count}\n")
    csvfile.write(f"Li: {li_percent}% {li_count}\n")
    csvfile.write(f"O'Tooley: {otooley_percent}% {otooley_count}\n")
    csvfile.write("-------------------------\n")
    csvfile.write(f"Winner: {winning_candidate}\n")