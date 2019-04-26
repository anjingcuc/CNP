# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class AnswerPipeline(object):
  def __init__(self):
    f = open('answers.csv', 'w')
    fieldnames = [
        'id', 'author_id', 'author_name', 'author_gender', 'content',
        'voteup_count'
    ]

    self.writer = csv.DictWriter(f, fieldnames=fieldnames)
    self.writer.writeheader()

  def process_item(self, item, spider):
    self.writer.writerow(item)
    return item
