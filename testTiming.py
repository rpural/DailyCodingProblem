#! /usr/bin/env python3

''' Demonstrate timing code via a context manager '''

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval =  self.end - self.start


import requests

with Timer() as t:
    conn =requests.get('https://www.google.com')
    print("Returned Status: {}".format(conn.status_code))

print("Request (pc) took {:.03f} sec.".format(t.interval))
