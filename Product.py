__author__ = 'Teerasej'


class Product:

    def __init__(self, id, name, categories):
        self.id = id
        self.name = name
        self.categories = categories

        self.feature_image_id = None
        self.product_image_ids = []
        self.table_info_string = None
        self.post_id = None
        self.post_status = 0

    @property
    def feature_image_name(self):
        return self.id.replace(' ','')

    @property
    def feature_image_file_name(self):
        return self.feature_image_name + '.jpg'



