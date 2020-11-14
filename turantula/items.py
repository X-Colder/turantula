# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TurantulaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_company_id = scrapy.Field()
    fund_company_name = scrapy.Field()

