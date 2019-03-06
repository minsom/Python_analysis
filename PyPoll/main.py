# PyPoll

import os
import csv

csvpath=os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)
    
    # create empty lists to store data
    Khan=[]
    Correy=[]
    Li=[]
    OTooley=[]

    for row in csvreader:
        
        # create a list of voters with unique candidate values
        if row[2] == "Khan":
            Khan.append(row[0])
        elif row[2] == "Correy":
            Correy.append(row[0])
        elif row[2] == "Li":
            Li.append(row[0])
        elif row[2] == "O'Tooley":
            OTooley.append(row[0])
        

# count total votes by using a length funtion    
total_votes=len(Khan)+len(Correy)+len(Li)+len(OTooley)
# count votes of each candidates
n_Khan=len(Khan)
n_Correy=len(Correy)
n_Li=len(Li)
n_OTooley=len(OTooley)
# calculate %
pct_Khan=round(n_Khan/total_votes*100,3)
pct_Correy=round(n_Correy/total_votes*100,3)
pct_Li=round(n_Li/total_votes*100,3)
pct_OTooley=round(n_OTooley/total_votes*100,3)

candidate={n_Khan:"Khan", n_Correy:"Correy", n_Li:"Li", n_OTooley:"O'Tooley"}
winner=candidate[max(n_Khan,n_Correy,n_Li,n_OTooley)]

# print(f"Election Results")
# print("----------------------------")
# print(f"Total Votes: {total_votes}")
# print("----------------------------")
# print(f"Khan: {pct_Khan}% ({n_Khan})")
# print(f"Correy: {pct_Correy}% ({n_Correy})")
# print(f"Li: {pct_Li}% ({n_Li})")
# print(f"O'Tookey: {pct_OTooley}% ({n_OTooley})")
# print("----------------------------")
# print(f"Winner: {winner}")
# print("----------------------------")
    
output = f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
Khan: {pct_Khan}% ({n_Khan})
Correy: {pct_Correy}% ({n_Correy})
Li: {pct_Li}% ({n_Li})
O'Tookey: {pct_OTooley}% ({n_OTooley})
----------------------------
Winner: {winner}
----------------------------
"""
print(output)

output_poll = os.path.join('poll.txt')

with open(output_poll, 'w') as textfile:

    print(output, file=textfile)

# output_poll = os.path.join('poll.txt')

# with open(output_poll, 'w') as textfile:
#     print(f"Election Results", file=textfile)
#     print("----------------------------",file=textfile)
#     print(f"Total Votes: {total_votes}",file=textfile)
#     print("----------------------------",file=textfile)
#     print(f"Khan: {pct_Khan}% ({n_Khan})",file=textfile)
#     print(f"Correy: {pct_Correy}% ({n_Correy})",file=textfile)
#     print(f"Li: {pct_Li}% ({n_Li})",file=textfile)
#     print(f"O'Tookey: {pct_OTooley}% ({n_OTooley})",file=textfile)
#     print("----------------------------",file=textfile)
#     print(f"Winner: {winner}",file=textfile)
#     print("----------------------------",file=textfile)