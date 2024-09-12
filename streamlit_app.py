import streamlit as st
import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="8008",
            database="nfl_db"
        )
        return connection
    except mysql.connector.Error as e:
        st.error(f"Error connecting to the database: {e}")
        return None

def insert_game(connection, date, team1_id, team2_id, team1_score, team2_score, location):
    cursor = connection.cursor()
    query = """
    INSERT INTO Games (date, team1_id, team2_id, team1_score, team2_score, location) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (date, team1_id, team2_id, team1_score, team2_score, location))
    connection.commit()
    cursor.close()

def fetch_games(connection):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM Games;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def update_game(connection, game_id, team1_score, team2_score):
    cursor = connection.cursor()
    query = """
    UPDATE Games SET team1_score = %s, team2_score = %s WHERE game_id = %s
    """
    cursor.execute(query, (team1_score, team2_score, game_id))
    connection.commit()
    cursor.close()

def delete_game(connection, game_id):
    cursor = connection.cursor()
    query = "DELETE FROM Games WHERE game_id = %s"
    cursor.execute(query, (game_id,))
    connection.commit()
    cursor.close()

# Streamlit UI
st.title("NFL Games CRUD Operations")

# Connect to database
connection = create_connection()

if connection:
    st.success("Successfully connected to the database!")
    
    # Create Game
    st.subheader("Insert a New Game")
    with st.form(key="insert_game_form"):
        date = st.date_input("Game Date")
        team1_id = st.number_input("Team 1 ID", min_value=1)
        team2_id = st.number_input("Team 2 ID", min_value=1)
        team1_score = st.number_input("Team 1 Score", min_value=0)
        team2_score = st.number_input("Team 2 Score", min_value=0)
        location = st.text_input("Location")
        submit_button = st.form_submit_button("Insert Game")
        if submit_button:
            insert_game(connection, date, team1_id, team2_id, team1_score, team2_score, location)
            st.success("Game inserted successfully!")

    # Read Games
    st.subheader("View Games")
    games = fetch_games(connection)
    if games:
        st.write("Games data from nfl_db:")
        st.write(games)
    else:
        st.write("No games found or there was an error fetching data.")

    # Update Game
    st.subheader("Update a Game")
    with st.form(key="update_game_form"):
        game_id = st.number_input("Game ID", min_value=1)
        team1_score = st.number_input("New Team 1 Score", min_value=0)
        team2_score = st.number_input("New Team 2 Score", min_value=0)
        update_button = st.form_submit_button("Update Game")
        if update_button:
            update_game(connection, game_id, team1_score, team2_score)
            st.success("Game updated successfully!")

    # Delete Game
    st.subheader("Delete a Game")
    with st.form(key="delete_game_form"):
        game_id = st.number_input("Game ID to Delete", min_value=1)
        delete_button = st.form_submit_button("Delete Game")
        if delete_button:
            delete_game(connection, game_id)
            st.success("Game deleted successfully!")
else:
    st.write("Failed to connect to the database.")
