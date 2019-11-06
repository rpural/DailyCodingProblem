#! /usr/bin/env python3

''' A Cards class '''

import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards =[Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    deck = Deck()
    print("fifth card is {}, tenth card is {}".format(deck[4], deck[9]))
