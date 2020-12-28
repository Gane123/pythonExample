import re
from bs4 import BeautifulSoup
import pandas as pd
import requests


# header模拟浏览器访问
header={
    'Host': 'www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.bilibili.com/',
    'Connection': 'keep-alive',
    'Cookie': '_uuid=F8EE5482-2CE1-3426-0C4C-52ABF60EEF6896527infoc; buvid3=FD3F5860-5D46-461A-B7DC-313A2F98C59A58475infoc; finger=-863946392',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
    }
# 要爬取的网站链接（哔哩哔哩动画排行榜）
url ="https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.39"
# 解析url
response=requests.get(url,headers=header).text
soup = BeautifulSoup(response, features='html.parser')
# 找出标签<div class="info">里面的内容，也就是需要爬取的内容，但是还包含其他的内容
all_content=soup.find_all('div',{'class':"info"})
# 通过正则爬取每个动画的综合得分
score=re.findall(r"<div>(.+?)</div>综合得分", str(all_content))
all_hrefs=[]
all_titles=[]
# 因为爬取的内容为列表形式，因此需要循环遍历，爬取出链接和题目
for one_content in all_content:
    # 获取标签<a class="title">里面的内容,这次就是要的题目与链接
    ones=one_content.find_all('a',{"class":'title'})
    # 循环遍历
    for one in ones:
        # 链接
        one_href=one['href']
        one_href=one_href.replace('//', '')
        # 题目
        one_title=re.findall(r">(.+?)</a>", str(one))
        # 将题目与链接分别添加到两个列表中
        all_hrefs.append(one_href)
        all_titles.append(one_title[0])
# 将三个列表放到字典中
dict={'title（动画名称）':all_titles,'href(动画链接)':all_hrefs,'score(综合得分)':score}
# 转换成DataFrame格式
df=pd.DataFrame(dict)
# 索引从1开始
df.index=df.index+1
# 存放到excel中
df.to_excel('E:/output/bilibili_动画.xlsx')

