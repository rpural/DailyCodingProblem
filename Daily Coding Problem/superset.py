#! /usr/bin/env python3

list = [ 1, 2, 3 ]

def superset( solutionset, subset ):

    print("solutionset = {}, subset = {}".format( solutionset, subset ))
    if len(subset) < 2:
        result = solutionset
        result.append(subset)
        print( "short subset, result = {}".format( result ))
        return result

    sub = subset[0:1]
    subs = subset[1:]
    result = solutionset
    result.append( sub )
    result.append(superset( result, subs ))
    print( "long subset, result = {}".format( result ))
    return result

super = superset( [], list )

print( super )
