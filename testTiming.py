#! /usr/bin/env python3

''' Demonstrate timing code via a context manager '''

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    # def __exit__(self, *args):
    def __exit__(self, exc_type, exc, exc_tb):
        self.end = time.perf_counter()
        self.interval =  self.end - self.start


from contextlib import contextmanager

@contextmanager
def Timer2(*args, **kwds):
    start_t = time.perf_counter()
    try:
        yield
    finally:
        end_t = time.perf_counter()
        interval = end_t - start_t
        print("Time = {:.03f}".format(interval))


import requests

with Timer() as t:
    conn =requests.get('https://www.google.com')
    print("Returned Status: {}".format(conn.status_code))

print("Request (pc) took {:.03f} sec.".format(t.interval))
print("-" * 5)
with Timer2():
    conn = requests.get('https://www.google.com')
    print("Returned Status: {}".format(conn.status_code))
