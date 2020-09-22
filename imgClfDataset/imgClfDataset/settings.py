
BOT_NAME = 'imgClfDataset'

SPIDER_MODULES = ['imgClfDataset.spiders']
NEWSPIDER_MODULE = 'imgClfDataset.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/Users/siddesh.suseela/Work/ntuoss-dataScrapingAndDataCleaning/imgClfDataset/raw_dataset/paintings'

