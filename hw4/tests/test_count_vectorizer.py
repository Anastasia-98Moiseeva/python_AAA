import unittest
from main import CountVectorizer


class TestCountVectorizer(unittest.TestCase):

    def assertPermutationEqual(self, first, second):
        return self.assertEqual(sorted(first), sorted(second))

    def test_empty_corpus(self):
        vectorizer = CountVectorizer()
        corpus = []
        self.assertEqual(vectorizer.fit_transform(corpus), [])
        self.assertEqual(vectorizer.get_feature_names(), [])

    def test_empty_texts(self):
        vectorizer = CountVectorizer()
        corpus = ['', '', '', '']
        self.assertEqual(vectorizer.fit_transform(corpus), [[], [], [], []])
        self.assertEqual(vectorizer.get_feature_names(), [])

    def test_text_with_unique_terms(self):
        vectorizer = CountVectorizer()
        corpus = ['Hello world', 'Wonderful life']
        self.assertEqual(vectorizer.fit_transform(corpus), [[1, 1, 0, 0], [0, 0, 1, 1]])
        self.assertEqual(vectorizer.get_feature_names(), ['hello', 'world', 'wonderful', 'life'])


if __name__ == '__main__':
    unittest.main()