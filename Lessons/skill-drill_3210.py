counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

print("----------------------------------------------------*")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) +" registered voters.")

print("----------------------------------------------------*")

# 3.2.11 Printing Formats and f-strings

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

print("----------------------------------------------------*")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
        f"You received {candidate_votes} number of votes. "
        f"The total number of votes in the election was {total_votes}. "
        f"You received {candidate_votes / total_votes * 100}% of the total votes. ")

print(message_to_candidate)

print("----------------------------------------------------*")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
        f"You received {candidate_votes:,} number of votes. "
        f"The total number of votes in the election was {total_votes:,}. "
        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

print(message_to_candidate)

