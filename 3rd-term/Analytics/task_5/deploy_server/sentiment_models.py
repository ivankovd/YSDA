import pandas as pd
import numpy as np
import nltk
import pymorphy2

import pickle

class Vectorizer:
    def __init__(self, lang="russian"):
        self.stemmer = pymorphy2.MorphAnalyzer()
        self.tokenizer = nltk.tokenize.word_tokenize
        self.stopwords = nltk.corpus.stopwords.words(lang)
        
    def is_word(self, string):
        return string.isalpha()

    def text_preprocessing(self, text):
        tokenized_text = self.tokenizer(text.lower())
        filtered_text = list(
            filter(lambda word: self.is_word(word) and word not in self.stopwords, tokenized_text)
        )
        return " ".join(list(map(lambda word: self.stemmer.parse(word)[0].normal_form, filtered_text)))
    
    def set_tf_idf_vectorizer(self, tf_idf_vectorizer):
        self.tf_idf_vectorizer = tf_idf_vectorizer
    
    def vectorize(self, text):
        text_for_vectorize = self.text_preprocessing(text)
        return self.tf_idf_vectorizer.transform([text_for_vectorize])

class SentimentClassifier(object):
    def __init__(self):
        with open("./models/classifier.pkl", "rb") as f:   
            self.classifier = pickle.load(f)

        with open("./models/vectorizer.pkl", "rb") as f:   
            self.tfidf_vectorizer = pickle.load(f)
        
        self.vectorizer = Vectorizer()
        self.vectorizer.set_tf_idf_vectorizer(self.tfidf_vectorizer)
        
        self.color_palette = {
            5: "#00FF00",
            4: "#00FF00",
            3: "#FFFF00",
            2: "#FF8000",
            1: "#FF0000"
        }

    def run(self, text):
#         try:
        vectorized_text = self.vectorizer.vectorize(text)
        pred_score = self.classifier.predict(vectorized_text)[0]
        return str(pred_score), self.color_palette[pred_score]
        
#         except:
#             return "-1", "#000000"
        