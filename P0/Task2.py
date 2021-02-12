"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
num_dict = dict()

for data in calls:
    calling_number = data[0]
    receiving_number = data[1]
    total_time = int(data[3])
    if calling_number in num_dict.keys():
        num_dict[calling_number] += total_time
    else:
        num_dict[calling_number] = total_time

    if receiving_number in num_dict.keys():
        num_dict[receiving_number] += total_time
    else:
        num_dict[receiving_number] = total_time

max_time_number = ''
max_time = 0
for num, time in num_dict.items():
    if time > max_time:
        max_time = time
        max_time_number = num

print(f'{max_time_number} spent the longest time, {max_time} seconds, on the phone during September 2016.')