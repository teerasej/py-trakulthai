import Product

__author__ = 'Teerasej'





class Uploader:

    def __init__(self, image_dir_path ):
        self.image_dir_path = image_dir_path
        self.product_not_upload_list = []





    def upload_product(self, product):
        """

        :param product: Product
        :return:
        """

        if self.is_featured_image_exist(product):
            print '[Found] Featured image: ' + product.feature_image_file_name
            product.featured_image_id = self.upload_image( self.get_full_path(product.feature_image_file_name))
        else:
            print '[Not Found] Feature image...'
            self.product_not_upload_list.append(product)
            return

        if self.is_product_image_exist(product):
            product_image_file_name_list = product.product_image_file_name_list()
            product_image_count = len(product_image_file_name_list)
            print '[Found] Product images: ' + product_image_count
            for i in range(product_image_count):
                print '     (' + (i+1) + ') ' + product_image_file_name_list[i]


            print '[Upload | start] product images... '
            for image_name in  product_image_file_name_list:
                upload_id = self.upload_image( self.get_full_path(image_name) )
                product.product_image_ids.append( upload_id )
                print '     Image ID: ' + upload_id + ' [' + image_name + ']'
            print '[Upload | finish]'

        else:
            print '[Not Found] product images...'
            self.product_not_upload_list.append(product)
            return

        # start uploading
        self.post(product)



    def is_featured_image_exist(product):
        """

        :param product: Product
        :return:
        """


        return False

    def is_product_image_exist(product):
        
        return False

    def get_full_path(self, image_name):
        pass

    def post(self, product):
        '''

        :param product: Product
        :return:
        '''
        post_name = self.get_post_name(product)
        feature_image_id = product.feature_image_id
        product_image_ids = product.product_image_ids
        table_info_string = product.table_info_string
        categories = product.categories
        pass


