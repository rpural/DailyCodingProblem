#! /usr/bin/env python3

''' Demonstrate timing code via a context manager '''

import time

class Timer:
    def __enter__(self):
        self.start_pc = time.perf_counter()
        self.start_pt = time.process_time()
        return self

    def __exit__(self, *args):
        self.end_pc = time.perf_counter()
        self.end_pt = time.process_time()
        self.interval_pc =  self.end_pc - self.start_pc
        self.interval_pt =  self.end_pt - self.start_pt


import requests

with Timer() as t:
    conn =requests.get('https://www.google.com')
    print("Returned Status: {}".format(conn.status_code))

print("Request (pc) took {:.03f} sec.".format(t.interval_pc))
print("Request (pt) took {:.03f} sec.".format(t.interval_pt))

print("-" * 5)
print("addition loop:")
with Timer() as t2:
    j = 0
    for i in range(1000000):
        j += i

print("Request (pc) took {:.03f} sec.".format(t2.interval_pc))
print("Request (pt) took {:.03f} sec.".format(t2.interval_pt))

