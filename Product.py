__author__ = 'Teerasej'


class Product:

    def __init__(self, **product):
        self.id = product.get('id', None)
        self.name = product.get('name', None)
        self.eng_name = product.get('eng_name', None)
        self.detail = product.get('detail', None)
        self.categories = product.get('categories', [])
        self.status = product.get('status', 0)

        self.table_info = product.get('table_info', {})
        self.table_type = product.get('table_type', None)

        # Image information
        self.feature_image_id = None
        self.feature_image_file = None

        self.product_image_ids = []
        self.product_image_files = []

        # Post information
        self.post_id = None
        self.post_status = 0


    @property
    def product_id_no_string(self):
        return self.id.replace(' ', '')


    @property
    def feature_image_file_name(self):
        return self.product_id_no_string + '.jpg'



