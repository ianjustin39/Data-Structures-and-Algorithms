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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set()
not_telemarketers_num = set()
prefix = '140'
for data in texts:
    not_telemarketers_num.add(data[0])
    not_telemarketers_num.add(data[1])
for data in calls:
    not_telemarketers_num.add(data[1])

for data in calls:
    call = data[0]
    if call not in not_telemarketers_num:
        telemarketers.add(call)

print('"These numbers could be telemarketers: "')
for num in sorted(telemarketers):
    print(num)
