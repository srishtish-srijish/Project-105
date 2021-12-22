
import math



# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To sort the data to get the list.
data = file_data[0]

#getting the mean
# data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100] #list of x or y
# data=[60,61,65,63,98,99,90,95,91,96]

#Step 1: finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean


#Step 2:subtract the mean from all the values and squaring the result
# squaring and getting the values
squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

#Step 3: getting the sum of all the elements in the square list

sum =0
for i in squared_list:
    sum =sum + i

#step 4: dividing the sum of the squares by n-1
result = sum/ (len(data)-1)

#Step 5: getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)
# print("derived using predefined function ",statistics.stdev(data))
