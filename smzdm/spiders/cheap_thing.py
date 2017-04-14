import scrapy
from smzdm.items import CheapThingsListItem


class CheapThings(scrapy.Spider):
    name = 'CheapThings'
    base_url_string = 'http://faxian.smzdm.com/9kuai9/p'
    start_urls = []
    for i in range(1, 100):
       start_urls.append(base_url_string+str(i)+'/')

    def parse(self, response):
        items = []
        article_list = response.xpath('//*[@id="feed-main-list"]/li')
        print response.url
        for sel in article_list:
            item = CheapThingsListItem()
            item['time'] = sel.xpath('@timesort').extract()[0]
            item['article_id'] = sel.xpath('@articleid').extract()[0]
            item['article_url'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="feed-ver-pic"]/a[@href and not(@class)]').xpath('@href').extract()[0]
            item['title'] = sel.xpath('div[@class="feed-block-ver "]/h5/a/text()').extract()[0]
            item['price'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="z-highlight z-ellipsis"]/text()').extract()[0]
            item['source'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="feed-ver-pic"]/a[@class]/text()').extract()[0]
            items.append(item)
            # yield scrapy.Request(item['article_url'][0], callback=self.get_article_detail)
        return items

    def get_article_detail(self, response):
        print(response.url)
        items = []
        item = CheapThingsListItem()
        item['article_url'] = ['test']
        items.append(item)
        return items
