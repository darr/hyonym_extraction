#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : sougou.py
# Create date : 2019-08-10 15:01
# Modified date : 2019-08-10 17:59
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from urllib import request
from lxml import etree
from urllib import parse
import jieba.posseg as pseg

class SougouBaike:
    def get_html(self, url):
        return request.urlopen(url).read().decode('utf-8').replace('&nbsp;', '')

    def find_sofouid(self, word):
        url = "http://baike.sogou.com/v78781.html?fromTitle=%s" % parse.quote(word)
        #print(url)
        pg = self.get_html(url)
        selector = etree.HTML(pg)
        data_href_lt = selector.xpath('//ol[@class="semantic_item_list"]/li/a/@data-href')

        url_lt = []
        url_lt.append(url)
        for i in range(len(data_href_lt)):
            info_url = "http://baike.sogou.com%sfromTitle=%s" % (data_href_lt[i], parse.quote(word))
            url_lt.append(info_url)

        return url_lt

    def info_extract(self, word):
        info_url = self.find_sofouid(word)
        #print(info_url)
        info_list = list()
        for i in range(len(info_url)):
            selector = etree.HTML(self.get_html(info_url[i]))
            info_data = self.extract_sogou(selector)
            info_list.append(info_data)

        infos = [info for info in info_list if len(info) > 2]
        return infos

    def extract_sogou(self, selector):
        info_data = {}
        lt = selector.xpath('//div[@class="relevant_wrap"]')
        info_data['tags'] = [item.replace('\n', '') for item in selector.xpath('//div[@class="relevant_wrap"]/a/text()')]
        if selector.xpath('//li[@class="current_item"]/text()'):
            info_data['current_semantic'] = selector.xpath('//li[@class="current_item"]/text()')[0].replace('    ', '').replace('（','').replace('）','')
        else:
            info_data['current_semantic'] = ''
        tables = selector.xpath('//table[@class="abstract_list"]')
        for table in tables:
            attributes = table.xpath('./tbody/tr/th/text()')
            values = [td.xpath('string(.)') for td in table.xpath('./tbody/tr/td')]
            for item in zip(attributes, values):
                info_data[item[0].replace(' ', '').replace('\xa0','')] = item[1].replace('    ', '')
        #print(info_data)
        return info_data

    def checksogou_polysemantic(self, selector):
        semantics = ['http://baike.sogou.com' + sem.split('?')[0] for sem in selector.xpath("//ol[@class='semantic_item_list']/li/a/@href")]
        names = [name for name in selector.xpath("//ol[@class='semantic_item_list']/li/a/text()")]
        info_list = list()
        if semantics:
            for item in zip(names, semantics):
                selector = etree.HTML(self.get_html(item[1]))
                info_data = self.extract_sogou(selector)
                info_data['current_semantic'] = item[0].replace('（','').replace('）','')
                if info_data:
                    info_list.append(info_data)
        return info_list

