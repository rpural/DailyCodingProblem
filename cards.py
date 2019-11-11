#! /usr/bin/env python3

''' A Cards class '''

import collections.abc

Card = collections.namedtuple("Card", ['rank', 'suit'])

class Deck(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards =[Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)


if __name__ == "__main__":
    from random import shuffle

    deck = Deck()
    print("size of deck is {}".format(len(deck)))
    print("fifth card is {}, tenth card is {}".format(deck[4], deck[9]))

    shuffle(deck)
    print("after shuffle:")
    print("size of deck is {}".format(len(deck)))
    print("fifth card is {}, tenth card is {}".format(deck[4], deck[9]))

    deck.insert(52, Card(0, 'J'))
    print("after adding Joker:")
    print("size of deck is {}".format(len(deck)))
    print("last cards are: {}, {}".format(deck[-2], deck[-1]))
