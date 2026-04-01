# 🎮 Game Success Prediction App

## 🚀 Overview
This project predicts whether a video game will be successful based on its features such as pricing, genre, gameplay modes, and review scores.

A machine learning model was trained on a Steam games dataset and deployed as a live web application using Streamlit.

👉 Live App: https://steam-game-success-predictor-z2kbikdeiq3lgq3ggks9gr.streamlit.app/

---

## 📊 Problem Statement
Game developers often lack data-driven insights to estimate the success of a game before release.

This project aims to:
- Predict game success using historical data
- Provide a simple interface for testing different game configurations

---

## 🧠 Approach

### 1. Data Preprocessing
- Cleaned and structured Steam dataset
- Handled categorical features (genres, game modes)
- Converted boolean features to numeric
- Removed noisy features (e.g., achievements due to potential leakage)

---

### 2. Feature Engineering
- One-hot encoding for genres and gameplay features
- Created pricing categories
- Selected relevant features for modeling

---

### 3. Model Selection
- Used Logistic Regression with `class_weight="balanced"`
- Focused on **recall** to better identify successful games

---

### 4. Evaluation
- Used confusion matrix and classification report
- Observed trade-off between precision and recall
- Performed sensitivity testing on key features

---

## ⚖️ Key Insight
The model is optimized to identify potentially successful games, even at the cost of some false positives.

---

## 🌐 Deployment
- Built an interactive UI using Streamlit
- Deployed using Streamlit Community Cloud
- Allows users to input game features and get real-time predictions

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## ⚠️ Limitations
- Limited feature coverage (not all game attributes included)
- Model may be optimistic due to recall optimization
- Predictions are based on historical patterns, not guaranteed outcomes

---

## 🚀 Future Improvements
- Add more features (release year, platform popularity)
- Improve model with ensemble methods
- Enhance UI and user experience

---

## 📌 Conclusion
This project demonstrates an end-to-end machine learning workflow, from data preprocessing and modeling to deployment as a real-world application.
