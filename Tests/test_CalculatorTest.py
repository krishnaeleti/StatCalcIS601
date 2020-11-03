import unittest
from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CSVReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # To test instantiation of calculator class
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Testing addition
    def test_addition(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()
