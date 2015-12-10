
data = []

f = open('day5_data.txt', 'r')
for line in f:
    data.append(line)

import re
double_regexp = re.compile(r"(.)\1")
exception_regexp = re.compile(r"(ab)|(cd)|(pq)|(xy)")

nice_list = 0

for word in data:
    #contains 3 vowels
    if len([letter for letter in word if letter in ['a','e','i','o','u']]) > 2\
        and  re.search(double_regexp, word)\
        and  not re.search(exception_regexp, word):
        nice_list += 1

print nice_list


#data = ["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"]


nice_list = 0

for word in data:
    c1 = False
    c2 = False
    for idx, letter in enumerate(word):
        count = word.count(letter)

        if count > 1:
            #first criteria
            if (idx+2) < len(word):
                next_letter = word[idx+1:idx+2]
                pair_idx = word.find(letter + next_letter)
                if pair_idx >= 0 and pair_idx < len(word)-1:
                    pair_two_idx = word[pair_idx+2:].find(letter+ next_letter)
                    if pair_two_idx >=0:
                        c1 = True

            #second criteria
            if (idx+2) < len(word)\
                 and  letter == word[idx+2]:
                c2 = True

        if c1 and c2:
            nice_list += 1
            break

print nice_list
