# Introduction to Python


This project is an introduction to using Python to prepare data and perform analysis on it.

The first part of the challenge is called PyBank. The instructions given task the student with creating a Python script to analyze the financial records of the example company. We were given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Using Python, the csv datafile is imported and lists for month count and profit are created. Using a for loop to inerate through the dataset, rows are added to both empty lists. A second for loop is used to compare each new entry to the previous one, creating a list of monthly changes. Using max and min functions, we can then determine the months with the greatest increase and greatest decrease, respectively.

![image](https://github.com/user-attachments/assets/dd9b190c-8ecf-4438-8e02-4e61eb241a69)


The second part of the challenge is called PyPoll. In this Challenge, the student is tasked with helping a small, rural town modernize its vote-counting process. We were given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

Python was used to import the csv date file. Lists were created to store data from the file: candidates name, number of votes, and percent of overall votes. Using a for loop, the script moves through each row of data and stores the candidate's information in the created lists. Within the loop, the candidate name in the new row is compared to the list of candidates, to either update the vote count if candidate is listed, or append the candidate if they are not. The output of this loop is a summary of candidate names and their total votes.

In an additional step, a for loop is again used to compare the candidate's total votes to the sum of all votes cast to calcuate the percent of total votes. These datapoints are then used to determine the winning candidate.

![image](https://github.com/user-attachments/assets/7dd3b6d9-fcd8-42a4-8347-6e20441cf82b)
