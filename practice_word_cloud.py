# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:21:48 2019

@author: imcna
"""

import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('winemag-data-130k-v2.csv', index_col = 0)

country = df.groupby('country')

plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=90)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")
plt.show()

text = df.description[0]

wordcloud = WordCloud(background_color = 'white').generate(text)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wordcloud.to_file("my_first_cloud.jpg")


#text = " ".join(review for review in df.description)
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# Using an Image to Create a Word Cloud
wine_mask = np.array(Image.open('wine.png'))
    
wc = WordCloud(background_color = "white", 
               max_words = 500, 
               mask = wine_mask,
               stopwords = stopwords)

# Generate a wordcloud
wc.generate(text)
# store to file
wc.to_file("test.jpg")

# show
plt.figure(figsize=[20,10])
plt.imshow(wc)
plt.axis("off")
plt.show()
    
# Making a word cloud match the colors of the image
usa = " ".join(review for review in df[df["country"]=="US"].description)

mask = np.array(Image.open('flag.jpg'))
wordcloud_usa = WordCloud(stopwords=stopwords, 
                          background_color="white", 
                          mode="RGBA", 
                          max_words=1000, 
                          mask=mask).generate(usa)

# create coloring from image
image_colors = ImageColorGenerator(mask)

#wordcloud_usa.to_file('usacloud.jpg')
plt.figure(figsize=[7,7])
plt.imshow(wordcloud_usa.recolor(color_func=image_colors), 
           interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png', format = 'png')
plt.show()