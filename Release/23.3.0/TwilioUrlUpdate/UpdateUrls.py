import csv
import sys
print("Environment:", sys.argv[1])
with open("ClientList.csv") as clientList:
  reader_obj = csv.reader(clientList)
  for row in reader_obj:
    print("row - ", row)
    print("row[0] - ", row[0])
    print("row[1] - ", row[1])
    print("row[2] - ", row[2])
