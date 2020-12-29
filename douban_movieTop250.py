from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

#获取豆瓣Top250页面
def get_Url(url):
    header={
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 84.0)Gecko/20100101Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml, application/xml;q = 0.9,image/webp, */*;q = 0.8',
        'Accept-Language':'zh-CN,zh;q = 0.8, zh-TW;q = 0.7, zh-HK;q = 0.5, en-US;q = 0.3, en;q = 0.2',
        'Referer': "https://movie.douban.com/top250",
        'Connection': 'keep-alive',
        'Cookie': 'bid = DN_L_dUYnQQ'
    }
    #解析url
    html=requests.get(url,headers=header).text
    return html

#获取爬取页面中所需数据
def get_Data(html,all_title,all_score):
    soup = BeautifulSoup(html, features="html.parser")
    # 电影评分
    scores = soup.find_all('div', {"class": "info"})
    # 电影名
    titles = soup.find_all('span', {"class": "title"})
    # 遍历所有电影名，将所有电影名字放到all_title列表中
    for j in range(len(titles)):
        title = re.findall(r'"title">(.+?)</span>', str(titles[j]))
        if "/" not in title[0]:
            all_title.append(title[0])
    # # 遍历所有评分信息，将所有电影对应的评分放到all_score列表中
    for j in scores:
        all_score.append(re.findall(r'"v:average">(.+?)</span>', str(j))[0])

    return all_title,all_score
if __name__ == '__main__':
    all_title = []
    all_score=[]
    #遍历10页数据，每页25条
    for i in range(10):
        url="https://movie.douban.com/top250?start={}&filter=".format(i*25)
        html=get_Url(url)
        all_titles,all_scores=get_Data(html,all_title,all_score)
    # 放到字典中
    dict = {'title（电影名字）': all_titles, 'score(评分)': all_scores}
    # print(dict)
    # 转换成DataFrame格式
    df=pd.DataFrame(dict)
    # 索引从1开始
    df.index=df.index+1
    # 存放到excel中
    df.to_excel('E:/output/豆瓣电影排行.xlsx')


