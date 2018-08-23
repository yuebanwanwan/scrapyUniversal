import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    #获取爬取时使用的Spider名称
    spider = custom_settings.get('spider')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    #合并配置,将json中的settings合并到创建项目时自动生成的settings
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    #启动爬虫
    process.crawl(spider,**{'name':name})
    process.start()

if __name__ == '__main__':
    run()