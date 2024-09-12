import streamlit as st
import pymysql

def create_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="8008",
            database="nfl_db"
        )
        return connection
    except pymysql.MySQLError as e:
        st.error(f"Error connecting to the database: {e}")
        return None

def fetch_teams(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Teams")
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        st.error(f"Error fetching data: {e}")
        return []

# Streamlit app
st.title("NFL Database Connection Test")

connection = create_connection()

if connection:
    st.success("Successfully connected to the database!")

    # Fetch and display data
    teams = fetch_teams(connection)
    if teams:
        st.write("Teams data from the nfl_db:")
        for team in teams:
            st.write(f"ID: {team[0]}, Abbreviation: {team[1]}, Name: {team[2]}, Conference: {team[3]}, Division: {team[4]}")
    else:
        st.write("No data found or there was an error fetching data.")

    connection.close()
else:
    st.write("Failed to connect to the database.")
