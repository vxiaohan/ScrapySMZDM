import scrapy
from smzdm.items import CheapThingsListItem


class CheapThings(scrapy.Spider):
    name = 'CheapThings'
    base_url_string = 'http://faxian.smzdm.com/9kuai9/p'
    start_urls = []
    for i in range(1, 3):
       start_urls.append(base_url_string+str(i)+'/')

    def parse(self, response):
        if response.url.split('/')[-2] == '9kuai9':
            filename = 'result/p1.html'
        else:
            filename = 'result/' + response.url.split('/')[-2]+'.html'
        print(filename)
        print(response.url.split('/'))
        items = []
        for sel in response.xpath('//*[@id="feed-main-list"]/li'):
            print sel.xpath('div[@class="feed-block-ver "]/div[@class="feed-ver-pic"]/a[@href and not(@class)]').xpath('@href').extract()
            item = CheapThingsListItem()
            item['time'] = sel.xpath('@timesort').extract()
            item['article_id'] = sel.xpath('@articleid').extract()
            item['article_url'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="feed-ver-pic"]/a[@href and not(@class)]').xpath('@href').extract()
            item['title'] = sel.xpath('div[@class="feed-block-ver "]/h5/a/text()').extract()
            item['price'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="z-highlight z-ellipsis"]/text()').extract()
            item['source'] = sel.xpath('div[@class="feed-block-ver "]/div[@class="feed-ver-pic"]/a[@class]/text()').extract()
            print(item)
            items.append(item)
            print(type(item['article_url']))
            yield scrapy.Request(item['article_url'][0], callback=self.get_article_detail)

    def get_article_detail(self, response):
        print(response.url)
        items = []
        item = CheapThingsListItem()
        item['article_url'] = ['test']
        items.append(item)
        return items
