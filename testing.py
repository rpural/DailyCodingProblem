#!/usr/bin/env python
list1=['A', 'T', 'G', 'C', 'A' ,'C', 'G' , 'T' , 'C', 'G']
list2=[ 'GGG' , 'TTTN' , ' - ' , 'NNN' , 'AAA' , 'CCC' , 'GCCC' , 'TTT'  ,'CCCATN' ]
list2=['AAAAGGGCCCCTTTTT', 'TTTN', ' - ', 'NNN', 'AAA', 'CCC', 'GCCC', 'TTT', 'CCCATN']

notifications = []
indexes = []

print list1
print list2

totals = { "A" : 0, "T" : 0, "G" : 0, "C" : 0 }

for i in range(min(len(list1), len(list2))):
    item1 = list1[i]
    item2 = list2[i]
    
    # Skip ' - '
    if item2 == ' - ':
        continue
    
    # Remove N since it's a wildcard
    item2 = item2.replace('N', '')
    
    # Remove item1
    item2 = item2.replace(item1, '')
    
    chars = set(item2)
    
    # All matched
    if len(chars) == 0:
        continue

    test2 = item2

    for selector in ["A", "T", "G", "C"]:
        total = len(test2)
        test2 = test2.replace(selector,'')

        totals[selector] += total - len(test2)
    
    notifications.append('{}/{}'.format(item1, '/'.join(set(item2))))
    indexes.append(i)
    
print(notifications)
print(indexes)
for selector in totals.keys():
    print(selector + ":  ", totals[selector])
