"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

diff_phone_number = []

for data in texts:
    sending_number = data[0]
    receiving_number = data[1]

    if sending_number not in diff_phone_number:
        diff_phone_number.append(sending_number)
    if receiving_number not in diff_phone_number:
        diff_phone_number.append(receiving_number)

for data in calls:
    calling_number = data[0]
    receiving_number = data[1]

    if calling_number not in diff_phone_number:
        diff_phone_number.append(calling_number)
    if receiving_number not in diff_phone_number:
        diff_phone_number.append(receiving_number)

print(f'There are {len(diff_phone_number)} different telephone numbers in the records.')


