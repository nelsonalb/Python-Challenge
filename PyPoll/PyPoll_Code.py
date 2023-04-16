import csv
import os

# Set the path for the CSV file
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidate_percentages = {}
winner = ""

# Open the CSV file
with open(file_path) as election_data:
    csvreader = csv.reader(election_data)

    # Read the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Calculate the total number of votes cast
        total_votes += 1

        # Add the candidate's name to the dictionary if it doesn't already exist
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 0

        # Add a vote to the candidate's total
        candidate_votes[row[2]] += 1

    # Calculate the percentage of votes each candidate won
    for candidate in candidate_votes:
        candidate_percentages[candidate] = round((candidate_votes[candidate] / total_votes) * 100, 2)

    # Determine the winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis to the terminal
print("---------------------------------------------")
print("Election Results")
print("---------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]}% ({candidate_votes[candidate]})")
print("---------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------")

# Export a text file with the results
with open("PyPoll/Analysis/Election_Results.txt", "w") as analysis_file:
    analysis_file.write("---------------------------------------------\n")
    analysis_file.write("Election Results\n")
    analysis_file.write("---------------------------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}\n")
    analysis_file.write("---------------------------------------------\n")
    for candidate in candidate_votes:
        analysis_file.write(f"{candidate}: {candidate_percentages[candidate]}% ({candidate_votes[candidate]})\n")
    analysis_file.write("---------------------------------------------\n")
    analysis_file.write(f"Winner: {winner}\n")
    analysis_file.write("---------------------------------------------\n")
