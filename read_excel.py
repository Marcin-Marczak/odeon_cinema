import xlrd
from search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data_for_test_02():
        wb = xlrd.open_workbook("../data_test.xls")
        sheet = wb.sheet_by_name("Data")
        data = []
        for i in range(1, sheet.nrows - 4):
            search_data = SearchData(sheet.cell(i, 1).value, sheet.cell(i, 2).value)
            data.append(search_data)
        return data

    @staticmethod
    def get_data_for_test_03():
        wb = xlrd.open_workbook("../data_test.xls")
        sheet = wb.sheet_by_name("Data")
        data = []
        for i in range(2, sheet.nrows - 2):
            search_data = SearchData(sheet.cell(i, 1).value, sheet.cell(i, 2).value)
            data.append(search_data)
        return data

    @staticmethod
    def get_data_for_test_04():
        wb = xlrd.open_workbook("../data_test.xls")
        sheet = wb.sheet_by_name("Data")
        data = []
        for i in range(4, sheet.nrows - 1):
            search_data = SearchData(sheet.cell(i, 1).value, sheet.cell(i, 2).value)
            data.append(search_data)
        return data

    @staticmethod
    def get_data_for_test_05():
        wb = xlrd.open_workbook("../data_test.xls")
        sheet = wb.sheet_by_name("Data")
        data = []
        for i in range(5, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 1).value, sheet.cell(i, 2).value)
            data.append(search_data)
        return data