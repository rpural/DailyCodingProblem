#! /usr/bin/env python3

import time
import functools
from contextlib import ContextDecorator

class TimerError(Exception):
    ''' A custom exception used to report errors in use of the Timer class '''


class Timer(ContextDecorator):
    timers = dict()

    def __init__(self, name=None, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger
        self._name = name

        if self._name:
            self.timers.setdefault(self._name, 0)

    def start(self):
        ''' Start a new timer '''
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = time.perf_counter()

    def stop(self):
        ''' Stop the timer, and report the elapsed time '''
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it.")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self._name:
            self.timers[self._name] += elapsed_time

        return elapsed_time

    def __enter__(self):
        ''' Start a new timer as a context manager '''
        self.start()
        return self

    def __exit__(self, *exc_info):
        ''' Stop the context manager timer '''
        self.stop()
