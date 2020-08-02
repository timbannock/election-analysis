# Election Analysis

## Overview of Election Audit
An audit by the Colorado Board of Elections employee of a recent local congressional election.

The following key points are required:
1. Calculate the total number of votes cast.
2. Calculate the percentage of votes each candidate won and the total number of votes each candidate won.
3. Determine the winner of the election based on popular vote.
4. Determine the voting turnout of each county.
5. Determine which county had the largest voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.47.3

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The county results were:
	- Jefferson county had 10.5% (38,855) of the votes.
	- Denver had 82.8% (306,055) of the votes.
	- Arapahoe had 6.7% (24,801) of the votes.
- Denver had the largest voter turnout at 306,055 votes, 82.8% of the total votes.
- The candidate results were:
	- Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes.
	- Diana DeGette recieved 73.8% of the vote and 272,892 votes.
	- Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes.
- The winner of the election was:
	- Diana DeGette who received 73.8% of the vote and 272,892 votes.
- Below is an image of the results as they are printed out in the Python terminal:
![Election Results](https://github.com/timbannock/election-analysis/blob/master/analysis/election-results.PNG)

## Election Audit Summary
The python script used to analyze this election is flexible enough to work for nearly any election setup. It tallies votes by both county and candidate, and therefore can easily be utilized to break down election statistics, as well as ensure the accuracy of vote counts. Notably, the script is written in such a way that it is expandable to include virtually any number of candidates or counties without needing to be modified from its current form, making it useful country-wide.

The below code shows how the script includes a 'generic' candidate and county references, allowing for election data from any region with any candidates can be referenced with the same code, as long as the data is input with the same basic structure.

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_count = 0
largest_percentage = 0
```

Below is the format for the data, which can then be read by the above script or organized into lists and dictionaries of candidate names, county information, and vote counts.

```
Ballot ID,County,Candidate
```
