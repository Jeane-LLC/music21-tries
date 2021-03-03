"""
Trie.py - Data structures for storing unique sequences of music21 objects

PitchTrie - A way to store and retrieve unique pitch sequences
"""


class PitchTrieNode:
    def __init__(self, pitch):
        self.pitch = pitch
        self.is_end = False
        self.count = 0
        self.children = {}


class PitchTrie(object):
    def __init__(self):
        self.root = PitchTrieNode("")

    def insert(self, pitches):
        node = self.root
        for pitch in pitches:
            if pitch in node.children:
                node = node.children[pitch]
            else:
                new_node = PitchTrieNode(pitch)
                node.children[pitch] = new_node
                node = new_node
        node.is_end = True
        node.count += 1

    def search(self, node, prefix):
        if node.is_end:
            prefix.append(node.pitch)
            self.output.append((prefix, node.count))
        for child in node.children.values():
            prefix.append(node.pitch)
            self.search(child, prefix)

    def query(self, prefix):
        self.output = []
        node = self.root
        for pitch in prefix:
            if pitch in node.children:
                node = node.children[pitch]
            else:
                return []
        self.search(node, prefix[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)
