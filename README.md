
# 📚 Student Course Recommender System

This is a simple content-based recommendation system built using Python. It suggests similar courses based on course descriptions using TF-IDF and cosine similarity.

---

## 🧠 Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 🚀 How It Works

The system:
1. Takes a list of course titles and descriptions.
2. Converts text into vectors using **TF-IDF**.
3. Calculates **cosine similarity** between all courses.
4. Recommends the most similar courses to the one selected.

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/your-username/student-course-recommender-system.git
cd student-course-recommender-system
pip install -r requirements.txt
python recommender.py
```

---

## 💡 Example

```python
recommend('Data Science')
```

**Output:**
```
1. Machine Learning
2. Web Development
3. Python Basics
```

---

## 📃 License

MIT License
