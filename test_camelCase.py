import unittest
import camelCase


class TestCase(unittest.TestCase):
    def test_only_spaces(self):
        input_output = {
            "        ": "",
            "  ": "",
            "": ""
        }
        msg = "Incorrect output"
        for inputs, output in input_output.items():
            self.assertEqual(camelCase.camelCase(inputs), output, msg)

    def test_one_word(self):
        inputs = ["xyz", "Xyz", "XYz", "XYZ", "xYz"]
        output = "xyz"
        msg = "Incorrect output"
        for word in inputs:
            self.assertEqual(camelCase.camelCase(word), output, msg)

    def test_escape_sequences(self):
        inputs_output = {
            "\t Hello How are you ?": "helloHowAreYou",
            "  \n hello how are \t \t \t You ?": "helloHowAreYou",
            "hello how are you \n ?": "helloHowAreYou"
        }
        msg = "Incorrect output"
        for inputs, output in inputs_output.items():
            self.assertEqual(camelCase.camelCase(inputs), output, msg)

    def test_upper_lower(self):
        inputs_output = {
            "HELLO PYTHON": "helloPython",
            "hello python": "helloPython",
            "Hello JAVA": "helloJava",
            "JAVA and PYTHON....": "javaAndPython"
        }
        msg = "Incorrect output"
        for inputs, output in inputs_output.items():
            self.assertEqual(camelCase.camelCase(inputs), output, msg)

    def test_sentences(self):
        inputs_output = {
            "A quick brown fox jumps over a lazy dog.": "aQuickBrownFoxJumpsOverALazyDog",
            " is This is python?": "isThisIsPython"
        }
        msg = "Incorrect output"
        for inputs, output in inputs_output.items():
            self.assertEqual(camelCase.camelCase(inputs), output, msg)


if __name__ == '__main__':
    unittest.main()
