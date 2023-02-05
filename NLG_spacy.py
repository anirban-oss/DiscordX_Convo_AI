# Steps to make a pipline for Natural language generation in the Data-Science interview questions and answers area.

import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the question-answer pairs
qa_pairs = [("What is data science?", "Data science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data."),
            ("What are the steps in data science?", "The steps in data science include defining the problem, collecting and cleaning data, preparing data for analysis, performing exploratory data analysis, building predictive models, and communicating results."),
            ("What are the types of data?", "There are two main types of data: structured and unstructured data. Structured data is organized and has a clear format, while unstructured data is unorganized and can include things like text, images, and audio."),
            ("What is machine learning?", "Machine learning is a type of artificial intelligence that allows a system to learn from data and make predictions or decisions without being explicitly programmed to perform the task."),
            ("What are the types of machine learning?", "There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.")]

# Loop through the question-answer pairs
for q, a in qa_pairs:
    # Process the question using spaCy
    doc = nlp(q)

    # Find the most similar question in the list
    similarities = [(similarity, index) for index, (_, b) in enumerate(qa_pairs) for similarity in (doc.similarity(nlp(b)),)]
    best_match = max(similarities, key=lambda x: x[0])

    # Print the answer to the most similar question
    print(f"Question: {q}")
    print(f"Answer: {qa_pairs[best_match[1]][1]}")
    print("")

# This code uses spaCy's nlp object to process the questions and 
# find the most similar question in the list of qa_pairs. 
# The similarity method is used to calculate the similarity 
# between two spaCy doc objects, and the answer to the 
# most similar question is printed.
