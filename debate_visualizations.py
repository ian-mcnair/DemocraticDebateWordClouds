# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:06:30 2019

@author: imcna
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('candidates.xlsx')

pos = range(len(df.candidates))

test = df.sort_values('length', ascending = False)

sns.set_context('talk')
sns.set_style("darkgrid")
sns.barplot(x = test.length,
            y = test.candidates)
plt.title('Candidate Speech Length')
plt.xlabel('Number of Words')
plt.ylabel('Candidate')
plt.show()