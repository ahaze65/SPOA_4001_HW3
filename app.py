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
    game_id = int(user_input)
    game_row = predictions[predictions['game_id'] == game_id]
    row = game_row.iloc[0]
    st.write(f"Game ID: {game_id} corresponds to the 2025 showdown between {row['team']} and {row['opponent']}")
    st.write(f"Predicted Win Probability for {row['team']}: {row['predicted_win_prob']:.2%}")
    st.write(f"Predicted Win Probability for {row['opponent']}: {row['opponent_win_prob']:.2%}") 
    fig, ax = plt.subplots()
    sizes = [row['predicted_win_prob'], row['opponent_win_prob']]
    labels = [row['team'], row['opponent']]
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # keeps it circular
    st.pyplot(fig)