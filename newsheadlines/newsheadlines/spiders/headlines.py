import scrapy

class newsheadlines(scrapy.Spider):
    
    name="news"
    start_urls = [
        'https://oilprice.com/Latest-Energy-News/World-News/'
    ]
    page = 1
    page_limit = 10

    def parse(self, response):
        if self.page <= self.page_limit:
            news_title = response.xpath("//h2[@class='categoryArticle__title']").extract()
            news_meta = response.xpath("//p[@class='categoryArticle__meta']").extract()
            self.page+=1
            for t, m in zip(news_title, news_meta):
                news_raw = {
                    'title': t,
                    'meta' : m,
                }

                yield  news_raw
            next_page  = f'https://oilprice.com/Latest-Energy-News/World-News/Page-{self.page}.html'
            yield scrapy.Request(next_page, self.parse)   

        