import streamlit as st
import numpy as np
import joblib
import os

# --- Load Model and Scaler ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model_diet.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler_diet.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# --- Helper functions for score encoding ---
def encode_calorie_score(calories):
    if calories > 300:
        return 0
    elif 200 <= calories <= 300:
        return 1
    else:
        return 2

def encode_fat(fats):
    if fats > 10:
        return 0
    elif 5 <= fats <= 10:
        return 1
    else:
        return 2

def encode_sodium(sodium):
    if sodium > 1000:
        return 0
    elif 500 <= sodium <= 1000:
        return 1
    else:
        return 2

def encode_fiber(fiber):
    if fiber < 2:
        return 0
    elif 2 <= fiber <= 5:
        return 1
    else:
        return 2

def encode_sugar(sugars):
    if sugars > 10:
        return 0
    elif 5 <= sugars <= 10:
        return 1
    else:
        return 2

def encode_protein(protein):
    if protein < 5:
        return 0
    elif 5 <= protein <= 10:
        return 1
    else:
        return 2

# --- Reasoning function ---
def explain_reasoning(calorie_score, fat_score, sodium_score, fiber_score, sugar_score, protein_score):
    reasons = []
    if calorie_score == 0:
        reasons.append("🔴 High in Calories")
    if fat_score == 0:
        reasons.append("🔴 High in Fats")
    if sodium_score == 0:
        reasons.append("🔴 High Sodium Content")
    if sugar_score == 0:
        reasons.append("🔴 High in Sugars")
    if fiber_score == 2:
        reasons.append("🟢 Excellent Fiber Content")
    if protein_score == 2:
        reasons.append("🟢 Good Protein Source")
    return reasons

# --- Personalized Tips ---
def personalized_tip(goal, fats, sugars, fiber, protein):
    tips = []
    if goal == "Weight Loss":
        if fats > 10:
            tips.append("👉 Reduce fats for better weight loss results.")
        if sugars > 10:
            tips.append("👉 Cut down sugars to lose fat faster.")
    elif goal == "Muscle Gain":
        if protein < 10:
            tips.append("👉 Increase protein intake to build muscles.")
    elif goal == "Diabetes Friendly":
        if sugars > 5:
            tips.append("👉 Lower sugar intake to control blood sugar.")
    elif goal == "Heart Health":
        if fats > 10 or sodium_score == 0:
            tips.append("👉 Reduce fats and sodium for heart protection.")
    return tips

# --- Streamlit UI ---
st.set_page_config(page_title="Nutrition AI 🚀", page_icon="🥑", layout="centered")
st.title("🥑 Nutrition AI")
st.subheader("Food Nutrition Analyzer + Personalized Advice")

# --- User Inputs ---
with st.form("input_form"):
    label = st.text_input("Food Name (e.g., apple_pie)")
    weight = st.number_input("Weight (grams)", min_value=0)
    calories = st.number_input("Calories", min_value=0)
    protein = st.number_input("Protein (grams)", min_value=0)
    carbohydrates = st.number_input("Carbohydrates (grams)", min_value=0)
    fats = st.number_input("Fats (grams)", min_value=0)
    fiber = st.number_input("Fiber (grams)", min_value=0)
    sugars = st.number_input("Sugars (grams)", min_value=0)
    sodium = st.number_input("Sodium (mg)", min_value=0)
    
    goal = st.selectbox(
        "Your Health Goal 🎯",
        ("General Health", "Weight Loss", "Muscle Gain", "Diabetes Friendly", "Heart Health")
    )

    submitted = st.form_submit_button("Analyze Nutrition 🍴")

# --- Prediction Logic ---
if submitted:
    try:
        # Score Encoding
        calorie_score = encode_calorie_score(calories)
        fat_score = encode_fat(fats)
        sodium_score = encode_sodium(sodium)
        fiber_score = encode_fiber(fiber)
        sugar_score = encode_sugar(sugars)
        protein_score = encode_protein(protein)

        total_score = calorie_score + fat_score + sodium_score + fiber_score + sugar_score + protein_score

        # Prepare Input
        input_data = np.array([[weight, calories, protein, carbohydrates, fats,
                                fiber, sugars, sodium, calorie_score, fat_score,
                                sodium_score, fiber_score, sugar_score, protein_score, total_score]])
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)

        # Output Health Label
        if total_score >= 7:
            health_label = "🌟 Good"
        elif 5 <= total_score < 7:
            health_label = "⚠️ Moderate"
        else:
            health_label = "❌ Bad"

        st.markdown(f"## Result: {health_label}")

        # Reasoning
        reasons = explain_reasoning(calorie_score, fat_score, sodium_score, fiber_score, sugar_score, protein_score)
        if reasons:
            st.subheader("🧐 Why this result?")
            for r in reasons:
                st.write(r)
        
        # Personalized Tip
        tips = personalized_tip(goal, fats, sugars, fiber, protein)
        if tips:
            st.subheader("🎯 Personalized Advice for You")
            for t in tips:
                st.info(t)

    except Exception as e:
        st.error(f"⚠️ Error occurred: {e}")

