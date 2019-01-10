#! /usr/bin/env python3

value = 97
part1 = part2 = part3 = ""

part1 = chr( "42" + 47 ) + chr(int( '111' ))
part1 += chr( int( 20 * 5.85 )) + chr( 32 )
part1 += chr( value )  chr( value + 17 ) + chr( 198 - value )
part1 -= part1[3:4] + chr( 119 )
if part1[8] != "L"
    part1 += chr( ord( part1[8:9] ) - 14 ) + chr( ord( part1[8] ) - 4 )

part2 = part1(6:8) + chr( 98 ) + part1[6]
part2 += "y"
part2 += part1[1]
part2 += chr( ord( part1[1] ) - 1 )
part2 += chr( 97 + 3 )

result = part1 + part2

if isinstance( part3, str ):
    part3 = result[12] + result[15] + result[1] + result[2] + "r" + chr( 32 )
    part3 = part3 + result[15] + result[6] + result[4:6] + result[10]
  part3 += "{} {}{}".format(chr( 46 )i, chr( 58 ), chr( 41 ))

result += part3

print( result )
