from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

#https://m.blog.naver.com/dh3508/221816555132를 참조하였습니다.

driver = webdriver.Chrome(r"C:/Users/82105/Desktop/chromedriver.exe")
driver.get("https://www.melon.com/chart/day/index.htm?classCd=AB0000")

#______곡명______
title=driver.find_elements_by_class_name('ellipsis.rank01')
titles=[]
for i in title:
    titles.append(i.text)
#print(titles)

#______가수명______
singer=driver.find_elements_by_class_name('ellipsis.rank02')
singers=[]
for i in singer:
    singers.append(i.text)
#print(singers)

#______가사______
numbers=[]
#_____TOP1~50
number50 = driver.find_elements_by_id('lst50')

for i in number50 :
    numbers.append(i.get_attribute('data-song-no'))

#_____TOP50~100
number100 = driver.find_elements_by_id('lst100')

for i in number100 :
    numbers.append(i.get_attribute('data-song-no'))

lyricsOriginal=[]
for i in numbers:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        lyric=driver.find_element_by_class_name("lyric")
        lyricsOriginal.append(lyric.text)
    except:
        lyricsOriginal.append("19")

lyrics=[]
for i in lyricsOriginal:
    lyrics.append(i.replace("\n"," "))

rv_list=[]      
for item in zip(titles, singers, lyrics): 
    rv_list.append( 
        [ 
            item[0], 
            item[1], 
            item[2], 
        ] 
    ) 

rv_infos = pd.DataFrame(rv_list, columns=['TITLE', 'SINGER', 'LYRIC']) 
rv_infos.to_csv('C:/Users/82105/Desktop/popTop100.csv', encoding='utf-8-sig') 
print("END")

driver.quit()
