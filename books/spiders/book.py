import scrapy
from ..items import BooksItem



class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        '''
        @url https://books.toscrape.com
        @returns item 20 20
        @returns request 1 50
        @scrapes url titulo preço
        '''
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = response.urljoin(book.css("h3 > a::attr(href)").get())    
            item["title"] = book.css("h3 > a::attr(title)").get()
            item["price"] = book.css(".price_color::text").get()
            yield item  
            
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            # Transformando a url relativa em absoluta
                next_page_url = response.urljoin(next_page)
                
                self.logger.info(
                    f"Navegando para a próxima pagina com o URL {next_page_url}"
                )
                # Passando url absoluta pra request
                yield scrapy.Request(
                    url=next_page,
                    callback=self.parse,
                    errback=self.log_error
                )
         
    
    def log_error(self, failure):
        self.logger.error(repr(failure))
   
    
        
        
            
            
            
            
        
