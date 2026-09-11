# import statements
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the data
predictions = pd.read_csv('predictions_2025.csv', index_col=False)

# seperate into tabs
tab1, tab2 = st.tabs(["Plotter", "All Game IDs"])

# make tab 1 (does main visualization)
with tab1:
    st.title("2025 College Football Win Probability Plotter")
    st.write("Welcome to the 2025 College Football Win Probability Plotter!")

    user_input = st.text_input("Please Enter a Game ID (e.g., 401756846):")
    if user_input:
        try:
            game_id = int(user_input)
            game_row = predictions[predictions['game_id'] == game_id]
            if game_row.empty:
                st.warning(f"No game found with ID: {game_id}. Please check the 'All Game IDs' tab and try again.")
            else:
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

        except ValueError:
            st.error("Please enter a valid numeric Game ID with 9 digits.")

with tab2:
    st.title("All Possible Game IDs")
    st.write("Here are all the game IDs for the 2025 season:")
    st.dataframe(predictions[['game_id', 'team', 'opponent']])