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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

Bangalore_number = set()
prefix_080 = '(080)'
prefix_789 = ['7', '8', '9']
prefix_140 = '140'
prefix_brackets = '(0'

for data in calls:
    calling_number = data[0]
    receiving_number = data[1]

    if calling_number.startswith(prefix_080):
        if receiving_number.startswith(tuple(prefix_789)):
            Bangalore_number.add(receiving_number[:4])

        if receiving_number.startswith(prefix_140):
            Bangalore_number.add(prefix_140)

        if receiving_number.startswith(prefix_brackets):
            Bangalore_number.add(receiving_number[receiving_number.index('('):receiving_number.index(')') + 1])

print(f'The numbers called by people in Bangalore have codes: ')
for num in sorted(Bangalore_number):
    print(num)


count1 = 0
count2 = 0
for data in calls:
    calling_number = data[0]
    receiving_number = data[1]

    if calling_number.startswith(prefix_080):
        count1 += 1
        if receiving_number.startswith(prefix_080):
            count2 += 1

print(f'{round(count2/count1 * 100, 2)} percent of calls from fixed lines in Bangalore are calls \n to other fixed lines in Bangalore.')