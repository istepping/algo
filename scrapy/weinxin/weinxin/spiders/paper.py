import scrapy
import subprocess
from scrapy.http import HtmlResponse
from scrapy.selector import Selector


class PaperSpider(scrapy.Spider):
    name = "paper"
    allowed_domains = ['qq.com']
    start_urls = [
        "http://weixin.sogou.com/weixin?query=大数据文摘"
    ]

    def parse(self, response):
        href = response.selector.xpath('//div[@id="sogou_vr_11002301_box_0"]/@href').extract()[0]
        cmd = r"F:\python\phantomjs-2.1.1-windows\bin\phantomjs ./getBody.js '%s'" % href
        stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        response = HtmlResponse(url=href, body=stdout)

        for selector in Selector(response=response).xpath('//*[@id="history"]/div/div/div/div'):
            hrefs = selector.xpath('h4/@hrefs').extract()[0].strip()
            title = selector.xpath('h4/text()').extract()[0].strip()
            abstract = selector.xpath('//*[contains(@class, "weui_media_desc")]/text()').extract()[0].strip()
            pubtime = selector.xpath('//*[contains(@class, "weui_media_extra_info")]/text()').extract()[0].strip()
            print(hrefs)
            print(title)
            print(abstract)
            print(pubtime)

    def parse_profile(self, response):
        print(response.body)
