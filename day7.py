
data = {}
calculated = {}

def calculate(key):
	print 'key=' + key
	try:
	    return int(key)
	except:
	    pass
	
	if key not in calculated:
	    source = data.get(key)
            print 'source=' + source
	
            if source.find('AND') >= 0:
                print 'AND ' + source
                sources = source.split(' AND ')
                o1 = calculate(sources[0])
                o2 = calculate(sources[1])
                calculated[key] = o1 & o2
            elif source.find('OR') >= 0:
                print 'OR ' + source
                sources = source.split(' OR ')
                o1 = calculate(sources[0])
                o2 = calculate(sources[1])
                calculated[key] = o1 | o2
            elif source.find('LSHIFT') >= 0:
                print 'LEFT SHIFT ' + source
                sources = source.split(' LSHIFT ')
                o1 = calculate(sources[0])
                o2 = calculate(sources[1])
                calculated[key] = o1 << o2
            elif source.find('RSHIFT') >= 0:
                print 'RIGHT SHIFT ' + source
                sources = source.split(' RSHIFT ')
                o1 = calculate(sources[0])
                o2 = calculate(sources[1])
                calculated[key] = o1 >> o2
            elif source.find('NOT') >= 0:
                print 'NOT ' + source
                source = source.replace('NOT ','')
                o1 = calculate(source)
                calculated[key] = ~o1
            else:
                print 'ASSIGN ' + source
                calculated[key] = calculate(source)

            if calculated[key] < 0:
                calculated[key] = calculated[key] & 0xffff
        
        
        return calculated[key]
            
f = open('day7_data.txt', 'r')
for line in f:
    parts = line.split('->')
    source = parts[0].strip()
    target = parts[1].strip()
    data[target] = source     

part1_val = calculate('a')
print part1_val

print 'part 2'

data = {}
calculated = {'b': part1_val}
f = open('day7_data.txt', 'r')
for line in f:
    parts = line.split('->')
    source = parts[0].strip()
    target = parts[1].strip()
    data[target] = source  

part2_val = calculate('a')
print part2_val




        

