import scrapy
import html2text

class AmericanUniversitiesSpider(scrapy.Spider):
    name = "american_universities"
    converter = html2text.HTML2Text()

    def start_requests(self):
        url = "http://www.ntnu.no/international/usa/tableusacanada.htm"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        trs = response.css("tr")#.extract()
        for tr in trs:
            tds = tr.css("td")
            if tds and tds[0].extract() == "<td>USA</td>":
                print(self.converter.handle(tds[1].extract()))

# def parse(self, response):
#     trs = response.css("tr")#.extract()
#     for tr in trs:
#         tds = tr.css("td")
#         if tds and tds[0] == "USA":
#             print(tds[1].extract())
