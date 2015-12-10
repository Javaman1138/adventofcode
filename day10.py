
data = "1113222113"

for x in range(0,50):
    print 'DATA -->  {0} - {1}'.format(x,data)
    
    new_data = ""
    prev_char = ""
    count = 0
    for i, curr_char in enumerate(data):
    
        if not prev_char and (i == len(data)-1):
            new_data += "{0}{1}".format(1, curr_char)
            continue
            
        if not prev_char:
            prev_char = curr_char
            count += 1

        elif (prev_char) and (curr_char != prev_char):
            new_data += "{0}{1}".format(count, prev_char)
            count = 1
            prev_char = curr_char
            if (i == len(data)-1):
                new_data += "{0}{1}".format(1, curr_char)
            
        elif (i == len(data)-1):
            count += 1
            new_data += "{0}{1}".format(count, curr_char)
        else:
            count += 1

    data = new_data
    
print len(data)