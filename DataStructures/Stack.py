"""An implementation of the Stack data structure.
A stack follows FILO (first in, last out)
"""
class Stack:
    def __init__(self):
        self.items = []

    """Tests to see whether the stack is empty. Returns a boolean value."""
    def isEmpty(self):
        return self.items == []

    """Adds a new item to the top of the stack. Takes an item and returns nothing."""
    def push(self, item):
        self.items.append(item)

    """Removes the top item from the stack. It needs no parameters and returns the item. The stack is modified."""
    def pop(self):
        return self.items.pop()

    """Returns the top item from the stack but does not remove it. Stack is not modified."""
    def peek(self):
        return self.items[len(self.items)-1]

    """Returns the size of the current stack."""
    def size(self):
        return len(self.items)

