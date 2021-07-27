
import requests as rq
import matplotlib.pyplot as plt
from collections import Counter as cnt
from wordcloud import WordCloud as wc
from konlpy.tag import Okt as klp
from bs4 import BeautifulSoup as bs


url='https://gall.dcinside.com/board/lists'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}

result = ''

for i in range(1,101):
    params = {'id': 'lgtwins_new', 'page': i}
    source=rq.get(url, params=params, headers=headers)
    soup=bs(source.content, 'html.parser')
    content=soup.select('.gall_tit')
    for content in content:
        title = content.select_one('a').text + ' '
        result += title
        
klp = klp()
nouns = klp.nouns(result)
words=[]
stopwords = ['오늘', '새끼', '시발', '씨발', '이제', '누구', '누가', '존나', '졸라', '진짜', '그대로', '병신', '보고', '정도', '지금', '내일', '어제', '지랄', '우리', '제일', '그냥', '하나', '생각', '이유', '사람']
for n in nouns:
    if len(n) > 1 and n not in stopwords:
        words.append(n)

cntWord = cnt(words).most_common(50)

tags = {}
for n, c in cntWord:
    tags[n] = c
    
wcResult = wc(font_path="./NanumSquareRoundR.ttf", max_font_size=768 ,width=3840, height=2160).generate_from_frequencies(tags)
plt.imshow(wcResult, interpolation='bilinear')
plt.axis('off')
plt.savefig('wcResult.png')