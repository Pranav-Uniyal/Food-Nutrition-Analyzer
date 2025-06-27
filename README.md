# 🥑 Nutrition AI —  Food Nutrition Analyzer

**Nutrition AI** is a Streamlit-based machine learning web application that analyzes the nutritional content of food items and provides:

* A health rating (🌟 Good, ⚠️ Moderate, ❌ Bad)
* A breakdown of nutritional concerns
* Personalized advice based on your health goals (like Weight Loss, Muscle Gain, etc.)

![image](https://github.com/user-attachments/assets/ae4e392c-917b-4641-9c3c-63bc346aab83)


---

## 🚀 Features

* 📊 **Nutrient Score Encoding** — Calories, fats, sodium, sugars, fiber, and protein are scored and interpreted.
* 🧠 **ML-Powered Health Rating** — Uses a trained ML model to classify overall healthiness.
* 🎯 **Goal-Based Tips** — Personalized advice based on user goals like weight loss or heart health.
* 📆 **Interactive Streamlit UI** — Simple, user-friendly interface with form input and real-time feedback.

---

## 📁 Project Structure

```
Package
├── model_diet.pkl          # Trained ML model (Joblib format)
├── scaler_diet.pkl         # Scaler used for input normalization
└── main.py                 # Main Streamlit application          
```

---

## 🛠️ Requirements

Make sure you have Python 3.x and the following libraries installed:

```bash
pip install streamlit numpy joblib
```

---

## ▶️ How to Run

1. **Clone the Repository**:

```bash
git clone https://github.com/Pranav-Uniyal/Food-Nutrition-Analyzer.git
cd Food-Nutrition-Analyzer
```

2. **Place your model and scaler files**:
   Make sure `model_diet.pkl` and `scaler_diet.pkl` are in the same directory as the script.

3. **Run the Streamlit App**:

```bash
streamlit run main.py
```

4. Open your browser at [http://localhost:8501](http://localhost:8501)

---




## 🧠 Model Logic

The app encodes nutrient scores using predefined thresholds and calculates a total health score. Based on this score:

* A prediction is made using the ML model (`model_diet.pkl`).
* Additional reasoning is provided (e.g., "🔴 High in Sugars").
* Personalized health tips are shown depending on the user's selected goal.

---

## 🎨 Screenshots
![WhatsApp Image 2025-06-27 at 16 44 36_10f2f402](https://github.com/user-attachments/assets/6c540f39-1c9a-4bf7-bfc6-32da1b52db47)
![image](https://github.com/user-attachments/assets/90060b14-062f-4a01-a87b-deb22661ecc6) 
![image](https://github.com/user-attachments/assets/3342a885-63b8-4239-a69d-642bad3c5d8f)

---
![WhatsApp Image 2025-06-27 at 16 44 36_2a6680d8](https://github.com/user-attachments/assets/d47b50c6-0fea-4243-bde3-f0a4f591ee48)
![Screenshot 2025-06-27 164150](https://github.com/user-attachments/assets/0c3fabd0-8ca6-4a95-a47f-5980e8e36363)
![Screenshot 2025-06-27 164209](https://github.com/user-attachments/assets/33ad09bb-9736-40ea-b340-b498444c63cf)


---

## 🧪 Sample Inputs

| Nutrient       | Example Value |
| -------------- | ------------- |
| Food Name      | `apple_pie`   |
| Weight (grams) | `150`         |
| Calories       | `250`         |
| Fats (g)       | `12`          |
| Sugars (g)     | `18`          |
| Sodium (mg)    | `800`         |
| Fiber (g)      | `3`           |
| Protein (g)    | `5`           |

Goal: `Weight Loss`

---
## Dataset link
Kaggle-[Dataset Link](https://www.kaggle.com/datasets/sanadalali/food-101-nutritional-information)

## 👨‍💼 Author

**Pranav Uniyal**
[GitHub](https://github.com/Pranav-Uniyal) | [LinkedIn](https://www.linkedin.com/in/pranav-uniyal-894801251/)
Feel free to connect and contribute!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
