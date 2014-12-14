__author__ = 'teerasej'



template = '[vc_row][vc_column width="2/3"][vc_simple_slider ids="{slider}" type="1"][/vc_column][vc_column width="1/3"][vc_column_text][sc:heading-product-detail][/vc_column_text][vc_table vc_table_theme="classic_blue"]{data_table}[/vc_table][vc_separator icon="star"][vc_column_text][sc:armstrong-prod-contact][/vc_column_text][vc_separator icon="star"][/vc_column][/vc_row][vc_row section="yes" parallax_speed="slow"][vc_column width="1/1"][vc_column_text][sc:heading-product-related][/vc_column_text][vc_separator type="invisible" icon="star"][vc_recent_works columns="4" category="door-closer"][/vc_column][/vc_row]'

# {slider}
# 1756,1248,...
# [vc_simple_slider ids="1776,1777" type="1"]
product_image_ids = [1000,2000]


# {data table}
data_table = [
    ['Art id.','L','H','D'],
    [100,1,2,3],
    [200,1,2,3],
    [300,1,2,3]
]

temp = []
for row in data_table:
    r = str(row).replace('\'','')
    temp.append(str(r).strip('[]'))

'|'.join(temp)
# repls = ('hello', 'goodbye'), ('world', 'earth')
# s = 'hello, world'
# reduce(lambda a, kv: a.replace(*kv), repls, s)