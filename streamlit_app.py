import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection('mysql')

def fetch_teams():
    query = "SELECT * FROM Teams;"
    df = conn.query(query, ttl=600)
    return df

# Streamlit app
st.title("NFL Teams Data")

if conn:
    st.success("Successfully connected to the database!")
    
    # Fetch and display data
    df = fetch_teams()
    if not df.empty:
        st.write("Teams data from the nfl_db:")
        st.dataframe(df)
    else:
        st.write("No data found or there was an error fetching data.")
else:
    st.write("Failed to connect to the database.")

    connection.close()
else:
    st.write("Failed to connect to the database.")
