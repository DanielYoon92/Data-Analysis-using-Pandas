#Dependencies
import pandas as pd
import os

#File Path
file_name = "election_data.csv"
dir = os.path.dirname(__file__)
csv_file = os.path.join(dir, "Resources", file_name)

#Read the CSV file
csv_df = pd.read_csv(csv_file)

#The total number of votes cast
total_votes = csv_df['Ballot ID'].count()

#A complete list of candidates who received votes
#Using print(candidates), can determine there are 3 unique candidates
candidates = csv_df['Candidate'].unique()

#The total number of votes each candidate won
candidate1 = 0;
candidate2 = 0;
candidate3 = 0;

for i in range(total_votes):
    if csv_df['Candidate'][i] == candidates[0]:
        candidate1 = 1 + candidate1
    elif csv_df['Candidate'][i] == candidates[1]:
        candidate2 = 1 + candidate2
    else:
        candidate3 = 1 + candidate3

#The percentage of votes each candidate won
#Divide each Candidates' votes by the total votes to get the percentage
#Round to 3 decimal places as per the output example
candidate1_percentage = round(candidate1 / total_votes * 100, 3) 
candidate2_percentage = round(candidate2 / total_votes * 100, 3)
candidate3_percentage = round(candidate3 / total_votes * 100, 3)

#The winner of the election based on popular vote
#By using describe function, can determine the top Candidate is Diana Degette
#print(winner)
winner = csv_df['Candidate'].describe()

#Print Result in Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {candidate1_percentage}% ({candidate1})")
print(f"{candidates[1]}: {candidate2_percentage}% ({candidate2})")
print(f"{candidates[2]}: {candidate3_percentage}% ({candidate3})")
print("-------------------------")
print(f"Winner: {candidates[1]}")

#Output to Text File
txt_filepath = os.path.join(dir,'PyPoll_Results.txt')

with open(txt_filepath, 'w') as text:
    text.write("Election Results" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"{candidates[0]}: {candidate1_percentage}% ({candidate1})" + "\n")
    text.write(f"{candidates[1]}: {candidate2_percentage}% ({candidate2})" + "\n")
    text.write(f"{candidates[2]}: {candidate3_percentage}% ({candidate3})" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {candidates[1]}" + "\n")