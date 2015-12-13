
import itertools

guest_list = set()
guest_list.add('Brian')
data = {'Brian':{'Carol':0, 'Eric':0, 'Bob':0, 'George':0, 'David':0, 'Alice':0, 'Mallory':0, 'Frank':0},
        'Carol':{'Brian':0},
        'Eric':{'Brian':0},
        'Bob':{'Brian':0},
        'George':{'Brian':0},
        'David':{'Brian':0},
        'Alice':{'Brian':0},
        'Mallory':{'Brian':0},
        'Frank':{'Brian':0},
        }

f1 = open('day13_data.txt', 'r')
for line in f1:
    line = line.replace("would ","").replace("happiness units by sitting next to ","").replace(".","")
    parts = line.split(" ")
    
    person = parts[0]
    if parts[1] == 'lose':
        happiness = 0 - int(parts[2])
    else:
        happiness = int(parts[2])
    neighbor = parts[3].strip()
    
    guest_list.add(person)
    if data.get(person):
        data[person][neighbor] = happiness
    else:
        data[person] = {neighbor: happiness}
        
    print "{0} {1} {2}".format(person, happiness, neighbor)
    
print data

total_happiness = 0
permutations =  list(itertools.permutations(guest_list)) 
for seating_order in permutations:
    
    configuration_total = 0
    for idx, person in enumerate(seating_order):
        
        if idx < (len(seating_order)-1):
            potential_neighbor = seating_order[idx+1]
        else:
            potential_neighbor = seating_order[0]

        direction1 = data[person][potential_neighbor]
        direction2 = data[potential_neighbor][person]
        configuration_total += (direction1 + direction2)
    if configuration_total > total_happiness:
        total_happiness = configuration_total
        
print total_happiness