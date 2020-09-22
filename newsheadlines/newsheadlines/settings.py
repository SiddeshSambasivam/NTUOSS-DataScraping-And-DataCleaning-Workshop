BOT_NAME = 'newsheadlines'

SPIDER_MODULES = ['newsheadlines.spiders']
NEWSPIDER_MODULE = 'newsheadlines.spiders'



ROBOTSTXT_OBEY = True

FEED_FORMAT="csv"
FEED_URI="./raw_dataset/news_raw.csv"
