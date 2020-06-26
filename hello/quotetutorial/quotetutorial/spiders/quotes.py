import scrapy

from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes=response.css('.quote')
        for quote in quotes:
            item=QuoteItem()
            text=quote.css('.text::text').extract_first()
            author=quote.css('.author::text').extract_first()
            tags=quote.css('.tags .tag::text').extract()

            item['text']=text
            item['author']=author
            item['tags']=tags
            yield item
        #实现翻页功能：
        next=response.css('.pager .next a::attr(href)').extract_first()
        url=response.urljoin(next)
        yield scrapy.Request(url,callback=self.parse)



