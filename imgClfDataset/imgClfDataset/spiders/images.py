import scrapy
from scrapy.loader import ItemLoader
from ..items import ImgclfdatasetItem

class images(scrapy.Spider):
    
    name = 'images'
    classname = "photographs" # [ "photographs", "paintings"]
    start_urls = [
        f"https://fineartamerica.com/art/{classname}"
    ]
    page = 1
    image_urls = []
    image_titles = []
    page_limit = 10

    def parse(self, response):
        
        self.image_titles = response.xpath('//p[@class="flowArtworkName"]//text()').extract()
        self.image_urls  = response.xpath('//div[@class="flowImageContainerDiv"]/a/img/@data-src').extract()
        
        self.page= self.page + 1
        
        if self.page <= self.page_limit:        
            item = ImgclfdatasetItem()
            item['image_urls'] = self.image_urls
            item['image_titles'] = self.image_titles
            yield item                
            
            next_page = f'https://fineartamerica.com/art/{self.classname}?page={self.page}'
            yield scrapy.Request(next_page, callback=self.parse)
        

                



