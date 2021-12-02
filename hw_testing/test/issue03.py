from one_hot_encoder import fit_transform
import unittest


class TestOheHotEncoding(unittest.TestCase):
    def test_with_assert_equal(self):
        actual = fit_transform('dark', 'light')

        expected = [('dark', [0, 1]), ('light', [1, 0])]
        self.assertEqual(actual, expected)

    def test_with_asset_not_in(self):
        actual = fit_transform('dark', 'light')

        for item in actual:
            self.assertNotIn(2, item[1])

    def test_with_assert_true(self):
        actual = fit_transform('dark', 'light')

        for item in actual:
            for i in item[1]:
                self.assertTrue(i < 2)

    def test_with_assert_raises(self):
        with self.assertRaises(TypeError):
            actual = fit_transform()
