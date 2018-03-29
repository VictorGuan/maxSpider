import scrapy 

class DmozSpider(scrapy.spiders.Spider):
    name ="domz"
    allowed_domains = ["domz.org"]
    start_urls = [
            "http://baike.daidu.com/item/Python/407313?fr=aladdin",
            "http://www.dmoz.org/Computers/Programing/Languages/Python/Books/"
            ]

    def parse(self,reponse):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body
