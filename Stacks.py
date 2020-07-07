
class Stack:

    """ This is just meant to be a simple stack implementation that my
    game-piece container class can inherit from.
    """

    def __init__(self, elements=[]):
        self.elements = elements

    def isEmpty(self):
        return not self.elements # since an empty list is implicitly False

    def length(self):
        return len(self.elements)

    def push(self, element):
        self.elements = self.elements + [element]

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped = self.elements[(self.length() - 1)]
            self.elements = self.elements[:(self.length() - 1)]
            return popped

    def view(self):
        return self.elements


class GamePieceCollection(Stack):

    """ This class is for storing the state of the game pieces throughout the
    course of the game.
    """

    def __init__(self, elements):
        super().__init__(elements)
