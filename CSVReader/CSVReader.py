import csv
from FilePath.Absolute_Path import absolute_path


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolute_path(filepath)) as test_data:
                csv_data = csv.DictReader(test_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
        except OSError:
            print('cannot open', filepath)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects