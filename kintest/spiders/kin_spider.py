import scrapy
from ..items import KintestItem


class QuotesSpider(scrapy.Spider):
    name = 'kin'
    start_urls = [
        'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7000000/'
    ]

    def parse(self, response):
        url_base = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC'
        for i in range(7000000, 7685418):
            url_content = url_base + str(i)
            yield response.follow(url_content, self.parse_doc)

    def parse_doc(self, response):
        items = KintestItem()
        title = response.css('.content-title::text').extract()
        abstract = response.css('.p-first-last::text').extract()
        text = response.css('.tsec > p::text').extract()
        figure = response.css('.caption p::text').extract()

        items['title'] = title
        items['abstract'] = abstract
        items['text'] = text
        items['figure'] = figure
        yield items




    # # def parse_doc(self, response):
    #     items = KintestItem()
    #     abstract = response.css('.p-first-last::text').extract()
    #     text = response.css('.tsec > p::text').extract()
    #     figure = response.css('.caption p::text').extract()
    #
    #     items['abstract'] = abstract
    #     items['text'] = text
    #     items['figure'] = figure
    #     yield items
    # cd kintest
    # scrapy crawl kin -o 파일이름.json