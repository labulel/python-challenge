import os
import csv
csvpath = os.path.join("Resources","03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    row_count= 0
    PnL = 0
    PL =[]
    Delta =[]
    Dt = []
    for row in csvreader:
        row_count = row_count+1
        PnL = PnL + int(row[1])
        PL.append(int(row[1]))
        Dt.append(row[0])
    for i in range(len(PL)):
        if i == 0:
            Delta.append (0)
        else:
            Delta.append (PL[i]-PL[i-1])
    
    max_chg_index = Delta.index(max(Delta))
    max_chg_date = Dt[max_chg_index]
    min_chg_index = Delta.index(min(Delta))
    min_chg_date = Dt[min_chg_index]
    Ave_chg = round(sum(Delta)/(row_count-1),2)
    Max_chg = max(Delta)
    Max_position = Delta.index(Max_chg)
    greatest_increase_month = Dt[Max_position] 

#write results to a new txt file: 
PyBank = os.path.join("..","PyBank","Analysis","PyBank_analysis.txt")
with open(PyBank,"w") as csvfile:
    csvfile.write("Financial Analysis\n")
    csvfile.write("-------------------------\n")
    csvfile.write(f"Total Months: {row_count}\n")
    csvfile.write(f"Total: ${PnL}\n")
    csvfile.write(f"Average Change: ${Ave_chg}\n")
    csvfile.write(f"Greatest Increase in Profits: {max_chg_date} (${max(Delta)})\n")
    csvfile.write(f"Greatest Decrease in Profits: {min_chg_date} (${min(Delta)})\n")
