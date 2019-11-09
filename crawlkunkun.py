#爬取坤坤的微博评论
import requests
import xlwt
from bs4 import BeautifulSoup
import jieba
import wordcloud
headers={'user-agent':'','cookie':''}#输入你的user-agent和cookie
text_list=[]
for i in range(1,1000):
    url='https://weibo.cn/comment/hot/Ie61yrDwK?rl=1&page='+str(i)
    res=requests.get(url,headers=headers,timeout=10)
    soup=BeautifulSoup(res.text,'lxml')
    div_list=soup.find_all('span',class_='ctt')
    for item in div_list:
        text_list.append(item.text)

#写入text文件
fp=open('D:\\python学习\\坤坤评论区1.txt','w+',encoding='utf-8')
fp.write('\n'.join(text_list))
fp.close()

#用wordcloud词云统计
f=open('D:\\python学习\\坤坤评论区1.txt','r',encoding='utf-8')
l=f.read()
f.close()
ls=jieba.lcut(l)
counts={}
for item in ls:
    counts[item]=counts.get(item,0)+1
del counts["你"]
del counts["的"]
del counts[" "]
del counts["\n"]
del counts[","]
del counts["，"]
del counts["!"]
del counts["！"]
del counts["@"]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))

#画出词云
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white")
w.generate(" ".join(ls))