#! /usr/bin/env python3

''' Python Morsels problem

Read in a pipe-delimited file and produce a comma-delimited file
'''
import csv
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delimiter', default='|')
parser.add_argument('--in-quote', dest='quotechar', default='"')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter=args.delimiter, quotechar=args.quotechar)
    with open(args.new_filename, mode='wt', newline='') as new_file:
        csv.writer(new_file).writerows(reader)
