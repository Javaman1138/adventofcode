from datetime import datetime
import itertools

data = []

f1 = open('day17_data.txt', 'r')
for line in f1:
    number = int(line.strip())
    data.append(number)

print data

#data = [20,15,10,5,5]

startTime = datetime.now()

print '************************'
#permutations =  list(itertools.permutations(data)) 
#print permutations

print '------------------------'
combo_count = 0
for x in range(2, len(data)):
    combinations = list(itertools.combinations(data, x))
    for combo in combinations:
        total = 0
        for item in combo:
            total += item
            
        if total == 150:
            print combo
            combo_count += 1

print datetime.now() - startTime
print combo_count