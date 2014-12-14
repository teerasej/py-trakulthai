import Product
import Uploader
import ProductManager

__author__ = 'Teerasej'

IMAGE_DIR = 'images'


print 'Initial system...'
preparer = ProductManager.ProductManager('teerasej@amaround.com','flamingdart','trakul thai product sheet')
uploader = Uploader.Uploader(IMAGE_DIR)

products = preparer.get_products()

for product in products:
    processed_product = uploader.upload_product(product)
    preparer.update_product_info(processed_product)

print '------'
print 'UPLOAD FINISHED'
