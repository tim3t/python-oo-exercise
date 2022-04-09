"""Word Finder: finds random words from a dictionary.
    >>>wf = WordFinder("words.txt")


"""
import random


class WordFinder:
    def __init__(self, path):
        file = open(path)
        self.words = []
        for w in file:
            self.words.append(w)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        return (w.strip() for w in file)
    
    def random(self):
        return (random.choice(self.words))[:-1:]

class SpecialWordFinder(WordFinder):
    def parse(self, file):
        return [w.strip() for w in file
            if w.strip() and not w.startswith("#")]w

