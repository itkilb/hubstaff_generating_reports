import csv


class ExportDataToCsv:
    def __init__(self, data):
        self._data = data

    def export_data(self):
        self.generate_file()

    def generate_file(self):
        file = open('report.csv', 'w')
        with file:
            writer = csv.writer(file)
            writer.writerows(self._data)
