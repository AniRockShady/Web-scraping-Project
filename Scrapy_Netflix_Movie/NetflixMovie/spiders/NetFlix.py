import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class NetflixSpider(scrapy.Spider):
    name = "netflix_spider"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = ["https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"]

    def parse(self, response):
    #     xpath = '//*[@id="h-2-cafe-makario-everett-washington"]'
    #     selection = response.xpath(xpath)
    #     for s in selection:
    #         l = Link()
    #         l['link'] = response.urljoin(s.get())
    #         yield l
    #     pass

    #    coffee_shops = response.xpath('//div[@class="wp-block-heading"]//li')

        xpath_com = '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div'

        for i in range(1,101):
            xpath = f'{xpath_com}[{i}]/div[3]/div[1]/div[1]/div/div/h2/a/@href'
            shop = response.xpath(xpath).get()
            yield {
                'Link': response.urljoin(shop)
            }