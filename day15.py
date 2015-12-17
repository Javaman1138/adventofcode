
import itertools

data = {}

f1 = open('day15_data.txt', 'r')
for line in f1:
    parts = line.replace(",","").split(" ")
    
    ingredient = parts[0]
    capacity = int(parts[2])
    durability = int(parts[4])
    flavor = int(parts[6])
    texture = int(parts[8])
    calories = int(parts[10])

    data[ingredient] = {"capacity":capacity, 
    		        "durability":durability, 
    		        "flavor":flavor,
    		        "texture":texture,
    		        "calories":calories}

print data

def build_combinations():
    for perm in itertools.permutations(range(0,100), len(data.keys())):
        if sum(perm) == 100:
            combinations.append(perm)

def calculate(): 
    max_value = 0
    keys = data.keys()
    for combo in combinations:
        c = 0
        d = 0
        f = 0
        t = 0
        cal = 0
        print combo
        for idx,amount in enumerate(combo):
            ingredient = keys[idx]
            
            c_calc = data[ingredient]['capacity'] * amount
            d_calc = data[ingredient]['durability'] * amount
            f_calc = data[ingredient]['flavor'] * amount
            t_calc = data[ingredient]['texture'] * amount
            cal_calc = data[ingredient]['calories'] * amount

            c += c_calc
            d += d_calc
            f += f_calc
            t += t_calc
            cal += cal_calc

        if c < 0:
            c = 0
        if d < 0:
            d = 0
        if f < 0:
            f = 0
        if t < 0:
            t = 0
        
        total = c * d * f * t
        if (total > max_value) and (cal <= 500):
            max_value = total
    
    return max_value

combinations = []
build_combinations()

max_value = 0
max_value = calculate()
print max_value
