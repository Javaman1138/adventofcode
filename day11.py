import re
from datetime import datetime

ignore_letters = ['i','o','l']

data = "hxbxwxba"
data = "hxbxxyzz"

def check_for_success(password):
    prev_char = " "
    seq_count = 0
    last_double_pos = -1
    double_count = 0
    has_seq_3 = False
    
    has_ignored_letters = [c for c in ignore_letters if c in password]
    if has_ignored_letters:
        return False
        
    for i, c in enumerate(password):
        #check for double
        if prev_char == c and (i - last_double_pos) > 1:
            double_count += 1
            last_double_pos = i
            
        #sequence of 3 check
        pre = int(prev_char.encode("hex"), 16)
        cur = int(c.encode("hex"), 16)
        dif = cur - pre
        if dif == 1 and seq_count > 0:
            has_seq_3 = True
        elif dif == 1:
            seq_count += 1
        else:
            seq_count = 0
    
        prev_char = c
        
    return (double_count > 1) and has_seq_3
    
def replace_char(data_string, position, char):
    return data_string[:position] + char + data_string[position+1:]
    
def add_one(data_string, position):
    c = data_string[position]
    if c=='z':
        data_string = replace_char(data_string, position, 'a')
        return add_one(data_string, position-1)
    else:
        h = c.encode("hex")
        x = int(h,16) + 1
        st = "%x" % x
        data_string = replace_char(data_string, position, st.decode('hex'))
        return data_string

startTime = datetime.now()

data = add_one(data,7)
while not check_for_success(data):
    data = add_one(data, 7)
    if check_for_success(data):
        print data
        break
print datetime.now() - startTime