jabber = open("/Users/rpn01/Downloads/sample.txt","r")

letters = set()

for line in jabber:
    print(line, end="")
    lets = set(line.upper()).intersection(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    letters = letters.union(lets)

jabber.close()

print(sorted(letters))
print(len(letters))
