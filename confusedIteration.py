a = {0:0}
b = []
for i in a:
    del a[i]
    b.append(i)
    a[i+1] = i
    print(b)
