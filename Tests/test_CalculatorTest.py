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

  # Testing subtraction
    def test_subtraction(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

 # Testing multiplication
    def test_multiplication(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

 # Testing division
    def test_division(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(float(row['Result']), self.calculator.divide(row['Value 1'], row['Value 2']))
            self.assertAlmostEqual(float(row['Result']), round(self.calculator.result, 9))
        test_data.clear()

# Testing squared
    def test_squared(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

 # Testing squared root
    def test_squared_root(self):
        test_data = CSVReader('/Tests/Data_Calculator/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.squared_root(row['Value 1']), round(float(row['Result']), 9))
            self.assertAlmostEqual(round(float(row['Result']), 9), round(self.calculator.result, 9))
        test_data.clear()

    def test_results(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()