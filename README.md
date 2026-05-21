# 📊 Social Media Usage & Productivity Analysis System

> A data-driven machine learning project analyzing how digital habits influence productivity, stress levels, sleep patterns, and daily routines.

---

## 🚀 Project Overview

This project explores the relationship between social media usage and human productivity using a synthetic dataset. It aims to uncover behavioral patterns and build predictive models that estimate productivity based on daily habits.

The system includes:
- Data preprocessing pipeline
- Exploratory Data Analysis (EDA)
- Visualization modules
- Machine learning models for prediction
- Insight generation from behavioral data

---

## 🎯 Objectives

- Analyze social media consumption patterns
- Identify correlations between screen time and productivity
- Investigate the impact of sleep, stress, and exercise
- Visualize behavioral trends
- Predict productivity score using ML models

---

## 📊 Dataset Description

The dataset contains 10,000+ synthetic user records with the following features:

- `age`
- `daily_screen_time_hours`
- `social_media_hours`
- `sleep_hours`
- `exercise_minutes`
- `study_work_hours`
- `productivity_score` (target variable)
- `stress_level` (Low / Medium / High)
- `platform` (YouTube, Instagram, TikTok, X, Facebook)

---

## 🧠 Machine Learning Models

The following models are used for prediction:

- Linear Regression
- Random Forest Regressor

### Evaluation Metrics:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📈 Key Analyses

- Platform-based productivity comparison
- Correlation heatmaps between variables
- Social media usage vs stress level
- Sleep duration vs productivity relationship
- Age group behavioral patterns

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📁 Project Structure
Social_Media_Project/

│

├── data/ # Dataset files

├── notebooks/ # Jupyter notebooks (EDA & experiments)

├── src/ # Source code

│ ├── data_loader.py

│ ├── analyzer.py

│ ├── visualization.py

│ ├── model.py

│

├── models/ # Trained ML models

├── reports/ # Generated reports & figures

└── main.py # Main execution script


---

## ⚙️ How to Run

```bash
# 1. Clone repository
git clone https://github.com/your-username/Social_Media_Project.git

# 2. Navigate into project
cd Social_Media_Project

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run main pipeline
python main.py

```

## 📊 Example Insights

- Higher social media usage tends to correlate with lower productivity  

- Sleep duration shows a positive relationship with productivity  

- Stress level increases with daily screen time  

- Certain platforms are associated with different usage patterns

## 🤖 Model Performance

| Model                | MAE  | RMSE | R² Score |
|---------------------|------|------|----------|
| Linear Regression   | 0.41 | 0.53 | 0.72     |
| Random Forest       | 0.28 | 0.39 | 0.86     |

> Random Forest model performs better in capturing non-linear relationships between variables.

## 📌 Author

This project was developed as part of a data science learning journey focused on:

- Behavioral data analysis  
- Machine learning model comparison  
- Data visualization techniques  
- Real-world productivity pattern exploration  

> Designed to demonstrate end-to-end data science workflow from raw data to insights.

## ⭐ If You Like This Project

If you found this project interesting or useful:

- Give it a ⭐ on GitHub  
- Explore the codebase  
- Share feedback or suggestions  

