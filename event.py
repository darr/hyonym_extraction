#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : event.py
# Create date : 2019-08-10 13:16
# Modified date : 2019-08-10 22:02
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from page import CreatePage

'''图谱展示'''
class EventGraph:
    def __init__(self, relfile, html_name):
        relfile = relfile
        self.html_name = html_name
        self.event_dict, self.node_dict = self.collect_events(relfile)

    def collect_events(self, relfile):
        '''统计事件频次'''
        event_dict = {}
        node_dict = {}
        for line in open(relfile):
            event = line.strip()
            #print(event)
            if not event:
                continue
            nodes = event.split('->')
            for node in nodes:
                if node not in node_dict:
                    node_dict[node] = 1
                else:
                    node_dict[node] += 1

            if event not in event_dict:
                event_dict[event] = 1
            else:
                event_dict[event] += 1

        return event_dict, node_dict

    def filter_events(self, event_dict, node_dict):
        '''过滤低频事件,构建事件图谱'''
        edges = []
        nodes = []
        for event in sorted(event_dict.items(), key=lambda asd: asd[1], reverse=True)[:2000]:
            e1 = event[0].split('->')[0]
            e2 = event[0].split('->')[1]
            if e1 in node_dict and e2 in node_dict:
                nodes.append(e1)
                nodes.append(e2)
                edges.append([e1, e2])
            else:
                continue
        return edges, nodes

    def show_graph(self,tp):
        '''调用VIS插件,进行事件图谱展示'''
        edges, nodes = self.filter_events(self.event_dict, self.node_dict)
        html_full_path = './results/%s_%s.html' % (tp, self.html_name)
        handler = CreatePage(html_full_path)
        data_nodes, data_edges = handler.collect_data(nodes, edges)
        handler.create_html(data_nodes, data_edges)

