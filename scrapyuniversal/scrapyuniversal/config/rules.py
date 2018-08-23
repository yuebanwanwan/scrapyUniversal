from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

#处理以及修改通过restrict_xpaths筛选出来的链接
#参考https://scrapy.readthedocs.io/en/latest/topics/link-extractors.html#module-scrapy.linkextractors.lxmlhtml文档
#如果需要处理提取的链接则需要在Rule()中添加process_value参数，并传递函数对象或者直接使用lambda表达式
def process_value(value):
    pass
# 定义爬取网站的规则
rules = {
    'china':(
        #用于提取信息的Rule要放在提取链接的Rule之前
        Rule(LinkExtractor(allow='https://travel.china.com.*?html',
                       restrict_xpaths='//div[@class="r2_l"]//div[@class="m_L"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[@class="nextPage"]/@href'))
    ),
    'biqukan':(
        #对于该链接既要提取信息也要将其加入请求队列中
        Rule(LinkExtractor(allow='.*?.html',restrict_xpaths='//div[@class="page_chapter"]'),callback='parse_item',follow=True),
    )
}
