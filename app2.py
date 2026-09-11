# import statements
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the data
wp = pd.read_csv('cfb_2025_game_data.csv', index_col=False)

predictions = pd.read_csv('predictions_2025.csv', index_col=False)

# seperate into tabs
tab1, tab2, tab3 = st.tabs(["Plotter", "Post Game Win Probabilities", "All Game IDs"])

# makes tab 1 which plots wp throughout the game
with tab1:
    st.title("2025 College Football Win Probability Plotter")
    st.subheader("Welcome to the 2025 College Football Win Probability Plotter!")

    st.write("- This page creates a line plot of the win probability for each team throughout the game.")
    st.write("- The 'Post Game Win Probabilities' page creates a stacked bar chart of the win probabilities after the game for each team using the box score data.")
    st.write("- The 'All Game IDs' page creates a list of all valid game IDs for the 2025 season.")

    user_input = st.text_input("Please Enter a Game ID (e.g., 401756846):", key="game_id_input_1")
    if user_input:
        try:
            game_id = int(user_input)
            game_row = wp[wp['game_id'] == game_id]
            if game_row.empty:
                st.warning(f"No game found with ID: {game_id}. Please check the 'All Game IDs' tab and try again.")
            else:
                #row = game_row.iloc[0]
                st.write(f"Game ID: {game_id} corresponds to the 2025 showdown between {game_row['homeTeamName'].iloc[0]} and {game_row['awayTeamName'].iloc[0]}")
                fig, ax = plt.subplots()
                ax.plot(game_row['game_play_number'], game_row['home_wp_after'], label=game_row['homeTeamName'].iloc[0])
                ax.plot(game_row['game_play_number'], game_row['away_wp_after'], label=game_row['awayTeamName'].iloc[0])
                ax.set_xlabel("Play Number", color="black")
                ax.set_ylabel("Win Probability (%)", color="black")
                ax.set_title("Win Probability Throughout The Game", color="black")
                ax.tick_params(colors="black")
                for spine in ax.spines.values():
                    spine.set_color("black")
                ax.legend()

                st.pyplot(fig)

        except ValueError:
            st.error("Please enter a valid numeric Game ID with 9 digits.")

# Tab 2 does post game win probabilities
with tab2:
    st.title("Post Game Win Probabilities")
    st.write("This page creates a stacked bar chart of the win probabilities for each team after the game using the box score data.")

    user_input_2 = st.text_input("Please Enter a Game ID (e.g., 401756846):", key="game_id_input_2")
    if user_input_2: # C:\Users\ajhay\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run app2.py
        try:
            game_id_2 = int(user_input_2)
            game_row_2 = predictions[predictions['game_id'] == game_id_2]
            if game_row_2.empty:
                st.warning(f"No game found with ID: {game_id_2}. Please check the 'All Game IDs' tab and try again.")
            else:
                row = game_row_2.iloc[0]
                st.write(f"Game ID: {game_id_2} corresponds to the 2025 showdown between {row['team']} and {row['opponent']}")
                st.write(f"Predicted Win Probability for {row['team']} (according to the model): {row['predicted_win_prob']:.2%}")
                st.write(f"Predicted Win Probability for {row['opponent']} (according to the model): {row['opponent_win_prob']:.2%}") 
                fig_2, ax_2 = plt.subplots()
                labels_2 = [row['team'], row['opponent']]
                matchup_label = f"{row['team']} vs {row['opponent']}"
                ax_2.bar(matchup_label, row['predicted_win_prob']*100, label=row['team'], color="#1f77b4")
                ax_2.bar(matchup_label, row['opponent_win_prob']*100, bottom=row['predicted_win_prob']*100, label=row['opponent'], color="#ff7f0e")
                ax_2.set_ylabel("Win Probability (%)", color="black")
                ax_2.set_title("Post Game Win Probabilities (according to the model)", color="black")
                ax_2.tick_params(colors="black")
                ax_2.legend()
                st.pyplot(fig_2)
        
        except ValueError:
            st.error("Please enter a valid numeric Game ID with 9 digits.")

# makes tab 3 which shows all valid game ids
with tab3:
    st.title("All Valid Game IDs")
    st.write("Here are all the game IDs for the 2025 season:")
    uni_list = pd.DataFrame(wp.groupby('game_id', as_index=False)[['game_id', 'homeTeamName', 'awayTeamName']].first())
    st.dataframe(uni_list)