import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import nltk
from nltk.corpus import stopwords as sw
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

nltk.download('stopwords')

df = pd.read_excel('candidates.xlsx')
df['speech_upper'] = df.speech.str.upper()

sns.set_context('poster')
mask = np.array(Image.open('flag.jpg'))

for i in range(len(df.candidates)):
    """
    This loop grabs the speech and cndidate name.
    Then it creates a word cloud and saves it.
    Unfortunately, I haven't figured out how to not display the images
    ,but it at least works...
    """
    speech = df.speech_upper[i]
    name = df.candidates[i]
        
    wordcloud = WordCloud(stopwords=sw.words('english'), 
                              background_color="white", 
                              mode="RGBA", 
                              max_words=1000, 
                              mask=mask).generate(speech)
    
    # create coloring from image
    image_colors = ImageColorGenerator(mask)
    
    plt.figure(figsize=[15,10])
    plt.imshow(wordcloud.recolor(color_func=image_colors), 
               interpolation="bilinear")
    plt.axis("off")
    plt.title(name)
    plt.savefig(name +'.png', format = 'png')
















