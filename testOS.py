#! /usr/bin/env python3

import os
import sys

if len( sys.argv ) > 1:
    working_path = sys.argv[1]
else:
    print( "testOS.py" )
    print( "\n    Given a working path as an argument, test creating" +
          "\n    a directory and a file, reading the file, and" +
          "\n    renaming the file, listing the directory, and removing" +
          "\n    the file and directory.\n" +
          "\n    The original purpose is to test automounts of NFS and" +
          "\n    CIFS directories, to see if the CIFS automounts respond" +
          "\n    to these python requests." )
    exit(0)

os.mkdir( working_path + "/testpath", 0o775 )
testfile = open( working_path + "/testpath/" + "testfile", mode='w' )
testfile.write( "This is a test file. Please ignore or remove if found.\n" )
testfile.close()
testfile = open( working_path + "/testpath/" + "testfile", mode='r' )
testdata = testfile.read()
print( testdata )
testfile.close()

os.rename( working_path + "/testpath/" + "testfile",
        working_path + "/testpath/" + "newfile" )
print( os.listdir( working_path + "/testpath/" ) )

os.unlink( working_path + "/testpath/" + "newfile" )
os.rmdir( working_path + "/testpath" )
