import scrapy
from RawData.items import  Rawdataitem
from scrapy.loader import ItemLoader

class images(scrapy.Spider):

    name = "raw_paint"
    start_urls = [
    "https://fineartamerica.com/art/photographs"
    ]
    page = 1

    def parse(self, response):
        title = response.xpath('//div[@class= "searchengineresultdiv"]/div/a/img/@title').extract()
        urls = response.xpath('//div[@class= "searchengineresultdiv"]/div/a/img/@data-src').extract()      
        self.page= self.page + 1
        for url, name in zip(urls, title):
            yield Rawdataitem(file_urls = [url], title= name)

        next_page = f'https://fineartamerica.com/art/photographs?page={self.page}'
        yield scrapy.Request(next_page, self.parse)
        

                



