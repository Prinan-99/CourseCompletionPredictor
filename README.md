# 📘 Course Completion Predictor

A machine learning–powered web application built using **Streamlit** that predicts whether a student is likely to **complete an online course** based on behavioral, performance, and engagement metrics.

The system analyzes features such as login frequency, time spent learning, assignments submitted/missed, progress percentage, and categorical indicators like gender, education level, employment status, and course category.

Its primary purpose is to help identify at-risk learners early and support educational institutions in improving student retention.

---

## 🚀 Features

- Accurate course completion prediction  
- Streamlit-based interactive UI  
- Accepts key student activity inputs  
- Fast and lightweight  
- Uses XGBoost model  
- Includes feature scaling + feature selection  
- Uses only the top 10 best-performing features  

---

## 🧠 Machine Learning Workflow

### **1. Data Preprocessing**
- Handling missing values  
- Removing high-cardinality columns  
- Label Encoding categorical columns  
- Identification of numeric/categorical/binary features  
- Outlier removal  

### **2. Feature Selection**
- SelectKBest to identify top 10 most important features:

### **3. Model Training**
- XGBoost chosen for best accuracy and performance  
- Trained on scaled selected features only  
- Saved using Joblib: `xgb_model.pkl`  

### **4. Deployment**
- Streamlit app: `app.py`  
- Scaler fitted on selected features: `scaler_selected.pkl`  

---

## 🖥️ Tech Stack

- **Python 3**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **XGBoost**
- **Streamlit**
- **Joblib**

---

## 🌐 How to Run the Application

### **1. Install dependencies**

### **2. Run the Streamlit app**

---

## 📊 Prediction Output

### ✔ Likely to Complete  
Indicates strong engagement and learning behavior.

### ✘ Likely to Drop Out  
Shows risk indicators — useful for early intervention.

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, open an issue first to discuss what you want to modify.

---

## 📜 License
This project is released under the **MIT License**.
