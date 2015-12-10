test_data = ["London to Dublin = 464",
		"London to Belfast = 518",
		"Dublin to Belfast = 141",
		"NY to Belfast = 100",
		"NY to London = 200",
		"NY to Dublin = 300"]

#test_data = ["London to Dublin = 464",
#		"London to Belfast = 518",
#		"Dublin to Belfast = 141"]

distances = {}
start_points = []

f1 = open('day9_data.txt', 'r')
for line in test_data:
        distance_split = line.split("=")
        miles = int(distance_split[1].strip())
        name_split =  distance_split[0].split('to')
        name1 = name_split[0].strip()
        name2 = name_split[1].strip()
        
        print "{0} to {1} = {2}".format(name1, name2, miles)
        if (distances.has_key(name1)):
            distances_for_name1 = distances[name1]
            distances_for_name1[name2] = miles
        else:
            distances[name1] = {name2: miles}
            start_points.append(name1)
        
        if (distances.has_key(name2)):
            distances_for_name2 = distances[name2]
            distances_for_name2[name1] = miles
        else:
            distances[name2] = {name1: miles}
            start_points.append(name2)

print start_points
print distances

def start_to_end(start, end):
        
	if not end:
	    return 0
	print 'distance {0} to {1} = {2}'.format(start, end, distances[start][end])
        return distances[start][end]


def traverse(visited, point, level):
    
    children = [x for x in distances[point] if x not in visited]
    pref = ""
    for x in range(0,level):
       pref += "."
       
    print pref + 'POINT ' + point
    print pref + 'child ' + str(children)
    print pref + 'visit ' + str(visited)
    
    if not children:
        return 0
        
    for idx, child in enumerate(children):
        print pref + str(idx)
        total = 0
        if child not in visited:
            child_visited = set(visited)
            child_visited.add(child)
            print pref + str(child_visited)
            print pref + 'start to end {0} + {1} = {2}'.format(point, child, start_to_end(point, child))
            return start_to_end(point, child) + traverse(child_visited, child, level+1)
            #print total
        else:
            total += 0
        print pref + 'sub total= ' + str(total) + '\n'

    return total
    
def trav(visited, point, level, total):
    pref = ""
    for x in range(0,level):
       pref += "."
    print pref + point
    print pref + str(visited)
    
    children = [x for x in distances[point] if x not in visited]
    print pref + str(children)
    
    if not children:
        return 0
        
    for child in children:
        new_visited = set(visited)
        new_visited.add(child)
        current_distance = start_to_end(point, child)
        return current_distance + trav(new_visited, child, level+1, current_distance)
        

print 'test-----------'

print trav(set(['London']), 'London', 1, 0)
print '----------------\n'




print '- permutations version -'
min_distance = 99999999
max_distance = 0

import itertools
permutations =  list(itertools.permutations(start_points))

for direction in permutations:
    total_distance = 0
    for idx in range(0, len(direction)-1):
        total_distance += distances[direction[idx]][direction[idx+1]]
    if total_distance < min_distance:
        min_distance = total_distance
    if total_distance > max_distance:
        max_distance = total_distance
        
print 'min distance = ' + str(min_distance)
print 'max distance = ' + str(max_distance)
    	