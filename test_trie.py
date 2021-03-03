from unittest import TestCase
from trie import PitchTrie
from random import choice
from copy import deepcopy
allPitches = ["A", "B", "C", "D", "E", "F", "G"]
allAccidentals = ["#", "-", ""]
allOctaves = ["1", "2", "3", "4", "5", "6", "7"]


def randomPitches(number):
    pitches = []
    for i in range(number):
        randomPitch = choice(allPitches) + choice(allAccidentals) + choice(
            allOctaves)
        pitches.append(randomPitch)
    return pitches


class Test_PitchTrie(TestCase):
    def test_init(self):
        pitches = randomPitches(5)
        single = deepcopy(pitches)
        pitches.extend(pitches)
        print("Pitch Sequence: " + str(pitches))
        print("single: ", single)
        pitchTrie = PitchTrie()
        pitchTrie.insert(pitches)
        print(pitchTrie.query(single))
