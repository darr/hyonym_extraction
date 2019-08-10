#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : baike.py
# Create date : 2019-08-09 14:45
# Modified date : 2019-08-10 18:56
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os

import jieba.posseg as pseg
from event import EventGraph
from baidu import BaiduBaike
from hudong import HudongBaike
from sougou import SougouBaike

class SemanticBaike:
    def __init__(self):
        cur = '/'.join(os.path.realpath(__file__).split('/')[:-1])
        self.tmp_file = os.path.join(cur, './baike_data/word_concept.txt')

    def extract_concept(self, word):
        '''根据instance本身抽取其概念'''
        wds = [w.word for w in pseg.cut(word) if w.flag[0] in ['n']]
        if not wds:
            return ''
        else:
            return wds[-1]

    def get_baidu_semantics(self, semantics, word):
        baidu = BaiduBaike()
        baidu_info = [[i['current_semantic'], i['tags']] for i in baidu.info_extract(word)]
        semantics += baidu_info

    def get_hudong_semantics(self, semantics, word):
        hudong = HudongBaike()
        hudong_info = [[i['current_semantic'], i['tags']] for i in hudong.info_extract(word)]
        semantics += hudong_info

    def get_sougou_semantics(self, semantics, word):
        sogou = SougouBaike()
        sogou_info = [[i['current_semantic'], i['tags']] for i in sogou.info_extract(word)]
        semantics += sogou_info

    def extract_main(self, word):
        '''对三大百科得到的semantic概念进行对齐'''
        print("baike:%s" % word)
        f = open(self.tmp_file, 'w+')

        semantic_dict = {}
        semantics = []

        tuples = []
        concepts_all = []

        self.get_baidu_semantics(semantics, word)
        self.get_hudong_semantics(semantics, word)
        self.get_sougou_semantics(semantics, word)

        for i in semantics:
            instance = i[0]
            concept = i[1]
            if not instance:
                continue
            if instance not in semantic_dict:
                semantic_dict[instance] = concept
            else:
                semantic_dict[instance] += concept

        # 对从百科知识库中抽取得到的上下位关系进行抽取

        for instance, concepts in semantic_dict.items():
            concepts = set([i for i in concepts if i not in ['', ' ']])
            concept_pre = self.extract_concept(instance)
            concepts_all += concepts
            concepts_all += [concept_pre]
            tuples.append([word, instance])
            tuples.append([instance, concept_pre])
            for concept in concepts:
                tuples.append([instance, concept])

        # 对词汇本身上下位义进行上下位抽取
        tmps = [[i, j] for i in concepts_all for j in concepts_all if j in i and i and j]
        tuples += tmps

        for tuple in tuples:
            if tuple[0] != tuple[1]:
                f.write('->'.join(tuple) + '\n')
        f.close()
        #print(tuples)
        handler = EventGraph(self.tmp_file, word)
        handler.show_graph("baike")

def show_graph():
    cur = '/'.join(os.path.realpath(__file__).split('/')[:-1])
    concept_file = os.path.join(cur, 'baike_concept.txt')
    handler = EventGraph(concept_file, 'baike_concept')
    handler.show_graph("baike")

if __name__ == '__main__':
    handler = SemanticBaike()
    handler.extract_main('苹果')

