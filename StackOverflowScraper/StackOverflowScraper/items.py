# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_question_value(text):
    if text not in [' ', ', ']:
        return int(text.split()[0])

class StackoverflowscraperItem(Item):
    tag_title = Field(
        output_processor = TakeFirst()
    )
    tag_link = Field(
        output_processor = TakeFirst()
    )
    tag_desc = Field(
        output_processor = TakeFirst()
    )
    tag_que_count = Field(
        input_processor = MapCompose(get_question_value),
        output_processor = TakeFirst()
    )
    tag_questions = Field()
    tag_number = Field(
        output_processor = TakeFirst()
    )
