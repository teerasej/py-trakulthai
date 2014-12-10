import gspread
import Product

__author__ = 'Teerasej'

class Preparer:

    def __init__(self):
        pass

    def get_products(self, username, password, sheet_name ):

        gc = gspread.login(username, password)
        print 'Signed in... '
        current_worksheet = gc.open(sheet_name).sheet1
        print 'Accessed sheet: "' + sheet_name + '"'

        rows = current_worksheet.get_all_values()
        print 'Total products: ' + len(rows) - 1

        products = []
        print '[Converting | Start] ...'

        for row in rows:
            product = self.convert(row)
            products.append(product)


        print '[Converting | Finish] ...'
        print '[Summary] Total converted product: ' + len(products) + ' (rows: ' + len(rows) + ')'

        return products

    def convert(self, row):

        return