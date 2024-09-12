import streamlit as st
import pymysql

def create_connection(db_name):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="8008",
        database=db_name
    )

# Toggle between NFL and CFB
option = st.selectbox("Select League", ["NFL", "CFB"])
db_name = "nfl_db" if option == "NFL" else "cfb_db"

connection = create_connection(db_name)

def insert_game(connection, date, team1_id, team2_id, team1_score, team2_score, location):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Games (date, team1_id, team2_id, team1_score, team2_score, location) VALUES (%s, %s, %s, %s, %s, %s)",
                   (date, team1_id, team2_id, team1_score, team2_score, location))
    connection.commit()

def update_game(connection, game_id, team1_score, team2_score):
    cursor = connection.cursor()
    cursor.execute("UPDATE Games SET team1_score = %s, team2_score = %s WHERE game_id = %s",
                   (team1_score, team2_score, game_id))
    connection.commit()

def delete_game(connection, game_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Games WHERE game_id = %s", (game_id,))
    connection.commit()

# Example UI for inserting a game
with st.form("game_form"):
    date = st.date_input("Game Date")
    team1_id = st.number_input("Team 1 ID", min_value=1)
    team2_id = st.number_input("Team 2 ID", min_value=1)
    team1_score = st.number_input("Team 1 Score", min_value=0)
    team2_score = st.number_input("Team 2 Score", min_value=0)
    location = st.text_input("Location")
    submit = st.form_submit_button("Submit")

    if submit:
        insert_game(connection, date, team1_id, team2_id, team1_score, team2_score, location)
        st.success("Game inserted successfully!")

# UI for updating and deleting games can be added similarly
