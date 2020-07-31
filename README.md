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

## Election Audit Summary
The python script used to analyze this election is flexible enough to work for nearly any election setup. It tallies votes by both county and candidate, and therefore can easily be utilized to break down election statistics, as well as ensure the accuracy of vote counts. Notably, the script is written in such a way that it is expandable to include virtually any number of candidates or counties without needing to be modified from its current form, making it useful country-wide.
