import scrapy


class BookCatalogueSpider(scrapy.Spider):
    name = "book_catalogue"
    allowed_domains = ["www.labirint.ru"]
    start_urls = ["https://www.labirint.ru/books/"]

    def parse(self, response):
        genres = response.xpath("//div[3]/div[1]/div[2]/div/div[3]/ul/li/a")
        for genre in genres:
            genre_name = genre.xpath(".//text()").get()
            link = genre.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.book_parse, meta={'book_genre' : genre_name})

    def book_parse(self, response):
        genre = response.request.meta['book_genre']
        book_info = response.xpath('//div[@class="genres-carousel__container  products-row "]/div/div')
        for info in book_info:
            author = info.xpath('.//div[@class="product-author"]/a/span/text()').get()
            book = info.xpath('.//span[@class="product-title"]/text()').get()
            price_now = info.xpath('.//span[@class="price-val"]/span/text()').get()
            pubhouse = info.xpath('.//div[@class="product-pubhouse"]/a/span/text()').get()
            price_old = info.xpath('.//span[@class="price-gray"]/text()').get()

            yield{
                'genre' : genre,
                'author' : author,
                'book' : book,
                'pubhouse' : pubhouse,
                'price_now' : price_now,
                'price_old' : price_old,
            }