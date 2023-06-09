import scrapy

class NetflixSpider(scrapy.Spider):
    name = "t1_spider"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = ["https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"]

    def parse(self, response):
        links = []

        xpath_com = '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div'

        for i in range(0, 101):
            xpath = f'{xpath_com}[{i}]/div[3]/div[1]/div[1]/div/div/h2/a/@href'
            movie = response.xpath(xpath).get()
            links.append(response.urljoin(movie))

        for link in links:
            yield scrapy.Request(link, callback=self.parse_movie)

    def parse_movie(self, response):
        name = response.xpath('//h1[@slot="title" and @class="title" and @data-qa="score-panel-title"]/text()').get()
        year = response.xpath('//p[@slot="info" and @class="info" and @data-qa="score-panel-subtitle"]/text()[1]').get()
        rating = response.xpath('//score-board[@data-qa="score-panel"]/@tomatometerscore').get()

        year = year.split(",")[0].strip()
        yield {
            'Link': response.url,
            'Title': name,
            'Year': year,
            'Ratings%': rating
        }

