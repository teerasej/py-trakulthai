import gspread
import fnmatch, re, os
from Product import Product

__author__ = 'Teerasej'


def found(current_product, current_file):

    id_code = current_product.id.replace(' ', '')
    re_dash = re.compile(fnmatch.translate(id_code + '-*'))
    re_dash_lower = re.compile(fnmatch.translate(id_code.lower() + '-*'))
    re_underscore = re.compile(fnmatch.translate(id_code + '_*'))
    re_underscore_lower = re.compile(fnmatch.translate(id_code.lower() + '_*'))
    re_no_trail = re.compile(fnmatch.translate(id_code + '.*'))
    re_no_trail_lower = re.compile(fnmatch.translate(id_code.lower() + '.*'))
    re_space = re.compile(fnmatch.translate(id_code + ' *'))
    re_space_lower = re.compile(fnmatch.translate(id_code.lower() + ' *'))

    # re_dash = re.compile(fnmatch.translate('*' + product_code + '-*'))
    # re_dash_lower = re.compile(fnmatch.translate('*' + product_code.lower() + '-*'))
    # re_underscore = re.compile(fnmatch.translate('*' + product_code + '_*'))
    # re_underscore_lower = re.compile(fnmatch.translate('*' + product_code.lower() + '_*'))
    # re_no_trail = re.compile(fnmatch.translate('*' + product_code + '.*'))
    # re_no_trail_lower = re.compile(fnmatch.translate('*' + product_code.lower() + '.*'))
    # re_space = re.compile(fnmatch.translate('*' + product_code + ' *'))
    # re_space_lower = re.compile(fnmatch.translate('*' + product_code.lower() + ' *'))

    # if re_dash.match(current_file) or re_dash_lower.match(current_file):
    #     return True
    # elif re_no_trail.match(current_file) or re_no_trail_lower.match(current_file):
    #     return True
    # elif re_underscore.match(current_file) or re_underscore_lower.match(current_file):
    #     return True
    # elif re_space.match(current_file) or re_space_lower.match(current_file):
    #     return True

    if re_dash.match(current_file) \
            or re_dash_lower.match(current_file) \
            or re_no_trail.match(current_file) \
            or re_no_trail_lower.match(current_file) \
            or re_underscore.match(current_file) \
            or re_underscore_lower.match(current_file) \
            or re_space.match(current_file) \
            or re_space_lower.match(current_file):
        return True


def parse_table_info(product, data_table_rows):

    # data table is in separate sheet
    """

    :param product: Product
    :param data_table_rows: List
    :return:
    """
    result_data_table = []

    for index in range(0, len(data_table_rows)-1):
        if data_table_rows[index][1] == product.id:

            # Table Header
            result_row = list(data_table_rows[index])
            result_row.pop(0)
            result_row.pop(0)
            result_row = filter(None, result_row)
            result_data_table.append(result_row)
            print '             ' + str(result_row)

            index_product_data_table = index + 1
            while data_table_rows[index_product_data_table][1] == '':
                result_row = list(data_table_rows[index_product_data_table])
                result_row.pop(0)
                result_row.pop(0)
                result_row = filter(None, result_row)
                result_data_table.append(result_row)
                print '             ' + str(result_row)

                index_product_data_table += 1

                if index_product_data_table == len(data_table_rows):
                    break

    return result_data_table

def parse_table_junk(product, product_row):
    """

    :param product: Product
    :param product_row: List
    :return:
    """
    # mock up
    #product_row = 'Art No.,L,D,A,H'

    result_data_table = []
    current_col = 7

    # Table header
    result_row = product_row[current_col].split(',')
    result_data_table.append(list(result_row))
    print '             ' + str(result_row)

    current_col += 1
    while product_row[current_col] != '':
        result_row = product_row[current_col].split(',')
        result_data_table.append(list(result_row))
        print '             ' + str(result_row)
        current_col += 1

        if current_col == len(product_row):
            break

    return result_data_table



username = 'teerasej@amaround.com'
password = 'flamingdart'

gc = gspread.login(username, password)
print 'Singed in...'
trakulthai_doc = gc.open("Trakul Thai Product Sheet")
print 'Opened document...'
product_sheet = trakulthai_doc.worksheet('armstrong')
# product_data_table = trakulthai_doc.worksheet('armstrong-table-data')
# data_table_rows = product_data_table.get_all_values()
print 'Got all worksheets...'

# product_ids = product_sheet.col_values(2)
product_rows = product_sheet.get_all_values()
print 'Product total: ' + str(len(product_rows) - 1)
print 'Start processing product item...'

for product_index in range(1, len(product_rows)):

    product_row = product_rows[product_index]

    # create product object
    product = Product(id=product_row[1],
                      name=product_row[2],
                      eng_name=product_row[3],
                      detail=product_row[4],
                      categories=product_row[5].split(','),
                      status=product_row[0],
                      table_type=int(product_row[6]))

    print '[' + product.id + '] start -----------'

    ###### Parse data table #######
    # print '     parsing data table...'
    # if product.table_type == 2:
    #     product.table_info = parse_table_info(product, data_table_rows)
    # elif product.table_type == 1:
    #     product.table_info = parse_table_junk(product, product_row)
    # elif product.table_type == 0:
    #     print '         No data table exist.'
    # else:
    #     print '         [WARN] product data table type not found.'
    # print '     finish parsing data table...'

    ###### check image files #######
    print '\n'
    print '     checking image files...'

    for root, dirs, files in os.walk("03 Armstrong"):
        for current_file in files:
            if found(product, current_file):

                file_name = current_file.title()

                # assign image

                if re.search('catalog', file_name, re.IGNORECASE):

                    if product.feature_image_file is None:
                        product.feature_image_file = current_file
                        print '         [Featured image]: ' + file_name
                    else:
                        product.product_image_files.append(current_file)
                        print '         [Product image]: ' + file_name
                else:
                    product.product_image_files.append(current_file)
                    print '         [Product image]: ' + file_name

    # Update product status in sheet
    status = ''
    if not product.feature_image_file and len(product.product_image_files) == 0:
        status = 'no image'
    elif product.feature_image_file and len(product.product_image_files) > 0:
        status = '1'
        product.status = 1
    else:
        if product.feature_image_file is None:
            status = 'no featured image'
        elif len(product.product_image_files) == 0:
            status = 'no product image'

    print '         [IMAGE STATUS]: ' + status

    # try:
    #     target_product_cell = product_sheet.find(product.id)
    #     product_sheet.update_cell(target_product_cell.row, 1, status)
    # except Exception:
    #     print '         [ERROR] 1st fail update status to product sheet'
    #     try:
    #         target_product_cell = product_sheet.find(product.id)
    #         product_sheet.update_cell(target_product_cell.row, 1, status)
    #     except Exception:
    #         print '         [ERROR] 2nd fail update status to product sheet'
    #         try:
    #             target_product_cell = product_sheet.find(product.id)
    #             product_sheet.update_cell(target_product_cell.row, 1, status)
    #         except Exception:
    #             print '         [FATAL] cannot update status to product sheet: ' + product.id

    print '     finish checking image files...'



    # post to wordpress
    print '\n'
    print '     Posting to wordpress...'




    print '[' + product.id + '] finished -----------'


    # product_code = product_id.replace(' ','')

    # for root, dirs, files in os.walk("03 Armstrong"):
    # for file in files:
    #         if found(product_id,file):






    # reObj = re.compile(fnmatch.translate('*AS20*'))
    # for root, dirs, files in os.walk("03 Armstrong"):
    #     for file in files:
    #         if reObj.match(file):
    #              print(os.path.join(root, file))