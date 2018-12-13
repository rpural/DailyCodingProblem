a = 65534       # ff fe
b = 65535       # ff ff
c = 65536       # 00 01 00 00
d = 2998302     # 02 2d c0 1e

with open("binary.data", "bw") as bin_file:
    bin_file.write(a.to_bytes(2,"big"))
    bin_file.write(b.to_bytes(2,"big"))
    bin_file.write(c.to_bytes(4,"big"))
    bin_file.write(d.to_bytes(4,"big"))
    bin_file.write(d.to_bytes(4,"little"))

with open("binary.data", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    f = int.from_bytes(bin_file.read(2), "big")
    g = int.from_bytes(bin_file.read(4), "big")
    h = int.from_bytes(bin_file.read(4), "big")
    x = int.from_bytes(bin_file.read(4), "big")

print("e = {}, f = {}, g = {}, h = {}, x = {}".format(e, f, g, h, x))

#    for i in range(17):
#        bin_file.write(bytes([i]))

#with open("binary.data", "br") as bin_file:
#    for b in bin_file:
#        print(b)
