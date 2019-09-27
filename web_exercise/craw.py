# bs4库是python中的第三方库，需要pip install bs4
from bs4 import BeautifulSoup
import random, os, django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_exercise.settings")
django.setup()
# 存储目标url
url_list = []
poto_list = []
title_list = []
p_list = []
from apps.exercise.models import Actions

for i in range(1, 9):
    # url入口
    url = f"https://www.jirou.com/lian/jb/list_179_{i}.html"
    # 伪装浏览器访问
    user_list = [
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        # 搜狗浏览器
        'Mozilla / 4.0(compatible;MSIE7.0;WindowsNT5.1;Trident / 4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
        # 360浏览器
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE))'
        # Chrome浏览器
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    ]

    user_agent = random.choice(user_list)
    # 头部信息
    headers = {'User-Agent': user_agent}

    # 构造请求
    response = requests.get(url, headers=headers).content
    # response.encoding = 'utf-8'

    # html.parser是python自带的一个文件解析库
    soup = BeautifulSoup(response, "html.parser")
    # 定位
    root_url = soup.select(".article-wrap .article-list a")
    for item in root_url:
        # print(item)
        # print(type(item))===> <class 'bs4.element.Tag'>

        # lxml是一个文件解析库，通过它的解析生成对象，是一个第三方库，需要安装
        soup_one = BeautifulSoup(str(item), "lxml")
        # poto为图片的链接
        poto = f"https:{soup_one.select('.article-list-pic')[0]['src']}"
        # poto_list.append(poto)

        # title为文章标题
        title = soup_one.select('.article-list-detaile h2')[0].get_text()
        # title_list.append(title)

        # 概要信息
        p = soup_one.select('.article-list-detaile p')[0].get_text()
        # p_list.append(p)
        # print(poto)

        # new_url为文章的链接
        new_url = f"https:{item['href']}"
        # print(f"https:{item['href']}")
        # url_list.append(new_url)

        Actions.objects.create(title=title, outline=p, pic=poto, content=new_url)

# 保存文章链接url
# print(url_list)

# 保存图片链接url.
# print(poto_list)

# 保存title文字
# print(title_list)

# 保存p标签的概要信息
# print(p_list)
