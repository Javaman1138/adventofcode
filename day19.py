from datetime import datetime
import itertools
import re
import copy

data = {}
molecule_chain = ""
combos = set()

f1 = open('day19_data.txt', 'r')
for line in f1:
    conversion = line.split('=>')
    if len(conversion) == 2:
        key =conversion[0].strip()
        val =conversion[1].strip()
        if key in data:
            data[key].append(val)
        else:
            data[key] = [val]

    elif len(conversion[0].strip()) > 0:
        molecule_chain = conversion[0].strip()
        
print "data = " + str(data)
print "chain = " + str(molecule_chain)

for substitution in data:
    print '--------' + str(substitution)
    positions = [m.start() for m in re.finditer(substitution, molecule_chain)]
    print "pos=" + str(positions)

    if not positions:
        continue
        
    sub_vals = data.get(substitution)
    print "sub_vals=" + str(sub_vals)

    products = [p for p in itertools.product(sub_vals, repeat=len(sub_vals))]

    for product in products:
        for position in positions:
            for p in product:
                temp = list(molecule_chain)
                temp[int(position)] = p
                if len(substitution) > 1:
                    del temp[int(position)+1]
                combos.add("".join(temp))
        
print '-combos-'
print combos
print len(combos)

