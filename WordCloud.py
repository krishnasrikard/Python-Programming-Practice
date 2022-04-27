import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm
from wordcloud import WordCloud
import random

Text = ""
Names = ["Lucifer", "Thomas Shebly", "James.T.Kirk", "James Herbert Bond", "Ethan Mathew Hunt", "Captain Jack Sparrow", "William Sherlock Scott Holmes", "Jon Snow"]

for i in range(180):
	Text = Text + random.choice(Names) + " "

wordcloud = WordCloud(colormap='jet', background_color='black').generate(Text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.savefig('Image.png')
plt.show()
