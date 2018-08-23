# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.utils import get_config
from scrapyuniversal.config.rules import rules
from scrapyuniversal.items import NewsItem
from scrapyuniversal.ItemLoader import ChinaLoader
from scrapyuniversal.items import DadaochaotianItem
from scrapyuniversal.ItemLoader import DaDaoChaoTianLoader


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self,name,*args,**kwargs):
        #config为dict或list类型
        config = get_config(name)
        self.config = config
        #此处的params表示spider对应的rules
        self.rules = rules.get(config.get('rules'))
        self.start_urls = config.get('start_urls')
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs)

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls,response=response)
            for key,value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key,*extractor.get('args'),**{'re':extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response,*extractor.get('args')))
                    yield loader.load_item()



