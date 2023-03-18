import gensim
from gensim import corpora, models, similarities
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from collections import defaultdict

# Load the Q&A data
data = [
    {'question': 'What is data science?', 'answer': 'Data science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.'},
    {'question': 'What are the key skills for a data scientist?', 'answer': 'Some key skills for a data scientist include programming, statistical analysis, machine learning, data visualization, and communication.'},
    {'question': 'What is machine learning?', 'answer': 'Machine learning is a method of teaching computers to learn from data, without being explicitly programmed.'},
    {'question': 'What is natural language processing?', 'answer': 'Natural language processing (NLP) is a field of computer science and artificial intelligence concerned with the interactions between computers and human (natural) languages.'},
    {'question': 'What is deep learning?', 'answer': 'Deep learning is a subset of machine learning that involves training artificial neural networks with multiple layers to recognize patterns in data.'}
]

# Tokenize, lemmatize, and remove stop words from the data
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
texts = [[lemmatizer.lemmatize(token.lower()) for token in word_tokenize(qa['question'] + ' ' + qa['answer']) if token.lower() not in stop_words and token.isalpha()] for qa in data]

# Create a dictionary and corpus for the data
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Train the LSI model
lsi_model = models.LsiModel(corpus, num_topics=5, id2word=dictionary)

# Define the chatbot's responses
def generate_response(input_text):
    input_text_tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(input_text) if token.lower() not in stop_words and token.isalpha()]
    input_text_bow = dictionary.doc2bow(input_text_tokens)
    input_text_lsi = lsi_model[input_text_bow]
    index = similarities.MatrixSimilarity(lsi_model[corpus])
    sims = index[input_text_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return data[sims[0][0]]['answer']

# Chat loop
while True:
    input_text = input('You: ')
    response = generate_response(input_text)
    print('Chatbot:', response)

'''
This chatbot uses Latent Semantic Indexing (LSI) to match the user's input to the most similar Q&A pair in the data. The chatbot tokenizes, lemmatizes, and removes stop words from both the data and the user's input, and then converts the text to a bag-of-words representation. It then trains an LSI model on the bag-of-words corpus, and uses the trained model to compute the cosine similarity between the user's input and each Q&A pair in the data. The chatbot returns the answer to the Q&A pair with the highest similarity score.
'''
