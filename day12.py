import json
import re

f1 = open('day12_data.txt', 'r')
data = f1.read()

print data

numbers = re.findall(r'[-\d]+', data)
print numbers

total = 0
for number in numbers:
    total += int(number)

print total

j = json.loads(data)
print j

def parse_dict(d):

    total = 0
    
    for key in d:
        val = d[key]
        if val == 'red':
            return 0
        else:
            if type(val) is dict:
                total += parse_dict(val)
            elif type(val) is list:
                total += parse_list(val)
            elif type(val) is int:
                total += val
            
    return total

def parse_list(j):

    total = 0
    for x in j:
        if type(x) is list:
            total += parse_list(x)
        elif type(x) is dict:
            total += parse_dict(x)
        elif type(x) is int:
            total += x

    return total
    
print parse_list (j)