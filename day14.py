
import itertools

data = {}

f1 = open('day14_data.txt', 'r')
for line in f1:
    parts = line.split(" ")
    
    reindeer = parts[0]
    fly_distance = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])

    data[reindeer] = {"dist":fly_distance, 
    		      "fly_time":fly_time, 
    		      "rest_time":rest_time,
    		      "status":{"fly":fly_time, "rest":0},
    		      "total_distance":0,
    		      "points":0}

def add_up_points():
    #calculate points
    totals_thus_far = [{x:data[x]['total_distance']} for x in data]
    max_total = max([data[x]['total_distance'] for x in data])        
    winners = [x for x in data if data[x]['total_distance'] == max_total]
    for winner in winners:
        data[winner]['points'] += 1

for race_time in range(0, 2503):
    for reindeer in data.keys():
        fly_status = data[reindeer]['status']['fly']
        rest_status = data[reindeer]['status']['rest']
        if fly_status and (fly_status <= data[reindeer]['fly_time']):
            distance_traveled = data[reindeer]['dist']
            data[reindeer]['total_distance'] += distance_traveled
            data[reindeer]['status']['fly'] -= 1
            if data[reindeer]['status']['fly'] == 0:
                data[reindeer]['status']['rest'] = data[reindeer]['rest_time']
        elif rest_status and (rest_status <= data[reindeer]['rest_time']):
            data[reindeer]['status']['rest'] -= 1
            if data[reindeer]['status']['rest'] == 0:
                data[reindeer]['status']['fly'] = data[reindeer]['fly_time']

    add_up_points()
    
print data

max_distance = 0
max_points = 0
for reindeer in data.keys():
    print "{0}: d={1}, p={2}".format(reindeer, data[reindeer]['total_distance'],data[reindeer]['points'])
    if data[reindeer]['total_distance'] > max_distance:
        max_distance = data[reindeer]['total_distance']
    if data[reindeer]['points'] > max_points:
        max_points = data[reindeer]['points']

print "MAX Distance = " + str(max_distance)
print "MAX Points   = " + str(max_points)