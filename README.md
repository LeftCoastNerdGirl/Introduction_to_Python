# python-challenge


This project is an introduction to using Python to prepare data and perform analysis on it.

The first part of the challenge is called PyBank. The instructions given task the student with creating a Python script to analyze the financial records of the example company. We were given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Using Python, the csv datafile is imported and lists for month count and profit are created. Using a for loop to inerate through the dataset, rows are added to both empty lists. A second for loop is used to compare each new entry to the previous one, creating a list of monthly changes. Using max and min functions, we can then determine the months with the greatest increase and greatest decrease, respectively.

Financial Analysis

------------------------------
Total Months: 86
Total Revenue: $22564198
Greatest Increase in Revenue: 16-Aug ($1862002)
Greatest Decrease in Revenue: 14-Feb ($-1825558)




The second part of the challenge is called PyPoll. In this Challenge, the student is tasked with helping a small, rural town modernize its vote-counting process. We were given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

Python was used to import the csv date file. Lists were created to store data from the file: candidates name, number of votes, and percent of overall votes. Using a for loop, the script moves through each row of data and stores the candidate's information in the created lists. Within the loop, the candidate name in the new row is compared to the list of candidates, to either update the vote count if candidate is listed, or append the candidate if they are not. The output of this loop is a summary of candidate names and their total votes.

In an additional step, a for loop is again used to compare the candidate's total votes to the sum of all votes cast to calcuate the percent of total votes. These datapoints are then used to determine the winning candidate.

Election Results
---------------------------
Total Votes: 369711
---------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
