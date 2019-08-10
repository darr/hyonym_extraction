#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : kb.py
# Create date : 2019-08-09 12:30
# Modified date : 2019-08-10 21:17
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os

from page import CreatePage
from event import EventGraph

class SemanticKB:
    def __init__(self):
        cur = '/'.join(os.path.realpath(__file__).split('/')[:-1])
        concept_file = os.path.join(cur, './kb_data/baike_concept.txt')
        self.tmp_file = os.path.join(cur, './kb_data/word_concept.txt')
        self.path = []
        self.concept_dict, self.down_concept_dict = self.collect_baikeconcept(concept_file)

    def collect_baikeconcept(self, concept_file):
        '''加载百科上下位概念'''
        concept_dict = {}
        down_concept_dict = {}
        for line in open(concept_file):
            line = line.strip().split('->')
            if not line:
                continue
            instance = line[0]
            category = line[1]
            if instance not in concept_dict:
                concept_dict[instance] = [category]
            else:
                concept_dict[instance].append(category)

            if category not in down_concept_dict:
                down_concept_dict[category] = [instance]
            else:
                down_concept_dict[category].append(instance)

        return concept_dict, down_concept_dict

    def walk_up_hyper(self, word):
        '''基于百科上下位词典进行遍历查询'''
        f = open(self.tmp_file, 'w+')
        hyper_words = self.concept_dict.get(word, '')
        if not hyper_words:
            return

        for hyper in hyper_words:
            depth = 0
            self.path.append('->'.join([word, hyper]))
            self.back_hyper_up(hyper, depth)

    def back_hyper_up(self, word, depth):
        '''基于既定知识库的深度遍历'''
        depth += 1
        if depth > 5:
            return
        if not word:
            return
        hyper_words = self.concept_dict.get(word, '')
        if not hyper_words:
            return []
        for hyper in hyper_words:
            self.path.append('->'.join([word, hyper]))
            for hyper_ in hyper_words:
                if hyper == 'root':
                    return
                self.back_hyper_up(hyper_, depth)

    def walk_down_hyper(self, word):
        '''基于百科上下位词典进行遍历查询'''
        hyper_words = self.down_concept_dict.get(word, '')
        if not hyper_words:
            return
        for hyper in hyper_words:
            depth = 0
            self.path.append('->'.join([word, hyper]))
            self.back_hyper_down(hyper, depth)

    def back_hyper_down(self, word, depth):
        '''基于既定知识库的深度遍历'''
        depth += 1
        if depth > 1:
            return
        if not word:
            return
        hyper_words = self.down_concept_dict.get(word, '')
        if not hyper_words:
            return []
        for hyper in hyper_words:
            self.path.append('->'.join([hyper, word]))
            for hyper_ in hyper_words:
                if word == 'root':
                    return
                self.back_hyper_down(hyper_, depth)

    def walk_concept_chain(self, word):
        '''获取上位和下位'''
        print("knowlage base:%s" % word)
        f = open(self.tmp_file, 'w+')
        # 对其进行上位查找
        self.walk_up_hyper(word)
        #　对其进行下位查找
        # self.walk_down_hyper(word)
        for i in set(self.path):
            f.write(i + '\n')
        f.close()

        handler = EventGraph(self.tmp_file, word)
        handler.show_graph("kb")

#   word = '孔子'
#   handler = SemanticKB()
#   handler.walk_concept_chain(word)
