import scrapy
import re

class DataMiner(scrapy.Spider):
    name = "DataMiner"

    def start_requests(self):
        urls = []

        # Nacita vsetky zdrojove stranky z pripraveneho suboru
        sources_filename = 'source_links'
        with open(sources_filename) as f:
            urls = f.readlines()

        # Odstrani biele znaky na koncoch riadkov
        urls = [line.strip() for line in urls]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        data = []
        births_ul = response.xpath('//span[@id=$val]/../following-sibling::ul', val='Births')[0]
        li_elements = births_ul.css('li').extract()

        # Vyparsuje a naformatuje data
        for li in li_elements:
            formatted_line = re.sub('<([\w `"\'\/,.:;&()%=\-+#–?!]+)>', '', str(li))
            data.append(formatted_line)

        # Zapis do suboru
        filename = 'raw_data'
        day_identifier = str.lower(response.css('h1::text').extract_first())

        with open(filename, 'a') as f:
            f.write('#' + day_identifier + '\n')
            for line in data:
                f.write(line + '\n')
