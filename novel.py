# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

if __name__ == '__main__':
    target = "https://www.biquta.com/161_161474/"

    req = requests.get(url=target)
    soup = BeautifulSoup(req.text, "html.parser")
    list_tag = soup.div(id="list")
    print('list_tag:', list_tag)
    # 获取小说名称
    story_title = list_tag[0].dl.dt.string

    # 开始循环每一个章节，获取章节名称，与章节对应的网址
    for i in tqdm(range(8350208, 8353664)):
        chapter_url = target + str(i) + '.html'
        chapter_req = requests.get(url=chapter_url)
        chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")

        name = chapter_soup.text.split('\n\n\n\n')[1].split(',')[1]
        chapter_name = '第' + str(i - 8350207) + '章  ' + name.split()[-1]

        content_tag = chapter_soup.div.find(id="content")
        content_text = content_tag.text.replace('\u3000\u3000', '\n  ')
        content_text = str(content_text.replace('\xa0', '\n'))[:-18]
        with open(story_title + '.txt', 'a') as f:
            f.write(chapter_name + '\n\n')
            f.write('  ' + content_text.strip())
            f.write('\n\n\n')
