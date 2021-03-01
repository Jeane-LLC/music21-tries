from music21 import corpus
from unittest import TestCase
from trie import NoteTrie

class Test_Trie(TestCase):
    def test_insert(self):
        triad = corpus.parse('theoryExercises/TriadExercise')
        noteTrie = NoteTrie(triad.flat.notes)
        pass

    def test_search(self):

        pass
