import gspread
import Product

__author__ = 'Teerasej'

class ProductManager:

    def __init__(self, username, password, sheet_name):
        self.username = username
        self.password = password
        self.sheet_name = sheet_name

    def get_products(self):

        gc = gspread.login(self.username, self.password)
        print 'Signed in... '
        current_worksheet = gc.open(self.sheet_name).sheet1
        print 'Accessed sheet: "' + self.sheet_name + '"'

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



    def update_product_info(self, processed_product):
        pass