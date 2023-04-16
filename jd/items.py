import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    score = scrapy.Field()
    time = scrapy.Field()
