import scrapy
from ..items import TurantulaItem


class AifundSpider(scrapy.Spider):
    name = 'aifund'
    allowed_domains = ['fund.10jqka.com.cn']
    start_urls = ['http://fund.10jqka.com.cn/datacenter/jz/']


    def parse(self, response):
#        item = TurantulaItem()
#        funds = response.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[4]/div/dl[2]')
#        for i in range(1, 124):
#            fund = response.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[4]/div/dl[2]/dd[%d]' % i).extract()
#            item['fund_company_name'] = fund[0].split('">')[2].split('<')[0]
#            item['fund_company_id'] = fund[0].split('">')[0].split('"')[-1]
#            yield item

        for link in self.link_extractor.extract_links(response):
            print(link)
