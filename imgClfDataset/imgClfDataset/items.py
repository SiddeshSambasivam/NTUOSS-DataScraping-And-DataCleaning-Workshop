# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgclfdatasetItem(scrapy.Item):

    image_titles = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    
