from scrapy.loader import  ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose

class NewsLoader(ItemLoader):
    #数据处理对象，返回列表的第一个非空值
    default_output_processor = TakeFirst()

class ChinaLoader(NewsLoader):
    text_out = Compose(Join(),lambda s:s.strip())
    source_out = Compose(Join(),lambda s:s.strip())

class DaDaoChaoTianLoader(NewsLoader):
    text_out = Compose(Join(),lambda  s:s.strip())
    source_out = Compose(Join(),lambda  s:s.strip())