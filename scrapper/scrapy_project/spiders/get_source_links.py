import scrapy
import re

class GetSourceLinksSpider(scrapy.Spider):
    name = "GetSourceLinksSpider"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/January_0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        #Vytvorenie vstupu (zoznamu vsetkych linkov) NEDOKONCENE!!
        source_links = []
        table = response.xpath('//table')

        # Parne a neparne mesiace
        for link in table.xpath('.//tr/td[@class=$val]/div/a//@href', val='navbox-list navbox-odd hlist'):
            source_links.append(link.extract())
        for link in table.xpath('.//tr/td[@class=$val]/div/a//@href', val='navbox-list navbox-even hlist'):
            source_links.append(link.extract())


        # Zapis linkov do suboru
        filename = 'source_links.txt'
        with open(filename, 'a') as f:
            for line in source_links:
                f.write('https://en.wikipedia.org' + line + '\n')
            f.close()
