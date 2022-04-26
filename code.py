import math
import csv
with open("data.csv", newline = "") as f: 
  reader = csv.reader(f)
  files_data = list(reader)

data = files_data[0]

def mean(data):
  l = len(data)
  total = 0
  for i in data:
    total += int(i)
  mean = total/l
  return mean
squaredlist = []
for b in data:
  a = int(b)-mean(data)
  a = a**2
  squaredlist.append(a)
  sum = 0
for i in squaredlist:
  sum += i
result = sum/(len(data)-1)
standarddeviation = math.sqrt(result)
print(standarddeviation)