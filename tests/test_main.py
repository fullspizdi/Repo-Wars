# tests/test_main.py

import unittest
from starter_repo.main import basic_calculation, main

class TestMain(unittest.TestCase):
    def test_basic_calculation(self):
        """
        Test the basic_calculation function to ensure it correctly adds two numbers.
        """
        self.assertEqual(basic_calculation(5, 3), 8)
        self.assertEqual(basic_calculation(0, 0), 0)
        self.assertEqual(basic_calculation(-1, 1), 0)
        self.assertEqual(basic_calculation(100, 200), 300)

    def test_main_output(self):
        """
        Test the main function to ensure it prints the correct outputs.
        This test checks if the output contains specific expected strings.
        """
        with self.assertLogs() as captured:
            main()
            self.assertIn("Welcome to Repo Wars! Let the battle of code commence!", captured.output[0])
            self.assertIn("The result of our basic calculation is: 8", captured.output[1])

if __name__ == '__main__':
    unittest.main()
