import os
import csv

budgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    for row in csvreader:
        total += 1
with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    netProfit = 0
    for row in csvreader:
        netProfit += int(row[1])

lists = []
with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        lists.append(int(row[1]))

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Total =[]
    for row in csvreader:
        lists.append(row[1])

for prices in lists:
    opening_price = int(lists[0])
    closing_price = int(lists[-1])
print(opening_price)
print(closing_price)

length = 0
average_change = 0
length_months = int(len(lists))
average_change = round((closing_price - opening_price) / (total - 1), 2)

Average_change_list = []
i = 2
for i in range(len(lists)):
    value_before = int(lists[i-1])
    value_next = int(lists[i])
    Average_change =  value_next - value_before
    Average_change_list.append(Average_change)
minValue = min(Average_change_list)
maxValue = max(Average_change_list)

indexmax = 0
indexmin = 0
for value in Average_change_list:
    for j in range(len(Average_change_list)):
        if minValue == Average_change_list[j]:
            indexmin = j
        elif maxValue == Average_change_list[j]:
            indexmax = j

original_value_min = int(lists[indexmin])
original_value_max = int(lists[indexmax])

datemax = []
datemin = []
with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if original_value_max == int(row[1]):
            datemax.append(row[0])
        elif original_value_min == int(row[1]):
            datemin.append(row[0])

#print(datemin)
import datetime
dtmin = datetime.datetime.strptime(datemin[0],'%y-%b').strftime('%b-%Y')
dtmax =datetime.datetime.strptime(datemax[0],'%y-%b').strftime('%b-%Y')
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total))
print("Total: $" + str(netProfit))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(dtmax) + " ($" + str(maxValue) + ")")
print("Greatest Decrease in Profits: " + str(dtmin) + " ($" + str(minValue) + ")")
