#!/usr/bin/env python3

print("\\033[XXm Set color")

for i in range(30,37+1):
    print("\033[%dm%d  " % (i, i), end="")
print()
for i in range(60, 67+1):
    print("\033[%dm%d  " % (i,i), end="")
print()

print("\033[39m")
print("\\033[38;5;XXXm Set color from 256 color pallet")
for i in range(16):
    for j in range(16):
        code = str(i * 16 + j)
        print("\033[38;5;" + code +"m " + code.ljust(4), end="")
    print("\033[39m")

print()
print("\\033[38;2;r;g;bm Set color via RGB")
print("\033[38;2;255;0;0m\\033[38;2;255;0;0m     \033[38;2;0;255;0m\\033[38;2;0;255;0m    \033[38;2;0;0;255m\\033[38;2;0;0;255m")
print("\033[38;2;234;236;35m\\033[38;2;234;236;35m  \033[38;2;255;0;255m\\033[38;2;255;0;255m  \033[38;2;0;255;255m\\033[38;2;0;255;255m")

print("\033[39m")

print("\\033[0m Reset")
print("\\033[39m Reset color")
print("\\033[2K Clear Line")
print("\\033[<L>;<C>H OR \\033[<L>;<C>f puts the cursor at line L and column C.")
print("\\033[<N>A Move the cursor up N lines")
print("\\033[<N>B Move the cursor down N lines")
print("\\033[<N>C Move the cursor forward N columns")
print("\\033[<N>D Move the cursor backward N columns")
print("\\033[2J Clear the screen, move to (0,0)")
print("\\033[K Erase to end of line")
print("\\033[s Save cursor position")
print("\\033[u Restore cursor position")
print(" ")
print("\033[4m\\033[4m Underline on\033[0m")
print("\\033[24m Underline off")
print("\033[9m\\033[9m Crossed out\033[29m")
print("\\033[29m Crossed out off")
print("\033[1m\\033[1m Bold on\033[0m")
print("\\033[21m Bold off")
