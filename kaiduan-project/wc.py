# 制作词云
# 导入相应的库
import numpy as np
import re
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image

f = open('content.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

newtxt = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", txt)
#print(newtxt)
words = jieba.lcut(newtxt)
#print(words)

img = Image.open(r'tupian.jpg')
img_array = np.array(img)
#print(img_array)

wordcloud = WordCloud(
    background_color="white",
    width=1080,
    height=960,
    font_path='C:\Windows\Fonts\STKAITI.TTF',
    max_words=150,
    scale=10,#清晰度
    max_font_size=100,
    mask=img_array,
    collocations=False).generate(newtxt)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('wc.png')