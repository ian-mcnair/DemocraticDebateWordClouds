# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:22:43 2019

@author: imcna
"""
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")
#
df = pd.read_excel('candidates1.xlsx')
df['speech_upper'] = df.speech.str.upper()

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords as sw
sw.words('english')


speech = df.speech_upper[10]

mask = np.array(Image.open('flag.jpg'))

wordcloud = WordCloud(stopwords=sw.words('english'), 
                          background_color="white", 
                          mode="RGBA", 
                          max_words=2000, 
                          mask=mask).generate(speech)

# create coloring from image
image_colors = ImageColorGenerator(mask)

#wordcloud_usa.to_file('usacloud.jpg')
plt.figure(figsize=[20,10])
plt.imshow(wordcloud.recolor(color_func=image_colors), 
           interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png', format = 'png')
plt.show()