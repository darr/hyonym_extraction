#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : etc.py
# Create date : 2019-08-09 15:49
# Modified date : 2019-08-09 15:50
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

HTML_STR = '''
    <html>
    <head>
      <script type="text/javascript" src="VIS/dist/vis.js"></script>
      <link href="VIS/dist/vis.css" rel="stylesheet" type="text/css">
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>

    <div id="VIS_draw"></div>
    <script type="text/javascript">
      var nodes = data_nodes;
      var edges = data_edges;

      var container = document.getElementById("VIS_draw");

      var data = {
        nodes: nodes,
        edges: edges
      };

      var options = {
          nodes: {
              shape: 'dot',
              size: 25,
              font: {
                  size: 14
              }
          },
          edges: {
              font: {
                  size: 14,
                  align: 'left'
              },
              color: 'red',
              arrows: {
                  to: {enabled: true, scaleFactor: 0.5}
              },
              smooth: {enabled: true}
          },
          physics: {
              enabled: true
          }
      };

      var network = new vis.Network(container, data, options);

    </script>
    </body>
    </html>
'''
