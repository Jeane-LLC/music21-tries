"""
Trie.py - Data structures for storing unique sequences of music21 objects

PitchTrie - A way to store and retrieve unique pitch sequences
"""


class PitchTrie:

    pitches = []
    children = []

    def __init__(self, pitches):
        self.pitches = pitches
        self.insert(pitches[1:])

    def search(self, pitch):
        index = -1
        for child in self.children:
            index += 1
            if child.pitches[0] == pitch:
                return index
        return index

    def insert(self, pitches):
        if len(pitches) == 0:
            return
        index = self.search(pitches[0])
        if index == -1 or index == len(pitches):
            print("not found")
            self.children.append(PitchTrie(pitches))
        else:
            print("found")
            self.children[index].insert(pitches[1:])

    def draw(self):
        print(self.pitches)
        for child in self.children:
            child.draw()
