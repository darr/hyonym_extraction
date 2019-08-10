#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : page.py
# Create date : 2019-08-09 15:45
# Modified date : 2019-08-10 22:03
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from etc import HTML_STR

'''构造显示图谱'''
class CreatePage:
    def __init__(self, html_name):
        self.html_name = html_name
        self.base = HTML_STR

    def collect_data(self, nodes, edges):
        '''生成数据'''
        node_dict = {node: index for index, node in enumerate(nodes)}
        data_nodes = []
        data_edges = []
        for node, id in node_dict.items():
            data = {}
            data["group"] = 'Event'
            data["id"] = id
            data["label"] = node
            data_nodes.append(data)

        for edge in edges:
            data = {}
            data['from'] = node_dict.get(edge[0])
            data['label'] = 'is-a'
            data['to'] = node_dict.get(edge[1])
            data_edges.append(data)
        return data_nodes, data_edges

    def create_html(self, data_nodes, data_edges):
        '''生成html文件'''
        f = open(self.html_name, 'w+')
        html = self.base.replace('data_nodes', str(data_nodes)).replace('data_edges', str(data_edges))
        f.write(html)
        f.close()

