import csv
from itertools import count

# opening the CSV file
with open('output_dataset\\final_output.csv', mode ='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)
    count_negative = 0
    count_positive = 0
    count_zero = 0
    sum = 0
    j=0
    total_positive = 0
    total_negative = 0
    # displaying the contents of the CSV file
    for line in csvFile:
        if(j==0):
            j=j+1
            continue
        if(float(line[-1]) < 0):
            count_negative = count_negative+1
            total_negative = total_negative + float(line[-1])
        elif(float(line[-1]) > 0):
            count_positive = count_positive+1
            total_positive = total_positive + float(line[-1])
        else:
            count_zero = count_zero + 1
        sum = sum + float(line[-2])
# Creating list contain all element
data = [['Total Orders - Correctly Charged',count_zero,sum],
["Total Orders - Over Charged",count_negative,total_negative],
["Total Orders - Under Charged",count_positive,total_positive]]


# # writing the file in summary_output.csv
header = ["field","count","sum"]
csv_file = "output_dataset\\summary_output.csv"
try:
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile,)
        writer.writerow(header)
        writer.writerows(data)

except IOError:
    print("I/O error")
