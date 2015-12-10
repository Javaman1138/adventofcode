import numpy

def parse_command(command):
    if command.find("turn on") == 0:
        command = command.replace('turn on', '')
        command = command.replace(' through ', ',')
        coords = get_coordinates(command)
        turn_on(coords[0], coords[1], coords[2], coords[3])
    elif command.find("turn off") == 0:
        command = command.replace('turn off', '')
        command = command.replace(' through ', ',')
        coords = get_coordinates(command)
        turn_off(coords[0], coords[1], coords[2], coords[3])
    elif command.find("toggle") == 0:
        command = command.replace('toggle', '')
        command = command.replace(' through ', ',')
        coords = get_coordinates(command)
        toggle(coords[0], coords[1], coords[2], coords[3])

def get_coordinates(command):
    command = command.replace(' through ', ',')
    return map(int, command.split(','))    
   
def turn_on( x, y, xx, yy):
    for ex in range(x, xx+1):
        for why in range(y, yy+1):
            Matrix[ex][why] += 1

def turn_off (x, y, xx, yy):
    for ex in range(x, xx+1):
        for why in range(y, yy+1):
            if Matrix[ex][why] > 0:
            	Matrix[ex][why] -= 1

def toggle(x, y, xx, yy):
    for ex in range(x, xx+1):
        for why in range(y,yy+1):
            Matrix[ex][why] += 2

Matrix = numpy.zeros(shape=(1000,1000),dtype=numpy.int32)

f = open('day6_data.txt', 'r')
for line in f:
    parse_command(line)
   
print Matrix
print numpy.sum(Matrix)


