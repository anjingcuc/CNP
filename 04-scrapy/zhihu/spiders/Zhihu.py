# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu.items import QuestionItem
from zhihu.items import AnswerItem


class ZhihuSpider(scrapy.Spider):
  name = 'Zhihu'
  start_urls = [
      'https://www.zhihu.com/api/v4/topics/19551137/feeds/essence?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B'
  ]


  def parse_question(self, response):
    answers_page = json.loads(response.text)
    answers_data = answers_page['data']

    for answer in answers_data:
      answer_item = AnswerItem()

      answer_item['id'] = answer['id']

      answer_item['author_id'] = answer['author']['id']
      answer_item['author_name'] = answer['author']['name']
      answer_item['author_gender'] = answer['author']['gender']

      answer_item['content'] = answer['excerpt']
      answer_item['voteup_count'] = answer['voteup_count']

      yield answer_item

  def parse(self, response):
    answers_page = json.loads(response.text)
    answers_data = answers_page['data']

    for answer in answers_data:
      info = answer.get('target')

      question_info = info.get('question')
      if question_info is not None:
        question_url_format = 'https://www.zhihu.com/api/v4/questions/{id}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&platform=desktop&sort_by=default&limit={limit}&offset={offset}'

        yield scrapy.Request(
            question_url_format.format(
                id=question_info['id'], limit=10, offset=0),
            callback=self.parse_question)

    if not answers_page['paging']['is_end']:
      next_url = answers_page['paging']['next']

      yield scrapy.Request(next_url, callback=self.parse)
