#! /usr/bin/env python3

''' Read a LinkedIn Learning history page and extract the names and dates
    of completed courses.
'''

from bs4 import BeautifulSoup
import re

states = ("COURSE", "Course", "Completed")

with open("../Downloads/rpn01 Completed Courses.html", "r") as source:
    html_doc = source.read()

# print(html_doc)
soup = BeautifulSoup(html_doc, "html.parser")
# print(dir(soup))
strings = list(soup.stripped_strings)
# print(strings)
state = 0
for line, string in enumerate(strings):
    if state == 0:
        if string == states[0]:
            state = 1
    if state == 1:
        title = strings[line+1]
        state = 2
    if state == 2:
        if re.match("Completed", string):
            print(f"{string}\t- {title}")
            state == 0
        elif string == states[0]:
            state = 1

