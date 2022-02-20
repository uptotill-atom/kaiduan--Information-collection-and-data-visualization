# 爬取评论内容的代码

import requests
import random
import re

def get_html(url,params):
    thisua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    headers = {"User-Agent":thisua}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    r.encoding='utf-8'

    return r.text


def parse_page(infolist,data):
    commentpat = '"content":"(.*?)"'
    lastpat = '"last":"(.*?)"'
    commentall = re.compile(commentpat,re.S).findall(data)
    next_cid = re.compile(lastpat).findall(data)[0]
    infolist.append(commentall)

    return next_cid



def print_comment_list(infolist):
    j = 0
    for page in infolist:
        print('第' + str(j+1) + '页\n')
        commentall = page
        for i in range(0,len(commentall)):
            print(commentall[i] + '\n')
        j += 1

def save_to_txt(infolist,path):
    fw = open(path, 'w+', encoding='utf-8')
    j = 0
    for page in infolist:

        commentall = page
        for i in range(0, len(commentall)):
            fw.write(commentall[i] + '\n')
        j += 1
    fw.close()

def main():
    infolist = []
    vid = '7625787154' ;
    cid = "0";
    page_num = 1000
    url = 'https://video.coral.qq.com/varticle/'+ vid +'/comment/v2'

    for i in range(page_num):
        params = {'orinum': '10', 'cursor': cid}
        html = get_html(url, params)
        cid = parse_page(infolist, html)

    print_comment_list(infolist)
    save_to_txt(infolist,'content.txt')

if __name__ == '__main__':
    main()