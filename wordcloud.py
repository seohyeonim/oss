from wordcloud import WordCloud
import pandas as pd 

df = pd.read_csv('C:/Users/82105/Desktop/popTop100.csv')

wordcloud=WordCloud(background_color = 'white',width=500,height=400).generate(''.join(df['LYRIC']))
wordcloud.to_file('C:/Users/82105/Desktop/MelonWord.png')
