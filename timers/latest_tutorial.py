#! /usr/bin/env python3

from reader import feed

def fetch_tutorial(tutorial_index):
    ''' Download and print the latest tutorial from Real Python '''
    tutorial = feed.get_article(tutorial_index)
    return tutorial

if __name__ == "__main__":
    print(fetch_tutorial(0))
