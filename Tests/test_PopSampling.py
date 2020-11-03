import unittest
from PopulationSampling.PopSampling import PopSampling
from CSVReader.CSVReader import CSVReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.PopSampling = PopSampling()

    # To test instantiation of PopSampling class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    # Testing Cochran
    def test_cochran(self):
        test_data = CSVReader('/Tests/Data_PopSampling/Cochran_Data.csv').data
        for row in test_data:
            #pprint(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']))
            self.assertEqual(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopSampling.result, int(row['Sample']))
        test_data.clear()