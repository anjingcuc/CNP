# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  id = scrapy.Field()
  title = scrapy.Field()
  url = scrapy.Field()

  pass


class AnswerItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  id = scrapy.Field()

  author_id = scrapy.Field()
  author_name = scrapy.Field()
  author_gender = scrapy.Field()

  content = scrapy.Field()
  voteup_count = scrapy.Field()

  pass