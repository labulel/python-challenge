import os
import csv
csvpath = os.path.join("Resources","03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
# calculate the number of months
    row_count= 0
    PnL = 0
    PL =[]
    Delta =[]
    for row in csvreader:
        row_count = row_count+1
        PnL = PnL + int(row[1])
        PL.append(int(row[1]))
    for i in range(len(PL)):
        if i == 0:
            Delta.append (0)
        else:
            Delta.append (PL[i]-PL[i-1])
    Ave_chg = round(sum(Delta)/(row_count-1),2)
        
print(f"Total Months: {row_count}")
print(f"Total: ${PnL}")
print(f"Average Change: ${Ave_chg}")


