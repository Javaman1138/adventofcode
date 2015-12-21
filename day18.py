from datetime import datetime
import itertools
import copy

data = []
matrix_length = 0
matrix_height = 0

f1 = open('day18_data.txt', 'r')
for idx,line in enumerate(f1):
    data.append([])
    for i,c in enumerate(line.strip()):
       data[idx].append(c)

data[0][0] = '#'
data[0][len(data)-1] = '#'
data[len(data)-1][0] = '#'
data[len(data)-1][len(data)-1] = '#'

copy_data = copy.deepcopy(data)

print data

def is_on(x, y):
    if x < 0 or y < 0:
        return None
    if x >= len(data) or y >= len(data):
        return None
    if data[x][y] == '#':
        return True
    else:
        return False
 
def check_neighbors(x, y):
    on_neighbor_count = 0
    if is_on(x-1, y-1):
        on_neighbor_count += 1
    if is_on(x, y-1):
        on_neighbor_count += 1
    if is_on(x+1, y-1):
        on_neighbor_count += 1
    if is_on(x-1, y):
        on_neighbor_count += 1
    if is_on(x+1, y):
        on_neighbor_count += 1
    if is_on(x-1, y+1):
        on_neighbor_count += 1
    if is_on(x, y+1):
        on_neighbor_count += 1
    if is_on(x+1, y+1):
        on_neighbor_count += 1

    return on_neighbor_count
    
    
for step in range(0, 100): 
    copy_data = copy.deepcopy(data)
    
    for rowidx, row in enumerate(data):
        for colidx, col in enumerate(data[rowidx]):
    
            if (rowidx==0 and colidx==0) or (rowidx==0 and colidx==len(data)-1) or\
               (rowidx==len(data)-1 and colidx==0) or (rowidx==len(data)-1 and colidx==len(data)-1):
                pass
            elif is_on(rowidx, colidx) and check_neighbors(rowidx, colidx) in [2,3]:
                pass
            elif not is_on(rowidx, colidx) and check_neighbors(rowidx, colidx) == 3:
                copy_data[rowidx][colidx] = '#'
            else:
                copy_data[rowidx][colidx] = '.'
 
    data = copy.deepcopy(copy_data)



on_count = 0
for rowidx, row in enumerate(data):
    for colidx, col in enumerate(data[rowidx]):
        if data[rowidx][colidx] == '#':
            on_count += 1
            
print 'on count=' + str(on_count)
