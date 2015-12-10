

length_sum = 0
memory_sum = 0

f1 = open('day8_data.txt', 'r')
for line in f1:
        actual_line = line.strip()
	length_sum += len(actual_line)
	
	mem_line = actual_line[1:-1].decode('string_escape')
	memory_sum += len(mem_line)
	
print "{0} - {1} = {2}".format(length_sum, memory_sum, length_sum-memory_sum)

import re
length_sum = 0
memory_sum = 0

f2 = open('day8_data.txt', 'r')
for line in f2:
        actual_line = line.strip()
	length_sum += len(actual_line)
	
	mem_line = "\"" + re.escape(actual_line) + "\""
	memory_sum += len(mem_line)
	
print "{0} - {1} = {2}".format(memory_sum, length_sum, memory_sum-length_sum)




