import unittest 

from scrapy.http import HtmlResponse, Request
from books.spiders.book import BookSpider
from books.items import BooksItem

class BookSpiderTest(unittest.TestCase):
    """testar se a spider escava os livros e os links da pagina"""
    def setUp(self):
        self.spider = BookSpider()
        self.example_html = """
        <html>
    <body>
        <ul>
            <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                <article class="product_pod">
                    <div class="image_container">
                        <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html">
                            <img src="media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg" alt="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)" class="thumbnail">
                        </a>
                    </div>
                    <p class="star-rating Five">
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                    </p>
                    <h3>
                        <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" title="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)">
                            Scott Pilgrim's Precious Little Life
                        </a>
                    </h3>
                    <div class="product_price">
                        <p class="price_color">£52.29</p>
                        <p class="instock availability">
                            <i class="icon-ok"></i>
                            In stock
                        </p>
                    </div>
                </article>
            </li>
            <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                <article class="product_pod">
                    <div class="image_container">
                        <a href="catalogue/another-book/index.html">
                            <img src="media/cache/another-image.jpg" alt="Another Book" class="thumbnail">
                        </a>
                    </div>
                    <p class="star-rating Four">
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                        <i class="icon-star"></i>
                    </p>
                    <h3>
                        <a href="catalogue/another-book/index.html" title="Another Book">
                            Another Book
                        </a>
                    </h3>
                    <div class="product_price">
                        <p class="price_color">£29.99</p>
                        <p class="instock availability">
                            <i class="icon-ok"></i>
                            In stock
                        </p>
                    </div>
                </article>
            </li>
        </ul>
        <li class="next"><a href="catalogue/page-2.html">next</a></li>
    </body>
</html>
       """   
        self.response = HtmlResponse(
            url ="https://books.toscrape.com",
            body = self.example_html,
            encoding="utf-8"
        )

def test_parse_scrapes_correct_book_information(self):
    """testa se a spider escava a informação correta de cada livro"""
    # coleta os items  que foram gerados na lista
    # pra que ppssa ser possivel itinerar mais de
    # uma vez.
    results = list(self.spider.parse(self.response))
    
    
    # tem que ter mais do que 2 items pra book e um pedido de pagination
    book_items = [item for item in results if isinstance(item, BooksItem)]
    pagination_requests = [
        item for item in results if isinstance(item, Request)
    ]
    
    self.assertEqual(len(book_items), 2)
    self.assertEqual(len(pagination_requests), 1)

def test_parse_creates_pagination_request(self):
    """testa se a spider cria o pedido da paginação corretamente"""
    results = list(self.spider.parse(self.response))
    pagination_requests = [item for item in results if isinstance(item, Request)]
    self.assertEqual(len(pagination_requests), 1) # verifica se tem um pedido de paginação
    self.assertEqual(pagination_requests[0].url, "https://books.toscrape.com/catalogue/page-2.html")

if __name__ == "__main__":
    unittest.main()