#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-09 13:14
# Modified date : 2019-08-10 21:58
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from kb import SemanticKB
from hyper_extract import HyponomyExtraction

from baike import SemanticBaike

def run_one_kb(word):
    handler = SemanticKB()
    handler.walk_concept_chain(word)

def kb_run():
    word = '孔子'
    run_one_kb(word)
    word = '苹果'
    run_one_kb(word)
    word = '中国'
    run_one_kb(word)
    word = '小麦'
    run_one_kb(word)
    word = '哆啦A梦'
    run_one_kb(word)
    word = '平壤'
    run_one_kb(word)

def run_hyper():
    content = '''油加醋，或者去涂脂抹粉“打造”它。历史是不需要加工的。无形的音乐是一种灵魂，而肺癌是癌症的一种'''
    handler = HyponomyExtraction()
    handler.process_candis2()

def baike_run():
    handler = SemanticBaike()
    word = '孔子'
    handler.extract_main(word)
    word = '苹果'
    handler.extract_main(word)
    word = '中国'
    handler.extract_main(word)
    word = '小麦'
    handler.extract_main(word)
    word = '哆啦A梦'
    handler.extract_main(word)
    word = '平壤'
    handler.extract_main(word)

def run():
    kb_run()
    #run_hyper()
    baike_run()

run()

