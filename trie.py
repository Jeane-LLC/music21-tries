from copy import deepcopy


class NoteTrie:

    children = []

    def __init__(self, flat, index, note=None):
        self.index = index
        if note:
            self.note = note
            self.flat = flat
        else:
            rootFlat = deepcopy(flat)
            self.note = rootFlat.pop(0)
            self.flat = rootFlat
        self.insert()

    def insert(self):
        childIndex = self.index
        if len(self.flat) == 0:
            return
        for note in self.flat:
            childIndex += 1
            rootFlat = deepcopy(self.flat)
            note = rootFlat.pop(0)
            self.children.append(NoteTrie(rootFlat, childIndex, note))

    def search(self):
        # BFS all of the nodes
        pass
