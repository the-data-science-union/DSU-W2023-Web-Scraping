# install scrapy first into terminal
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    # set a name for the spider that you will use to refer to it :D ex. "scrapy crawl myspider"
    name = "myspider"

    # list of names of acceptable links for where we want to crawl + scrape
    allowedDomains = ["toscrape.com"] # in this example, we want to stay on this website toscrape.come

    # the starting url of where we will start scraping from
    start_urls = [
        "http://books.toscrape.com/"
    ]

    # tuple of rules on where to crawl
    rules = (
        # allowing the links that have the word 'catalogue' and 'category' to go to all the pages of books
        Rule(LinkExtractor(allow="catalogue/category")),
        # sidenote, rmbr if you only have one item in a tuple, need an additional ',' at the end to be recognized as a tuple

        # ^above gives us all the links with 'catalogue' and 'category
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
        # callback -> "parse_item", need to define this function now
    )

    # webscraping part
    def parse_item(self, response):
        # define the parts you want to extract using the 'inspect' feature on the webpage
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            #"availability": response.css(".availability::text").get()
        }


# command to get an output file (can do csv too :D)
# scrapy crawl myspider -o output.json

# command to use interactive shell to explore html codes
# scrapy shell http://books.toscrape.com/