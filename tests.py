from woordy import Woordy
import unittest, json


class TestModule(unittest.TestCase):
    "Checks for the translate module."

    def test_translate_valid(self):
        self.maxDiff = None
        method_result = Woordy.translate("book", "en", "pt")
        result = '{"livro": "collection of sheets of paper bound together containing printed or written material"}'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)        
        self.assertCountEqual(expected_result, expected_result)


    def test_translate_not_valid(self):
            method_result = Woordy.translate("auhfa", "en", "pt")
            expected_result = 'Word not found. Try checking for some typo issues.'
            self.assertEqual(method_result, expected_result)


if __name__ == "__main__":
    unittest.main()