import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm
from wordcloud import WordCloud
import random

Text = ""
Names = ['Srikar', 'Vignesh', 'Ashish', 'Kotesh', 'Abhi', 'Saketh', 'Harsha', 'SubbaRao', 'Dhanumjai']

for i in range(180):
	Text = Text + random.choice(Names) + " "

wordcloud = WordCloud(colormap='gist_ncar', background_color='black').generate(Text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.savefig('Image.png')
plt.show()
