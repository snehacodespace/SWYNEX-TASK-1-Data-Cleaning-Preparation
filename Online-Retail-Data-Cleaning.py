import csv

with open("Online_Retail_Cleaned.csv", "r", encoding="utf-8") as file:
    data = csv.reader(file)

    for row in list(data)[:6]:
        print(row)


import csv

with open("Online_Retail_Cleaned.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file))

print("Total Rows:", len(data) - 1)
print("Total Columns:", len(data[0]))        