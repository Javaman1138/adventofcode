data = []

f = open('day2_data.txt', 'r')
for line in f:
    data.append(line)
    
print 'day 2'
print 'puzzle 1'

total_sq_feet = 0
for c in data:
    l,w,h = [int(s) for s in c.split('x')]
 
    side1 = (l*w)
    side2 = (w*h)
    side3 = (h*l)

    slack = min([side1,side2,side3])
    surface_area = 2*side1 + 2*side2 + 2*side3
    total_sq_feet +=  surface_area + slack

print total_sq_feet


print 'puzzle 2'

total_ribbon_feet = 0
for c in data:
    l,w,h = [int(s) for s in c.split('x')]

    side1 = (2*l) + (2*w)
    side2 = (2*w) + (2*h)
    side3 = (2*h) + (2*l)

    ribbon_length = min([side1,side2,side3])
    bow = l*w*h

    total_ribbon_feet += ribbon_length + bow

print total_ribbon_feet
