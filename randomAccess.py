#! /usr/bin/env python3

''' Create a "random access" file using read(), write(), and seek()
'''

ra = open("random.bin", "w")

for i in range(100):
    record = "     " + str(i)
    record = record[-4:]
    ra.write(record)

rasize = ra.tell()  # Remember end of file
ra.close()

ra = open("random.bin", "r+")

for record in range(5, 31, 5):
    ra.seek(record * 4)  # Find the "n'th" four character record
    data = ra.read(4)
    print(f"data: {data}")
    newdata = int(data) + 22
    newdata = "    " + str(newdata)
    newdata = newdata[-4:]
    ra.seek(record * 4)  # Move back to the beginning of the record
    ra.write(newdata)

ra.seek(0)  # Go back to the beginning of the file
while ra.tell() < rasize:
    try:
        data = ra.read(4)
        print(f"data: {data}")
    except:
        print("Reached end of file")
print("End")

ra.close()
