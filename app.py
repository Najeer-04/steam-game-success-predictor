import streamlit as st
import pickle
import numpy as np

# ---------------- LOAD ---------------- #
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ---------------- UI ---------------- #
st.set_page_config(page_title="Game Success Predictor", page_icon="🎮")

st.title("🎮 Game Success Predictor")
st.write("Predict whether a game will be successful based on its features.")

# ---------------- INPUT SECTIONS ---------------- #

st.header("💰 Pricing")

is_free = st.selectbox("Is the game free?", ["No", "Yes"])

if is_free == "Yes":
    price = 0.0
    st.info("Free game → price automatically set to 0")
else:
    price = st.number_input("Price (USD)", min_value=0.0, max_value=100.0)

# ---------------- #

st.header("⭐ Quality")

metacritic = st.slider("Metacritic Score", 0, 100, 50)

# ---------------- #

st.header("🎯 Game Details")

required_age = st.number_input("Required Age", min_value=0)

genres = st.multiselect(
    "Select Genres",
    ["Action", "RPG", "Adventure", "Indie", "Strategy", "Casual"]
)

game_modes = st.multiselect(
    "Game Modes",
    ["Single-player", "Multi-player", "Co-op", "PvP"]
)

# ---------------- INPUT SUMMARY ---------------- #

st.subheader("📋 Input Summary")
st.write(f"Price: {price}")
st.write(f"Free: {is_free}")
st.write(f"Metacritic: {metacritic}")
st.write(f"Age Requirement: {required_age}")
st.write(f"Genres: {genres}")
st.write(f"Modes: {game_modes}")

# ---------------- PREDICTION ---------------- #

if st.button("🚀 Predict Success"):

    is_free_val = 1 if is_free == "Yes" else 0

    # Genres
    genre_dict = {
        "Action": 0,
        "RPG": 0,
        "Adventure": 0,
        "Indie": 0,
        "Strategy": 0,
        "Casual": 0
    }

    for g in genres:
        if g in genre_dict:
            genre_dict[g] = 1

    # Modes
    mode_dict = {
        "Single-player": 0,
        "Multi-player": 0,
        "Co-op": 0,
        "PvP": 0
    }

    for m in game_modes:
        if m in mode_dict:
            mode_dict[m] = 1

    # Base input
    input_dict = {
        "required_age": required_age,
        "metacritic": metacritic,
        "is_free": is_free_val,
        "price_initial (USD)": price,
        "is_released": 1
    }

    input_dict.update(genre_dict)
    input_dict.update(mode_dict)

    # Fill missing columns
    for col in columns:
        if col not in input_dict:
            input_dict[col] = 0

    # Convert to array
    input_array = np.array([input_dict[col] for col in columns]).reshape(1, -1)

    # Scale
    input_scaled = scaler.transform(input_array)

    # Predict
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    # ---------------- OUTPUT ---------------- #

    st.header("📊 Prediction Result")

    st.metric("Success Probability", f"{prob:.2f}")

    if prediction == 1:
        st.success("🎉 This game is likely to be SUCCESSFUL")
    else:
        st.error("❌ This game is likely NOT successful")

    st.write("### 🧠 Interpretation")
    st.write(
        "This prediction is based on historical patterns. Higher probability indicates higher likelihood of success."
    )

    if metacritic == 0:
        st.warning("⚠️ Missing Metacritic score may reduce prediction accuracy")