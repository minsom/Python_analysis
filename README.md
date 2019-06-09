# 1. Financial Data
![Revenue](Images/revenue-per-lead.jpg)
A Python script([PyBank/main.py](PyBank/main.py)) that analyzes the financial records([budget](PyBank/Resources/budget_data.csv)) of a selected company to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
  
'PyBank/main.py' prints the analysis to the terminal and export a text file with the results.
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```


# 2. Poll Data
![Vote-Counting](Images/Vote_counting.jpg)
A Python script([PyPoll/main.py](PyPoll/main.py)) that analyzes a set of poll data([votes](PyPoll/Resources/election_data.csv)) and calculates each of the following:
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
 
 'PyPoll/main.py' prints the analysis to the terminal and export a text file with the results.
   ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
