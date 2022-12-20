import unittest
import change_text


class TestChangeText(unittest.TestCase):
    def test_change_uppercase(self):
        word = "word"
        result = change_text.all_capitals(word)
        self.assertEqual(result, "WORD")

    def test_get_title(self):
        word = "pradeep"
        result = change_text.get_title(word)
        self.assertEqual(result, "Pradeep")


if __name__ == '__main__':
    unittest.main()
