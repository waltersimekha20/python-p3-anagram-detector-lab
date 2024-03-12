# Save this code in a file named 'anagram.py'

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower()]
