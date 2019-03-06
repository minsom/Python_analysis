# PyBank

import os
import csv

csvpath=os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    # create empty lists to store data
    month=[]
    profit=[]

    for row in csvreader:
        # make a list of month 
        month.append(str(row[0]))
        # make a list of profit/losses
        profit.append(int(row[1]))
    
    # count the number of elements (monts) in the dataset
    total_month=len(month)

    # sum of profit/losses column
    total = sum(profit)

    # make a list of changes in profit/losses
    change_list = []
    for i in range(total_month-1):
        change_list.append(profit[i+1]-profit[i])

    # sum of changes
    total_changes = sum(change_list)

    # average of changes in profit/losses, round 2 decimal places
    average_changes = round((total_changes / (total_month-1)),2)
    # calculate the greatest increase in profits
    max_profit=max(change_list)
    # calculate the greatest decrease in profits
    min_profit=min(change_list)
    
    # month index of the greatest increase in profits in the month list (+1 required because length of the change_list is 1 shorter)
    max_month = change_list.index(max_profit) + 1
    # month index of the greatest decrease in profits in the month list 
    min_month = change_list.index(min_profit) + 1

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total}
Average Change: ${average_changes}
Greatest Increase in Profits: {month[max_month]} (${max_profit})
Greatest Decrease in Profits: {month[min_month]} (${min_profit})
"""
print(output)

output_bank = os.path.join("bank.txt")

with open(output_bank, 'w') as textfile:

    print(output, file=textfile)

# with open(outpath, "w",newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     # Header
#     writer.writerow(["Total Month", "Total", "Average Change","Greatest Increase in Profits","Greatest Decrease in Profits"])
#     writer.writerow([total_month,total,average_changes,)



