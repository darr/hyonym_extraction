# HyponymyExtraction
HyponymyExtraction and Graph based on KB Schema, Baike-kb and online text extract,  
基于知识概念体系，百科知识库，以及在线搜索结构化方式的词语上下位抽取．  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# 项目介绍

上下位关系是语言学概念。
概括性较强的单词叫做特定性较强的单词的上位词（hypernym），特定性较强的单词叫做概括性较强的单词的下位词(hyponym)。比如我们说，苹果是一种水果，苹果就是水果的一个下位词，也可以称为一个实例，而水果则是苹果的一个上位词，也可以称为一个类．  
上下位这种语义关系是整个词汇语义关系中的一个重要内容，通过上下位关系，可以将世间万物进行组织和练联系起来，对于增进人们对某一实体或概念的认知上具有重要帮助  
自然语言文本中存储着大量的上下位关系知识，如经过语言专家编辑整理形成的概念语义词典，如同义词词林，中文主题概念词典，hownet等，也存在开放百科知识平台当中，有效地利用这些信息，能够支持多项应用，如：
1) 基于上下位关系的知识问答
2) 基于上下位关系的知识推荐
3) 基于上下位关系的文本理解

本项目主要解决第一个问题，本项目的应用场景是：用户输入一个需要了解的词语，后台通过查询既定知识库，从百百科知识库，在线非结构化文本中进行抽取，形成关于该词语的上下位词语网络，并以图谱这一清晰明了的方式展示出来．

# 本项目将采用三种方式来完成这一目标

1)基于既定知识库的直接查询，对应kb.py  
2)基于在线百科知识库的抽取，对应baike.py  
3)基于在线文本的结构化抽取，对应hyper_extract.py  

# 项目分解

# 1)基于既定知识库的直接查询
kb.py, 会生成相应的html文件,为最终展示结果  
# 结果展示　　

哆啦A梦  
![image](./img/kb_duolaameng.png)
平壤  
![image](./img/kb_pingrang.png)
孔子  
![image](./img/kb_kongzi.png)
小米  
![image](./img/kb_xiaomai.png)
苹果  
![image](./img/kb_pingguo.png)
中国  
![image](./img/kb_zhongguo.png)

# 2)基于在线百科的概念抽取
baike.py, 会生成相应的html文件,为最终展示结果  
# 结果展示

电话  
![image](./img/baike_dianhua.png)
孔子  
![image](./img/baike_kongzi.png)
平壤  
![image](./img/baike_pingrang.png)
杨幂  
![image](./img/baike_yangmi.png)
哆啦A梦  
![image](./img/baike_duolaameng.png)
老子  
![image](./img/baike_laozi.png)
小米  
![image](./img/baike_xiaomai.png)
姚明  
![image](./img/baike_yaoming.png)
黄河  
![image](./img/baike_huanghe.png)
苹果  
![image](./img/baike_pingguo.png)
小米  
![image](./img/baike_xiaomi.png)
中国  
![image](./img/baike_zhongguo.png)
