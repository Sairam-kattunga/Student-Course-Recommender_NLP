
# 🎓 Advanced Course Recommender System

This is an advanced, command-line based course recommendation system for students. It uses Natural Language Processing (TF-IDF + Cosine Similarity) to find similar courses based on course descriptions.

---

## 🔍 Features

- Recommend similar courses based on user input
- Uses TF-IDF vectorizer and cosine similarity
- CLI interface to run from terminal
- Modular and extensible Python code
- Clean dataset in JSON format

---

## 🧠 Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

---

## 📦 Dataset

Stored in `data/courses.json`, contains course titles and descriptions.

---

## 🚀 How to Use

### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Run the recommender

```bash
python recommender.py "Data Science" --top 3
```

### ✅ Sample Output

```
Top 3 recommendations for 'Data Science':
1. Machine Learning
2. Python Basics
3. Web Development
```

---

## 📂 Project Structure

```
advanced-course-recommender-system/
├── recommender.py
├── requirements.txt
├── README.md
└── data/
    └── courses.json
```

---

## 🧩 Future Enhancements

- Web UI using Streamlit or Flask
- Real-time course update from database
- Student profile–based recommendations

---

## 📃 License

MIT License
