'''
  This program reads the American League baseball players, 2003, tsv file
    using the csv reader 
    and stores it in a list of dictionaries, one for each player
  Each line has the team, the player name, the salary and the position played.

  The program writes a report on the average salary per player to a txt file.
  The program writes the players who made less than $310,000 to a csv file
    using the csv writer with a header line suitable for excel.
'''

import csv

infile = 'albb.salaries.2003.csv'

# create new empty list
playersList = []

with open(infile, 'r') as csvfile:
    # the csv file reader returns a list of the csv items on each line
    ALReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')

    # from each line, a list of row items, put each element in a dictionary
    #   with a key representing the data
    for line in ALReader:
      # skip lines without data
      if line[0] == '' or line[0].startswith('American') or line[0].startswith('Team')\
            or line[0].startswith('Source'):
          continue
      else:
          try:
            # create a dictionary for each player
            player = {}
            # add each piece of data under a key representing that data
            player['team'] = line[0]
            player['name'] = line[1]
            player['sal'] = int(line[2].replace(',',''))
            player['position'] = line[3]
    
            # add this player to the list
            playersList.append(player)
    
          except IndexError:
            print ('Error: ', line)
csvfile.close()

print ("Read", len(playersList), "player data")


# Write a report text file with a title and the average of the salaries
# First create an output file name
outfile1 = infile.replace('csv', '') + 'report.txt'
# open the file for writing
fout1 = open(outfile1, 'w')

# write title at top of file
fout1.write("American League Baseball players average salary in 2003\n for players earning less than $310,000\n\n")

# comput the average salary over all players
total_salary = 0.0
for player in playersList:
  if player['sal'] < 310000:
    total_salary += player['sal']
average_salary = total_salary / len(playersList)

# write a report line as a string to the file
fout1.write('Average salary = ${:,.2f}'.format(average_salary))
fout1.close()