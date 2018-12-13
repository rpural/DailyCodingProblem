#! /usr/bin/env python3

''' Daily Coding Problem

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
    You should be as efficient with time and space as possible.This problem was asked by Twitter.
'''

class orderLog:
    def __init__(self):
        self.maxLog = int(input("Maximum number of log entries to keep: "))
        self.orderIds = list()

    def record(self, order):
        self.orderIds.append(order)
        if len(self.orderIds) > self.maxLog:
            self.orderIds = self.orderIds[- self.maxLog:]

    def get_last(self, position):
        return (self.orderIds[-position:])[0]

    def __str__(self):
        return "{}".format(self.orderIds)

order = 9999

orders = orderLog()

while order != 0:
    order = int(input("Order number: "))

    if order == 555:
        oldOrder = orders.get_last(5)
        print("order #5 was order number {}".format(oldOrder))
    elif order == 666:
        print("OrderLog: {}".format(orders))
    else:
        orders.record(order)

