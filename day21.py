import itertools

boss_hit_points = 109
boss_damage = 8
boss_armor = 2

weapons = {'dagger': {'cost':8, 'damage':4, 'armor':0},
	'shortsword': {'cost':10, 'damage':5, 'armor':0},
	'warhammer': {'cost':25, 'damage':6, 'armor':0},
	'longsowrd': {'cost':40, 'damage':7, 'armor':0},
	'greateaxe': {'cost':74, 'damage':8, 'armor':0}}

armours = {'none':{'cost':0, 'damage':0, 'armor':0},
        'Leather': {'cost':13, 'damage':0, 'armor':1},
	'chainmail': {'cost':31, 'damage':0, 'armor':2},
	'splintmail': {'cost':53, 'damage':0, 'armor':3},
	'bandedmail': {'cost':75, 'damage':0, 'armor':4},
	'platemail': {'cost':102, 'damage':0, 'armor':5}}
	
rings = {'none':{'cost':0, 'damage':0, 'armor':0},
        'plus 1': {'cost':25, 'damage':1, 'armor':0},
	'plus 2': {'cost':50, 'damage':2, 'armor':0},
	'plus 3': {'cost':100, 'damage':3, 'armor':0},
	'defense +1': {'cost':20, 'damage':0, 'armor':1},
	'defense +2': {'cost':40, 'damage':0, 'armor':2},
	'defense +3': {'cost':80, 'damage':0, 'armor':3},
	}
	

def fight(hp, damage, armour):
   bosshp = boss_hit_points
   while True:
       bosshp -= max(1, damage - boss_armor)
       if bosshp <=0:
           return True
       hp -= max(1, boss_damage - armour)
       if hp <= 0:
           return False
           
minimum = 9999999
maximum = 0
for weapon in weapons:
    for armour in armours:
        for ring1, ring2 in itertools.combinations(rings, 2):
           my_hp = 100
           cost = weapons[weapon]['cost'] + armours[armour]['cost'] + rings[ring1]['cost'] + rings[ring2]['cost']
           dam = weapons[weapon]['damage'] + armours[armour]['damage'] + rings[ring1]['damage'] + rings[ring2]['damage']
           arm = weapons[weapon]['armor'] + armours[armour]['armor'] + rings[ring1]['armor'] + rings[ring2]['armor']
           if fight(my_hp, dam, arm):
               minimum = min(minimum, cost)
           else:
               maximum = max(maximum, cost)

print minimum
print maximum