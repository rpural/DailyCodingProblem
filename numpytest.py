#! /usr/bin/env python3

import numpy as np
import time

start = time.time()
search_pool = list(range(1000000000))  # a list of 1 billion numbers
print("list: search_pool creation time: {} secs".format((time.time() - start)))

start = time.time()
a = min(search_pool)
print("list: min(search_pool) time: {} secs".format((time.time() - start)))

start = time.time()
a = max(search_pool)
print("list: max(search_pool) time: {} secs".format((time.time() - start)))

start = time.time()
search_pool = range(1000000000)  # an iterable of 1 billion numbers
print("iterable: search_pool creation time: {} secs".format((time.time() - start)))

start = time.time()
a = min(search_pool)
print("iterable: min(search_pool) time: {} secs".format((time.time() - start)))

start = time.time()
a = max(search_pool)
print("iterable: max(search_pool) time: {} secs".format((time.time() - start)))

start = time.time()
search_pool = np.arange(1000000000)  # an ndarray of 1 billion numbers
print("ndarray: search_pool creation time: {} secs".format((time.time() - start)))

start = time.time()
a = np.min(search_pool)
print("ndarray: np.min(search_pool) time: {} secs".format((time.time() - start)))

start = time.time()
a = np.max(search_pool)
print("ndarray: np.max(search_pool) time: {} secs".format((time.time() - start)))

