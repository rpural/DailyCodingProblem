#! /usr/bin/env python3

''' Implement a Timer context manager for timing Python
    code
'''

import time

class Timer:
    ''' Timer class definition

            To be used as the context manager in a with statement.

            This will collect the perf_counter() delta of the code
            within the with context, and leave the result as
            object.interval
    '''
    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self._end = time.perf_counter()
        self.interval =  self._end - self._start

if __name__ == "__main__":
    import requests

    with Timer() as t:
        conn =requests.get('https://www.google.com')

    print("Request took {:.03f} sec.".format(t.interval))
