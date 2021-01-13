import requests
import pandas as pd

def getUrl(url):
    #请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
       }
    #解析url
    html = requests.get(url, headers=header).json()
    #返回json数据
    return html
def getData(html):
    #从json中取出需要的数据
    data = html['data']['list']
    # 转成DataFrame格式
    datadf = pd.DataFrame(data)
    #从data取出想要的字段以及对应数据
    weeklydf = datadf[['title', 'pic', "bvid", 'desc', 'dynamic', 'rcmd_reason']]
    # 拼接动画链接
    weeklydf['bvid'] = 'https://www.bilibili.com/video/' + weeklydf['bvid']
    return weeklydf
if __name__ == '__main__':
    for i in range(1,95):
        url='https://api.bilibili.com/x/web-interface/popular/series/one?number={}'.format(i)
        html=getUrl(url)
        weeklydf=getData(html)
        # 索引从1开始
        weeklydf.index=weeklydf.index+1
        weeklydf.to_excel('E:/output/bilibili/每周必看第'+str(i)+'期.xlsx')


# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
#    }
# for i in range(1,95):
#     url='https://api.bilibili.com/x/web-interface/popular/series/one?number={}'.format(i)
#     #解析url
#     html=requests.get(url,headers=header).json()
#     print(html)
#     data=html['data']['list']
#     all_titles=[]
#     all_pics=[]
#     # print(data)
#     df=pd.DataFrame(data)
#     df1=df[['title','pic',"bvid", 'desc', 'dynamic', 'rcmd_reason']]
#     df1['bvid'] = 'https://www.bilibili.com/video/' + df1['bvid']
#     # 索引从1开始
#     df1.index=df1.index+1
#     df1.to_excel('E:/output/bilibili/第'+str(i)+'期.xlsx')