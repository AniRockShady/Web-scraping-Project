# Importing scrapy
import scrapy


class NetflixSpider(scrapy.Spider): #initializing the NetflixSpider class
    name = "t1_spider" #Spider name
    allowed_domains = ["rottentomatoes.com"] #Domain that is only allowed to crawl
    start_urls = ["https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"]


    def __init__(self, limit_pages=True, *args, **kwargs): #Initializing the NetflixSpider with __init__ method
        super().__init__(*args, **kwargs)
        self.limit_pages = limit_pages


    def parse(self, response): #parse method processing response from start_url
        links = []  #initializing an empty list

        xpath_com = '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div' #Xpath of the website block with link

        for i in range(0, 102): #Running the loop for 100+ time as Xpath is having common section with increasing order (numbers)
            xpath = f'{xpath_com}[{i}]/div[3]/div[1]/div[1]/div/div/h2/a/@href' #Combining the common Xpath + current order index i
            movie = response.xpath(xpath).get() #response object extracting url
            links.append(response.urljoin(movie)) #appending to the empty list

        if self.limit_pages: #Limiting number of links
            links = links[:100] #we target 100

        for link in links: #Loop iterating over the List link
            yield scrapy.Request(link, callback=self.parse_movie) #creating request object for each link and yielding to parse_movie method for processing 

        #parse_movie method is used as a callback function to handled response from the url


    def parse_movie(self, response): #method being called for each URL requested in parse
        name = response.xpath('//h1[@slot="title" and @class="title" and @data-qa="score-panel-title"]/text()').get() #extracting name using XPath
        year = response.xpath('//p[@slot="info" and @class="info" and @data-qa="score-panel-subtitle"]/text()[1]').get() #extracting year using Xpath
        rating = response.xpath('//score-board[@data-qa="score-panel"]/@tomatometerscore').get() #Extracting rating using Xpath

        #Above deatils are extracted from response to the links 

        year = year.split(",")[0].strip() #extracting just the year which is separated by comma from a string
        yield {
            'Link': response.url,
            'Title': name,
            'Year': year,
            'Ratings%': rating,
        }

        #Finally getting the Details as a dictionary
