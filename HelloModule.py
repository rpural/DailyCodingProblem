"""
The helloModule is a demonstration of the structure of an imported module
It contains a variable, helloString, and a function, sayHello(string="")

Print various greetings.
"""

helloString = "Hello, World"

def sayHello(string=""):
    """
    Print a greeting, defaulting to 'Hello, World'

    sayHello(string="Hi, Jim!")
    """

    if string == "":
        print(helloString)
    else:
        print(string)
