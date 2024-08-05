import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import BeautifulFreeImgItem
from itemloaders.processors import MapCompose
from urllib.parse import urljoin



class BeautifulImgSpider(CrawlSpider):
    name = "beautiful_img"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//a[@class = 'zNNw1']")), callback='parse_item', follow=True),)

    def parse_item(self, response):
        loader = ItemLoader(item=BeautifulFreeImgItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
        
        loader.add_xpath("category", "//a[@class = 'm7tXD jhw7y TYpvC']/text()")
        loader.add_xpath("image_name", "//h1/text()")
        image_urls = response.xpath("//div[@class = 'wdUrX']/img[2]/@src").extract_first()
        loader.add_value("image_urls", image_urls)
        
        yield loader.load_item()