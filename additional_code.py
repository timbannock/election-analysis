===========================================================================
DATETIME CLASS
===========================================================================
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

===========================================================================
OPEN, READ AND CLOSE FILE
===========================================================================

# Assign a varialbe for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election reults and read the file.
election_data = open(file_to_load, 'r')
# To do: perform analysis.
# Close the file.
election_data.close()

===========================================================================
3.4.2: Open and Read Files Using Python
===========================================================================

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

===========================================================================
3.4.3 Write to Files with Python
===========================================================================
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file, each county on a separate line using newline escape sequence at end of each county name like this: \n.
     txt_file.write("Arapahoe\nDenver\nJefferson")
===========================================================================
# Skill Drill 3.4.3

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file, each county on a separate line using newline escape sequence at end of each county name like this: \n.
     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
===========================================================================
3.4.4: Read the Election Results
===========================================================================
# BASE SCRIPT

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

===========================================================================
# Added to the end of the base script, this will print every single row of the CSV

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

===========================================================================
# Added to the end of the base script, this will print just the first item (column) from each row

	# Print just the first item from each row
	for row in file_reader:
		print(row[0])

===========================================================================
# Added to the end of the base script, skip the header row of the CSV file, use the next() method

    headers = next(file_reader)

