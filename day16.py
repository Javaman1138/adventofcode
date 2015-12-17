
import itertools

data = {}

f1 = open('day16_data.txt', 'r')
for line in f1:
    parts = line.split(":")
    aunt_id = parts[0].replace("Sue ",'')
    data[aunt_id] = {}
    
    info = line[len(aunt_id) + 5:]
    
    for detail in info.split(","):
        details = detail.split(":")
        
        detail_id = details[0].strip()
        detail_val = int(details[1].strip())
    	data[aunt_id][detail_id] = detail_val

match_data = {'children': 3,
		'cats': 7,
		'samoyeds': 2,
		'pomeranians': 3,
		'akitas': 0,
		'vizslas': 0,
		'goldfish': 5,
		'trees': 3,
		'cars': 2,
		'perfumes': 1}

highest_match_id = 0
highest_match_val = 0

for aunt in data:
    matches = 0
    print aunt
    details = data[aunt]
    for detail in details:
        if (detail in ["cats","trees"]) and (data[aunt][detail] > match_data[detail]):
                print 'GREATER THAN {0} {1}'.format( match_data[detail], detail)
		matches += 1
        elif (detail in ["pomeranians","goldfish"]) and (data[aunt][detail] < match_data[detail]):
        	print 'LESS THAN {0} {1}'.format( match_data[detail], detail)
		matches += 1
        elif (detail not in ["cats","trees","pomeranians","goldfish"]) and data[aunt][detail] == match_data[detail]:
                print 'MATCH {0} {1}'.format( match_data[detail], detail)
		matches += 1
    
    if matches > highest_match_val:
        highest_match_val = matches
        highest_match_id = aunt
        
print "highest id={0} value={1}".format(highest_match_id, highest_match_val)