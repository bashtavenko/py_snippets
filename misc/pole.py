"""Given a set of words, find with the least tries the required word."""


class Client:
    """Computer guesses word based on the dictionary."""

    def __init__(self, words, server):
        self.words = words
        self.server = server

    def guess(self):
        pass


class Server:
    """Human who comes up with a guess word and provide hints on each guess."""

    def __init__(self, word):
        self.word = word

    def guess(self, guess_word):
        """Returns a string with all letters in correct position or '_'."""
        result = []
        for c in self.word:
            if c in guess_word:
                result.append(c)
            else:
                result.append("-")
        return "".join(result)
