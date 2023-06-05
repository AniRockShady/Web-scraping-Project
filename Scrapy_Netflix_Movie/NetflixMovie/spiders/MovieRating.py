import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class NetflixSpider(scrapy.Spider):
    name = "rating_spider"
    allowed_domains = ["rottentomatoes.com"]

    def start_requests(self):
        try:
            with open("netflix.csv",'rt') as k:
                url_add = [url.strip() for url in k.readlines()][1:]

                print(url_add)

                print("DEBUGING__________________________________________-")

        except FileNotFoundError: 
            url_add = []

        for url in url_add:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        
        name = '//h1[@slot="title" and @class="title" and @data-qa="score-panel-title"]/text()'
        year = '//p[@slot="info" and @class="info" and @data-qa="score-panel-subtitle"]/text()[1]'
        rating = '//score-board[@data-qa="score-panel"]/@tomatometerscore'
        # category = '//p[@slot="info" and @class="info" and @data-qa="score-panel-subtitle"]/text()[2]'

        get_name = response.xpath(name).getall()
        get_year = response.xpath(year).getall()
        get_ratings = response.xpath(rating).getall()
        # get_category = response.xpath(category).getall()

        yield {
            'film_name': get_name,
            'film_year': get_year,
            'film_ratings': get_ratings
        }

        
