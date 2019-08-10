#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : hudong.py
# Create date : 2019-08-10 14:59
# Modified date : 2019-08-10 18:49
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from urllib import request
from lxml import etree
from urllib import parse

class HudongBaike:
    def get_html(self, url):
        return request.urlopen(url).read().decode('utf-8').replace('&nbsp;', '')

    def info_extract(self, word):  # 互动百科
        url = "http://www.baike.com/wiki/%s" % parse.quote(word)
        #print(url)
        selector = etree.HTML(self.get_html(url))
        info_list = list()
        info_data = self.extract_hudong(selector)
        if selector.xpath('//li[@class="current"]/strong/text()'):
            info_data['current_semantic'] = selector.xpath('//li[@class="current"]/strong/text()')[0].replace('    ', '').replace('（','').replace('）','')
        else:
            info_data['current_semantic'] = ''
        info_list.append(info_data)
        #print(info_data)
        polysemantics = self.checkhudong_polysemantic(selector)
        if polysemantics:
            info_list += polysemantics

        infos = [info for info in info_list if len(info) > 2]
        #print(infos)
        return infos

    def extract_hudong(self, selector):
        info_data = {}
        info_data['desc'] = selector.xpath('//div[@id="content"]')[0].xpath('string(.)')
        info_data['intro'] = selector.xpath('//div[@class="summary"]')[0].xpath('string(.)').replace('编辑摘要', '')
        info_data['tags'] = [item.replace('\n', '') for item in selector.xpath('//p[@id="openCatp"]/a/text()')]
        for info in selector.xpath('//td'):
            attribute = info.xpath('./strong/text()')
            val = info.xpath('./span')
            if attribute and val:
                value = val[0].xpath('string(.)')
                info_data[attribute[0].replace('：','')] = value.replace('\n','').replace('  ','').replace('    ', '')
        return info_data

    def checkhudong_polysemantic(self, selector):
        semantics = [sem for sem in selector.xpath("//ul[@id='polysemyAll']/li/a/@href") if 'doc_title' not in sem]
        names = [name for name in selector.xpath("//ul[@id='polysemyAll']/li/a/text()")]
        info_list = list()
        if semantics:
            for item in zip(names, semantics):
                url = "https:%s" % item[1]
                #print(url)
                selector = etree.HTML(self.get_html(url))
                info_data = self.extract_hudong(selector)
                info_data['current_semantic'] = item[0].replace('（','').replace('）','')
                if info_data:
                    info_list.append(info_data)
        return info_list
