
# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample course data
data = {
    'Course': ['Python Basics', 'Advanced Java', 'Data Science', 'Web Development', 'Machine Learning'],
    'Description': [
        'Learn the basics of Python including syntax, variables, and data types.',
        'Deep dive into Java programming concepts like OOPs and multithreading.',
        'Covers data preprocessing, visualization, and statistical analysis.',
        'Frontend and backend web development with HTML, CSS, JS, and Django.',
        'Build and train models using regression, classification and clustering.'
    ]
}

df = pd.DataFrame(data)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Description'])

# Compute similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommend function
def recommend(course_title):
    indices = pd.Series(df.index, index=df['Course']).drop_duplicates()
    idx = indices[course_title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]

    course_indices = [i[0] for i in sim_scores]
    return df['Course'].iloc[course_indices]

# Test
print("Recommended for 'Data Science':")
print(recommend('Data Science'))
