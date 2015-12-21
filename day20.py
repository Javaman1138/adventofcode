from datetime import datetime

def justthefactorsmaam(n):
    return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

wanted = 36000000

f1 = False
f2 = False
cur = 1
while True:
    f = justthefactorsmaam(cur)
    found1 = 10*sum(f)
    found2 = 11*sum([x for x in f if cur/x <= 50])
    if not f1 and found1 >= wanted:
        print 1, cur, found1, f
        f1 = True
    if not f2 and found2 >= wanted:
        print 2, cur, found2, f
        f2 = True

    if f1 and f2:
        break

    cur = cur+1



# original --- very very very slow 

#startTime = datetime.now()
#for house in range(831000,850000):
#    total = 0
    
#    for elf in range (1, house+1):
#        if house % elf == 0:
#           total += elf * 10  
#        elif elf == 1:
#           total += elf * 10  

#    if house % 1000 == 0:
#       print "house {0} to {1}".format(house, total)

#    elif total >= 36000000:
#       print "house {0} to {1}".format(house, total)
#       break

print datetime.now() - startTime