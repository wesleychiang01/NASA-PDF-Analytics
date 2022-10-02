import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
from nltk.draw.dispersion import dispersion_plot
from nltk.probability import ConditionalFreqDist
from nltk.probability import FreqDist
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from yellowbrick.text import TSNEVisualizer


class Statistics:
    # 1.Word Cloud
    def wordcloud(self, text_parsed):
        self.text = text_parsed
        self.allwords = text_parsed.split()
        wordcloud = WordCloud(width=1000, height=450, background_color='white', max_font_size=60).generate(text_parsed)

        plt.figure(figsize=(45, 15))
        # plot wordcloud in matplotlib
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Keywords Wordcloud from PDF", size=55)
        # plt.show()
        plt.savefig('wordcloud.png')
        self.df = pd.DataFrame(self.allwords)
        self.frequency()

    # Term Frequency
    def term(self):

        tfidf = TfidfVectorizer()
        text_data = np.array(self.allwords)

        feature_matrix = tfidf.fit_transform(text_data)
        feature_matrix.toarray()

        # Show tf-idf feature matrix
        tfidf.get_feature_names_out()

        topics = ['aeronautics', 'astronautics', 'chemistry and materials', 'engineering', 'geosciences',
                  'life sciences', 'math and computer sciences', 'physics', 'social and info science', 'space sciences', 'general']
        dispersion_plot(self.allwords, topics)
        self.df = pd.DataFrame(self.allwords)

    # Frequency Distribution
    def frequency(self):
        freqdist = nltk.FreqDist(self.allwords)
        plt.figure(figsize=(16, 5))
        freqdist.plot(50)

        # Most Frequent 10 words in all Text

        freqdist.most_common(10)

        ## Draw a bar chart with the count of the most common 10 words
        x, y = zip(*freqdist.most_common(n=10))
        plt.figure(figsize=(16, 5))
        plt.bar(range(len(x)), y, color='Orange', tick_label=y)
        plt.xticks(range(len(x)), x)
        plt.title('Frequency Count of Top 10 Words', size=20)
        plt.xlabel('Frequent Words')
        plt.ylabel('Count')
        plt.rcParams.update({'font.size': 20})
        # plt.show()
        plt.savefig('Most Frequent 10 words.jpeg')

        # Get Bigrams from text
        bigrams = nltk.bigrams(self.allwords)
        # Calculate Frequency Distribution for Bigrams
        freq_bi = nltk.FreqDist(bigrams)

        # Draw a bar chart with the count of the most common 10 words
        x, y = zip(*freq_bi.most_common(n=15))
        plt.figure(figsize=(18, 12))
        plt.barh(range(len(x)), y, color='Maroon')
        y_pos = np.arange(len(x))
        plt.yticks(y_pos, x)
        plt.title('Frequency Count of Top 15 Bi-Grams', size=40)
        plt.ylabel('Frequent Words')
        plt.xlabel('Count', fontsize=14)
        plt.tight_layout()
        plt.savefig('Most Frequent 15 Bi-Grams.jpeg')

        self.trigram()

    def trigram(self):

        # Get Trigrams from text
        trigrams = nltk.trigrams(self.allwords)
        # Calculate Frequency Distribution for Bigrams
        freq_tri = nltk.FreqDist(trigrams)

        # Print and plot most common bigrams
        freq_tri.most_common(10)

        # Draw a bar chart with the count of the most common 50 words
        x, y = zip(*freq_tri.most_common(n=15))
        plt.figure(figsize=(18, 12))
        plt.barh(range(len(x)), y, color='Darkblue')
        # plt.barh(x,range(len(x)), color = 'Orange', tick_label = y)
        # plt.xticks(range(len(x)), x)
        y_pos = np.arange(len(x))
        plt.yticks(y_pos, x)
        plt.title('Frequency Count of Top 15 Tri-Grams',  size=40)
        plt.ylabel('Frequent Words')
        plt.xlabel('Count')
        plt.tight_layout()
        # plt.show()
        plt.savefig('Most Frequent 15 Tri-Grams.jpeg')

    def word_distribution(self):
        cfdist = ConditionalFreqDist((len(word), word) for word in self.allwords)
        cfdist.plot()

        tfidf = TfidfVectorizer()

        docs = tfidf.fit_transform(self.allwords)

        # Create the visualizer and draw the vectors
        tsne = TSNEVisualizer()
        tsne.fit(docs)
        tsne.poof()

        # tokenizer to remove unwanted elements from out data like symbols and numbers
        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        cv = CountVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)

        text_counts = cv.fit_transform(self.df[0])
