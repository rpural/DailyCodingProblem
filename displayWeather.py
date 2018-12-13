#! /usr/bin/env python3

''' Weather

Read DarkSky weather data in json format and display information about the weather.
'''

import sys
import json

def displayDictKeys( d, indent=0 ):
    for i in d.keys():
        print( "{}data at key {} is type: {}".format( " " * indent, i, type( d[ i ] )))
        if type( d[ i ] ) == type( {} ):
            displayDictKeys( d[ i ], indent=indent+4 )
        elif type( d[ i ] ) == type( [] ):
            print( "{}list has {} elements".format(" " * (indent + 4), len( d[ i ] )))
            displayListElements( d[ i ], indent=indent+4 )

def displayListElements( l, indent=0 ):
    print( "{}[".format( " " * indent ))
    if len( l ) > 3:
        for i in range(2):
            print("{}  element[{}] is type: {}".format( " " * (indent+2), i, type( l[ i ] )))
            if type( l[ i ] ) == type( {} ):
                displayDictKeys( l[ i ], indent=indent+4 )
            elif type( l[ i ] ) == type( [] ):
                print( "{}list has {} elements".format(" " * (indent + 4), len( l[ i ] )))
            displayListElements( l[ i ], indent=indent+4 )
        print("{}  ...".format( " " * (indent+2)))
        for i in range(len( l ) - 2, len(l)):
            print("{}  element[{}] is type: {}".format( " " * (indent+2), i, type( l[ i ] )))
            if type( l[ i ] ) == type( {} ):
                displayDictKeys( l[ i ], indent=indent+4 )
            elif type( l[ i ] ) == type( [] ):
                print( "{}list has {} elements".format(" " * (indent + 4), len( l[ i ] )))
                displayListElements( l[ i ], indent=indent+4 )
    else:
        for i in range( len( l )):
            print("{}  element[{}] is type: {}".format( " " * (indent+2), i, type( l[ i ] )))
    print( "{}]".format( " " * indent ))


if len( sys.argv ) > 1:
    weatherFile = sys.argv[1]
else:
    weatherFile = ""

if weatherFile != "":
    try:
        with open( weatherFile, "r" ) as wf:
            weather = json.load( wf )
    except IOError:
        print( "Error reading {}".format( weatherFile ))

print( "file {} is type: {}".format( weatherFile, type( weather )))

displayDictKeys( weather )


