
# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import argparse
import json
import os

class CourseRecommender:
    def __init__(self, data_path="data/courses.json"):
        self.data_path = data_path
        self.df = self.load_data()
        self.sim_matrix = None
        self.tfidf_matrix = None
        self.build_model()

    def load_data(self):
        with open(self.data_path, "r") as file:
            data = json.load(file)
        return pd.DataFrame(data)

    def build_model(self):
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.df['Description'])
        self.sim_matrix = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, course_title, top_n=3):
        indices = pd.Series(self.df.index, index=self.df['Course']).drop_duplicates()
        if course_title not in indices:
            raise ValueError(f"Course '{course_title}' not found.")
        idx = indices[course_title]
        sim_scores = list(enumerate(self.sim_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        course_indices = [i[0] for i in sim_scores]
        return self.df['Course'].iloc[course_indices].tolist()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Course Recommendation System")
    parser.add_argument("course", help="Course title to get recommendations for")
    parser.add_argument("--top", type=int, default=3, help="Number of recommendations")
    args = parser.parse_args()

    recommender = CourseRecommender()
    try:
        recommendations = recommender.recommend(args.course, top_n=args.top)
        print(f"Top {args.top} recommendations for '{args.course}':")
        for i, course in enumerate(recommendations, start=1):
            print(f"{i}. {course}")
    except ValueError as e:
        print(e)
