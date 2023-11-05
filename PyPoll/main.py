# import module
import csv

# file paths
file_to_load = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis.txt"

# vote counter
total_votes = 0

# candidates and their vote counters
candidate_options = []
candidate_votes = {}

# create variables for winner
winning_candidate = ""
winning_count = 0

# open csv
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    
    # loop
    for row in reader:
        
        # add to vote count
        total_votes = total_votes + 1
        
        # get candidate name
        candidate_name = row["Candidate"]
        
        # is name already in list?
        if candidate_name not in candidate_options:
            
            # add to list
            candidate_options.append(candidate_name)
            
            # add candidate vote
            candidate_votes[candidate_name]=0
            
        # add vote to count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print results to file
with open(file_to_output, "w") as txt_file:

    # print final vote count
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )
    print(election_results)
    
    # save to text file
    txt_file.write(election_results)
    
    # loop to determine winner
    for candidate in candidate_votes:
        
        # retrieve vote count and %
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # who won
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        # print individual results to terminal
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        
        # save vote count to text file
        txt_file.write(voter_output)
        
    # print winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    
    # add to text file
    txt_file.write(winning_candidate_summary)
        
        
