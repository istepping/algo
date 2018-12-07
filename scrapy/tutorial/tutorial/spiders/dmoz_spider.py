import scrapy

##
class DmozSpider(scrapy.Spider):
    name = "dmoz" # 取别spider
    allowed_domains = ["readthedocs.io"]
    # 为每一个url创建一个request
    start_urls=[
        "https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html",
        "https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html"
    ]
    # request请求成功回调函数
    def parse(self, response):
        filename=response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)