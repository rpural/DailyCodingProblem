#! /usr/bin/env python3

'''
    Use simpy to simulate a theater lobby

    Imagine you’ve been hired to help the manager for a small, local movie 
    theater. The theater has been receiving poor reviews due to their long wait 
    times. The manager, who is just as concerned about cost as he is about 
    customer satisfaction, can only afford to keep so many employees on staff.

    The manager is particularly worried about what chaos can unfold once those 
    blockbusters start coming out: lines wrapping around the theater, employees 
    stretched to their limit, angry moviegoers missing the opening scenes… This 
    is definitely a situation to avoid!

    After checking the reviews, the manager was able to determine that a given 
    moviegoer to their theater is willing to spend at most 10 minutes from the 
    time they arrive until the time they put their butt in a seat. In other 
    words, the average wait time for a night at the theater needs to be 10 
    minutes or less. The manager has asked for your help to figure out a 
    solution to getting customer wait times under this 10 minute requirement.
'''

import random
import simpy
import statistics

wait_times = []

class Theater(object):
    def __init__(self, env, num_cashiers, num_ushers, num_servers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.usher = simpy.Resource(env, num_ushers)
        self.server = simpy.Resource(env, num_servers)

    def purchase_ticket(self, moviegoer):
        ''' A cashier takes an average of 1 to 3 minutes to sell a ticket '''
        yield self.env.timeout(random.randint(1, 3))

    def check_ticket(self, moviegoer):
        ''' The ushers can take check one ticket every three seconds '''
        yield self.env.timeout(3/60)

    def purchase_food(self, moviegoer):
        ''' A server can help a moviegoer in 1 to 5 minutes '''
        yield self.env.timeout(random.randint(1, 5))

def go_to_movies(env, moviegoer, theater):
    global wait_times

    # moviegoer arrives at the theater
    arrival_time = env.now

    # purchase a ticket
    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(moviegoer))

    # have the ticket checked
    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    # randomly, stop by the concession stand to get something to eat
    if random.choice([True, False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.purchase_food(moviegoer))

    # moviegoer heads to their seat
    wait_times.append(env.now - arrival_time)

def run_theater(env, num_cashiers, num_ushers, num_servers):
    theater = Theater(env, num_cashiers, num_ushers, num_servers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    while True:
        yield env.timeout(0.20) # generate a new customer every 12 seconds

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))

def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)

def get_user_input():
    num_cashiers = int(input("# of cashiers: "))
    num_ushers = int(input("# of ushers: "))
    num_servers = int(input("# of servers: "))
    params = [num_cashiers, num_ushers, num_servers]
    return params

def main():
    global wait_times 

    # setup
    random.seed(42)
    num_cashiers, num_ushers, num_servers = get_user_input()

    # run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_ushers, num_servers))
    env.run(until=90)

    # view the results
    mins, secs = get_average_wait_time(wait_times)
    print("Running simulation...\n",
         f"The average wait time is {mins} minutes and {secs} seconds.",
            )

if __name__ == "__main__":
    main()
