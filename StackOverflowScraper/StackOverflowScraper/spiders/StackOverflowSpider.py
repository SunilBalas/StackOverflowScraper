import scrapy
from StackOverflowScraper.items import StackoverflowscraperItem
from scrapy.loader import ItemLoader


class StackQuestionSpider(scrapy.Spider):
    name = 'StackQuestionSpider'
    #start_urls = ['http://stackoverflow.com/']

    def __init__(self):
        super().__init__()
        self.page_count = 1
        self.total_pages = 30

    def start_requests(self):
        base_url = "http://stackoverflow.com/questions"

        while self.page_count <= self.total_pages:
            yield scrapy.Request(
                f"{base_url}?tab=newest&page={self.page_count}"
            )
            self.page_count += 1

    def parse(self, response):
        print("[ RESPONSE ]")
        ques_div = response.css("div.s-post-summary--content")

        for que in ques_div:
            title = que.css("h3.s-post-summary--content-title a::text").get()
            desc = que.css("div.s-post-summary--content-excerpt::text").get().strip()
            tags = que.css("div.s-post-summary--meta-tags > ul li a::text").getall()
            yield {
                "title" : title,
                "desc" : desc,
                "tags" : tags
            }

class StackTagSpider(scrapy.Spider):
    name = "StackTagSpider"
    
    def __init__(self):
        super().__init__()
        self.page_count = 1
        self.total_pages = 5
        self.base_url = "http://stackoverflow.com"
        self.tag_count = 1

    def start_requests(self):
        tag_base_url = f"{self.base_url}/tags"

        while self.page_count <= self.total_pages:
            yield scrapy.Request(
                url=f"{tag_base_url}?page={self.page_count}"
            )
            self.page_count += 1

    def parse(self, response):
        print(f"[ RESPONSE ] =====> {self.page_count}")
        tag_card = response.css("div.s-card")

        for tag in tag_card:
            loader = ItemLoader(item=StackoverflowscraperItem())

            loader.add_value('tag_number', self.tag_count)
            loader.add_value('tag_title', tag.css("a.post-tag::text").get())
            loader.add_value('tag_link', tag.css("div.flex--item a").attrib['href'])
            loader.add_value('tag_desc', tag.css("div.flex--item.fc-medium::text").get().strip())
            loader.add_value('tag_que_count', tag.css("div.fs-caption > div.flex--item::text").get())            

            self.tag_count += 1
            yield loader.load_item()