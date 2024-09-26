## Generic text file distribution
## https://dariuslfuller.medium.com/creating-visuals-with-nltks-freqdist-ac4e667e49f3

import seaborn
from matplotlib import pyplot as plt
import pandas as pd
from nltk import FreqDist
from nltk.tokenize import word_tokenize
#nltk.download('stopwords')

## Uncomment these if missing packages are throwing errors
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

## Open file from user
print("Input file path: ")
localPath = input()
paper = open(localPath, "r", encoding="utf8")
raw = paper.read()

#stop_words = set(stopwords.words('english'))
punctuation = [".", ",", "'", ":", ";", "?", "!", "(", ")", "{", "}", "[", "]", "’", "''", "``"] 
tokens = word_tokenize(raw)

#notStopWords = []
notPunctuation = []

for word in tokens:
    #if word not in stop_words:
     #   notStopWords.append(word)
    if word not in punctuation:
        notPunctuation.append(word)

fdist = FreqDist(notPunctuation)
print(fdist)
print("Input number of words to display: ")
topWords = input()

try:
    topWords = int(topWords)
except ValueError:
    topWords = -1

if (topWords > 0):
    common = fdist.most_common(topWords)
    for word in common:
        print(word)
else:
    common = fdist.most_common()
    for word in common:
        print(word)
        
## Convert to Pandas series via Python dictionary
all_dist = pd.Series(dict(common))

## Set figure, variables
fig, ax = plt.subplots(figsize=(10,10))

## Seaborn plotting
plot = seaborn.barplot(x=all_dist.index, y=all_dist.values, ax=ax)
# plt.xticks(rotation=30);

paper.close()