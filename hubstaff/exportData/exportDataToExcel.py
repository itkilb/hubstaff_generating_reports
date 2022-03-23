from openpyxl import Workbook


class ExportDataToExcel:
    def __init__(self, data):
        self._data = data

    def export_data(self):
        self.generate_file()

    def generate_file(self):
        wb = Workbook()
        ws = wb.active

        for i in self._data:
            ws.append(i)

        wb.save('report.xlsx')
