import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "fees": ["Fees depends on course.", "It is affordable."],
    "admission": ["You can apply online.", "Visit admission portal."]
}
vectorizer = TfidfVectorizer()
def get_response(user_input):
    all_questions = list(data.keys())
    all_answers = list(data.values())
    tfidf = vectorizer.fit_transform(all_questions + [user_input])
    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    index = similarity.argmax()
    return random.choice(all_answers[index])