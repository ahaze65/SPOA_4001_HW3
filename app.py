# import statements
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the data
predictions = pd.read_csv('predictions_2025.csv', index_col=False)

st.title("2025 College Football Win Probability Predictor")
st.write("Welcome to the 2025 College Football Win Probability Predictor!")

user_input = st.text_input("Please Enter a Game ID (e.g., 401756846):")
if user_input:
    st.write(f"Game ID: {user_input} corresponds to the 2025 showdown between {predictions.loc[user_input, 'team']} and {predictions.loc[user_input, 'opponent']}")
    st.write(f"Predicted Win Probability for {predictions.loc[user_input, 'team']}: {predictions.loc[user_input, 'predicted_win_prob']:.2%}")
    st.write(f"Predicted Win Probability for {predictions.loc[user_input, 'opponent']}: {predictions.loc[user_input, 'opponent_win_prob']:.2%}") 
    fig, ax = plt.subplots()
    sizes = [predictions.loc[user_input, 'predicted_win_prob'], predictions.loc[user_input, 'opponent_win_prob']]
    labels = [predictions.loc[user_input, 'team'], predictions.loc[user_input, 'opponent']]
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # keeps it circular
    st.pyplot(fig)