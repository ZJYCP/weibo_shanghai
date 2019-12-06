---
title: 我研究了一下上海凌晨不睡觉的人们
date: 2019-12-06 18:45:07
tags: 
    - 爬虫
categories: 
    - 爬虫
---
最近牙疼，疼到睡不着的那种。每晚总得深夜起来，喝上几口凉水，摸黑找出一片甲硝唑含上，到阳台站上一会儿，继续感受着隐隐阵痛。

夜已深。整个城市有一种褪色的沉淀感，周围很安静，听不见白日里的嘈杂声。这地界也算得上是在上海市区吧，附近的高层住宅楼依稀闪着几点亮光，然而在光污染的影响下，它们在橘黄色的天空背景下并不起眼。我知道，那是还没有入睡的人们。

我有点好奇，那些灯火下映射的人，他们是谁，他们又在做什么？我决意去了解一下

于是，我开始写代码QAQ

方法也比较干脆，通过分析微博同城的信息，看看大家的动态。俗话说<*爬虫写得好，牢饭吃到饱*>，这次写的爬虫简单至极，没有并发请求，没有用代理，甚至连请求头都是一成不变。

几天下来，我获取了超过100万条上海本地的微博数据，去重并筛选出在凌晨发的之后数据里少了很多(如无特殊说明，本文凌晨均指0点-5点)，**因为这些都是公开数据，这边放上来应该也无碍**。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/database)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/origindata)

首先看一下性别，女性竟然是男性的三倍，是不是说女性更容易熬夜。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/gender.png)

当然，其实这很大程度上是由于微博上女性用户数量多于男性的缘故。通过计算各性别用户在凌晨发博数据在全天的占比，发现，女性的比值为**9.3%**,男性为**8.7%**，相差并不大。所以说，不管是男性还是女性，都有不睡觉的理由。

我们再看下发博时间的统计，很明显，凌晨0点到1点的人数最多，可能那时对年轻人来说时候还早，夜生活才刚刚开始。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/hour.png)

随着夜色入深，大部分人还是会向睡眠妥协，但终究还是有修仙党战胜了睡眠，凌晨4点发博的人仍占到了5%。5点时段的人数比4点略有回升，环比增长8个百分点，估计是有人已经起早干活了吧。

当然，相比以上这些，我更关心他们在凌晨时段究竟在做什么，于是采用了基于 TF-IDF 算法的关键词抽取，对每条微博提取出10个关键词，绘制出词云(看↓，福尔摩斯)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/word22.png)

几个权重比较大的词（自己、上海、开心....)  <**自己**>的词频远超其他。或许在上海这个快节奏的都市中，唯有深夜，才有段时间是留给自己的吧。

从词云来看，大家的都表现得蛮积极的。不过我还是决定再深挖一下。这里通过paddlepaddle进行深度学习，使用百度的ERNIE+BI-LSTM模型，在ChnSentiCorp数据集上fine-tune后对微博数据进行情感倾向分析。(PS.感谢百度AI平台提供的16GB显存的Tesla V100算力卡)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/sen.png)

可以看出，有超过70%的状态都是积极的，看来大家都是想起高兴的事情，才睡不着呀。于是，我便看了看究竟是什么高兴的事。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/o1.png)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/o3.png)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/o2.png)

我觉得可还行。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/smile2.jpg)

不过，也有人喜欢在深夜的时候吐露负面情绪，或许夜深人静更清醒，于是更绝望

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/n1)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/n3)

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/n2)

绝望向左，希望向右！希望大家都能好好的！

综合地看了下，表现为消极的微博比重较多的为**情感问题**，而情感倾向为积极的微博<**吃**>相关的记录所占的也是相当多。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/eat)

***喝酒吃串串，快活似神仙***

在深夜里，人们不睡觉时最惦记着谁呢，家人，朋友，还是对象？ 这些在深夜时分的碎碎念，可能代表了人们情感中最温暖和柔软的部分：

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/mom)

最后统计了把用户信息，绝大部分都是和你我一样的普通人，也不乏有个别大V在其中。

![image](https://blog-1252832257.cos.ap-shanghai.myqcloud.com/emx6_blog/data)

*我不太想写太多诸如在大城市的人，人生艰难，生活无奈的话，毕竟在这些不睡觉的人里，有许多都是因为有开心的事情，或者对第二天的期待而无法入睡的。*

*当然也会有不开心的时候，有辗转反侧，有难以入眠，有浓烈的孤独，有不甘和委屈在被窝里留下的泪，有睁着眼睛到天亮，这些，一直会有，也永远会有，但天亮的时候，我们又迎来了新的一天。*

最后，记住一点，年轻人，少熬夜，以及 保护好牙齿。

* * *

> tips：
> 本文受<我研究了一下上海凌晨不睡觉的人们>启发
> 关于程序，为了~~不暴露自己拙劣的编程水平~~保护部分隐私信息，这里暂不贴出来了。后续可能会写篇文章记录下，大概率会咕。
> 涉及技术栈及开源框架：scrapy爬虫框架、手机网络请求抓包、jieba分词、paddlepaddle深度学习框架、wordcloud词云、阿里DataV数据可视化平台、亚马逊QuickSight BI系统。

