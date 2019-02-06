import os
import csv

candidates = []

budgetCSV = os.path.join('..', 'Resources', 'election_data.csv')

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    for row in csvreader:
        total += 1

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
length = 0
for candidate in candidates:
    length += 1
Vote_count = [0] * length

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        for i in range(length):
            if candidates[i] == row[2]:
                Vote_count[i] += 1
#print(Vote_count)                

Percent_list = []
for i in range(length):
    Percent_list.append('{:.3%}'.format(round((int(Vote_count[i])/ int(total)), 3)))
#print(Percent_list)

Max_value = max(Percent_list)
#print(Max_value)
indexmax = 0
for j in range(length):
    if Max_value == Percent_list[j]:
        indexmax = j


#Percent_list = [0] * length
#Percent_list[0] = round((int(Vote_count[0])/ int(total))*100, 3)
#Percent_list[1] = round((int(Vote_count[1])/ int(total))*100, 3)
#Percent_list[2] = round((int(Vote_count[2])/ int(total))*100, 3)
#Percent_list[3] = round((int(Vote_count[3])/ int(total))*100, 3)

list_of_lists = [candidates, Percent_list, Vote_count]

print("Election Results")
print("----------------------")
print(f"Total Votes: " + str(total))
print("----------------------")
#for a, b, c in (candidates, Percent_list, Vote_count):
    #print(a, b, c)
for a in zip(*list_of_lists):
    print(a)
#for candidate, percent, vote in zip(candidates, Percent_list, Vote_count):
    #print(candidate, percent, vote)
print("----------------------")
print("Winner is: " + candidates[indexmax])



