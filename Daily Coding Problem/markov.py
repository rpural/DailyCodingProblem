#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

    [
      ('a', 'a', 0.9),
      ('a', 'b', 0.075),
      ('a', 'c', 0.025),
      ('b', 'a', 0.15),
      ('b', 'b', 0.8),
      ('b', 'c', 0.05),
      ('c', 'a', 0.25),
      ('c', 'b', 0.25),
      ('c', 'c', 0.5)
    ]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
'''

import json
import random
import collections

def transition(current, markov):
    '''
        Given a list of transitions and probabilities of making each specific
        transition, and the current location in the chain, select the next
        location and return it.
    '''

    # first, get a list of the possible next states and their probability
    next = list()
    for transit in markov:
        if transit[0] == current:
            next.append(transit)

    # next, get our state change probability index (random number from 0 - 1)
    newstate = random.random()

    # Find where in the state change list we should transit to
    accumulate = 0.0
    for _, nextstate, prob in next:
        accumulate += prob
        if newstate < accumulate:
            return nextstate
    # we shouldn't make it to here, but in this case, return the last state
    return next[-1][1]

# The starting state, number of steps and the Markov chain of transitions
# are stored in a file in JSON format
with open("markov.dat") as f:
    problem = json.load(f)

# Display the initial state and the number of state changes to run through
print("Starting from state {}, and performing {} steps...".format(problem["start"], problem["steps"]))
# print(problem)

# Collect the number of visits each state receives
accumulate = collections.defaultdict(int)

# Initialize to the starting state, and loop through the steps calling transition()
current = problem["start"]
for loop in range(problem["steps"]):
    current = transition(current, problem["markov"])
    accumulate[current] += 1

# print the results of the visits (number of visits per state
print("\nVisit counts:")
for s, c in accumulate.items():
    print("    '{}' = {}".format(s, c))
# print(accumulate)
