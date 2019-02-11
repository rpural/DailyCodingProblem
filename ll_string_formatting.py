#! /usr/bin/env python3

from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # Create a template with place holders
    temp1 = Template("You're watching ${title} by ${author}")
    str2 = temp1.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    data = { "author" : "Joe Marini",
             "title" : "Advanced Python"}
    str3 = temp1.substitute(data)
    print(str3)

main()