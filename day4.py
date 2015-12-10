
input = "iwrupvqb"

import hashlib

for x in range(0, 100000000):
    test = "{0}{1}".format(input,x)
    m = hashlib.md5(test)
    hex = m.hexdigest()
    if hex[:6] == "000000":
        print x
        print hex
        break
