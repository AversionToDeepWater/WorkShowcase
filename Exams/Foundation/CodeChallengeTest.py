from unittest import TestCase, main
from CodeChallenge import no_of_handshakes

class TestCodeChallengeFunction(TestCase):
    def test_CorrectValue(self):
        expected = no_of_handshakes(3)
        result = 3
        self.assertEqual(expected, result)

    def test_ReallyLargeValue(self):
        expected = no_of_handshakes(100)
        result = 4950
        self.assertEqual(expected, result)

    def test_ZeroAsInput(self):
        expected = no_of_handshakes(0)
        result = 0
        self.assertEqual(expected, result)

    def test_string(self):
        expected = no_of_handshakes("str")
        result = None
        self.assertEqual(expected, result)

    def test_one(self):
        expected = no_of_handshakes(1)
        result = 0
        self.assertEqual(result, expected)

    def test_LargeNoOfPeople(self):
        expected = no_of_handshakes(20)
        result = 190
        self.assertEqual(expected, result)




if __name__ == "__main__":
    main()