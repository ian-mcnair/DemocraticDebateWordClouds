# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:27:03 2019

@author: imcna
"""
# Scrapping the HTML 
from requests import get
url1 = 'https://time.com/5615358/2020-first-democratic-debate-transcript/'
url2 = 'https://time.com/5616518/2020-democratic-debate-night-2-transcript/'
response1 = get(url1)
response2 = get((url2))

# Parse HTML
from bs4 import BeautifulSoup
html1 = BeautifulSoup(response1.text, 'html.parser')
html2 = BeautifulSoup(response2.text, 'html.parser')

# Get just the pieces of text spoken by
transcript1 = []
transcript2 = []
for p in html1.select('p'):
    transcript1.append(p.text)

for p in html2.select('p'):
    transcript2.append(p.text)

transcript1[0:5]

transcript2[0:5]


# List of all candidates. Needed to do this manually
candidates1 = ['Booker', 'Castro', 'De Blasio', 
              'Delaney', 'Gabbard', 'Inslee', 
              'Klobuchar', "O’Rourke", "Ryan", 
              "Warren", 'Holt', 'Guthrie', 'Announcer',
              'DIAZ-BALART', 'Todd', 'Maddow']

candidates2 = ['Biden', 'Sanders', 'Harris', 'Buttigieg',
               'Yang', 'Gillibrand', 'Williamson',
               'Hickenlooper', 'Bennet',
               'Swalwell','Holt', 'Guthrie',
               'DIAZ-BALART', 'Todd', 'Maddow']

# Capitalize the Candidates
for i in range(len(candidates1)):
    candidates1[i] = candidates1[i].upper()
for i in range(len(candidates2)):
    candidates2[i] = candidates2[i].upper()
    
# Make a dictionary for storing what each candidate said
candidate_words1 = {}
for i in candidates1:
    candidate_words1[i] = ''
candidate_words2 = {}
for i in candidates2:
    candidate_words2[i] = ''
   

# This loop goes through each line of the transcript
for i in range(len(transcript1)):
    flag = False
    current = ''
    # This one loops through candidates
    # triggers a flag for later
    for j in range(len(candidates1)):
        if candidates1[j] in transcript1[i]:
            current = candidates1[j]
            flag = True
            break
    if flag:
        candidate_words1[current] += transcript1[i]

for i in range(len(transcript2)):
    flag = False
    current = ''
    # This one loops through candidates
    # triggers a flag for later
    for j in range(len(candidates2)):
        if candidates2[j] in transcript2[i]:
            current = candidates2[j]
            flag = True
            break
    if flag:
        candidate_words2[current] += transcript2[i]
        
        
for i in candidate_words1:
    candidate_words1[i] = candidate_words1[i].replace(i + ':', '')
for i in candidate_words2:
    candidate_words2[i] = candidate_words2[i].replace(i + ':', '')
    
cand_vals1 = {}
for i in candidate_words1:
    cand_vals1[i] = len(candidate_words1[i])
cand_vals2 = {}
for i in candidate_words2:
    cand_vals2[i] = len(candidate_words2[i])


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df1 = pd.DataFrame(list(zip(list(cand_vals1.keys()),
                           list(cand_vals1.values()),
                           list(candidate_words1.values()))),
                columns = ['candidates', 'length', 'speech']
                )
df2 = pd.DataFrame(list(zip(list(cand_vals2.keys()),
                           list(cand_vals2.values()),
                           list(candidate_words2.values()))),
                columns = ['candidates', 'length', 'speech']
                )

#########################
# Fix this part!
df = df1.append(df2)

df =
#########################

df.to_excel('candidates1.xlsx', index = False)

pos = range(len(df.candidates))

test = df.sort_values('length', ascending = False)

sns.set_style("darkgrid")
sns.barplot(x = test.length,
            y = test.candidates)
plt.title('Candidate Speech Length')
plt.xlabel('Number of Words')
plt.ylabel('Candidate')
plt.show()








# After Removing the stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')
print(stopwords.words()[620:680])





