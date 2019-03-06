class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        ''' Accepts an item as a parameter and appends it to the end of the list.
            Returns nothing.

            The runtime for this method is O(1), or constant time, because
            appending to the end of a list happens in constant time.
        '''

        self._items.append(item)

    def pop(self):
        ''' Removes and returns the last item from the list (top of stack)

            The runtime is O(1).
        '''

        if self._items:
            return self._items.pop()
        else:
            return None

    def peek(self):
        ''' Returns the last item from the list (top of stack), but does not
            remove the item.

            The runtime is O(1)
        '''

        if self._items:
            return self._items[-1:][0]
        else:
            return None

    def size(self):
        ''' This method returns the length of the list representing the Stack.
        '''

        return len(self._items)

    def is_empty(self):
        ''' This method returns True if there are no items on the stack.
        '''

        return self._items == []
