import streamlit as st
import pickle
import pandas as pd

teams = [
    "Sunrisers Hyderabad",
    "Mumbai Indians",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Kings XI Punjab",
    "Chennai Super Kings",
    "Rajasthan Royals",
    "Delhi Capitals",
]

cities = [
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Indore",
    "Kolkata",
    "Delhi",
    "Chandigarh",
    "Jaipur",
    "Chennai",
    "Cape Town",
    "Port Elizabeth",
    "Durban",
    "Centurion",
    "East London",
    "Johannesburg",
    "Kimberley",
    "Bloemfontein",
    "Ahmedabad",
    "Cuttack",
    "Nagpur",
    "Dharamsala",
    "Visakhapatnam",
    "Pune",
    "Raipur",
    "Ranchi",
    "Abu Dhabi",
    "Sharjah",
    "Mohali",
    "Bengaluru",
]
pipe = pickle.load(
    open(
        r"C:\Users\singh\OneDrive\Desktop\ML Project 1\IPL Win Predicter\pipe.pkl", "rb"
    )
)

st.title("....IPL Winner Preditions....")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the Batting Team", sorted(teams))

with col2:
    bowling_team = st.selectbox("Selectthe Bowling Team", sorted(teams))

selected_city = st.selectbox("Select the host city", sorted(cities))
target = st.number_input("Target")

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Current Score")

with col4:
    wickets = st.number_input("Wickets Fallen")

with col5:
    overs = st.number_input("Overs Completed")

if st.button("Know the result"):
    runs_left = target - score
    balls_left = 120 - overs * 6
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame(
        {
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [selected_city],
            "runs_left": [runs_left],
            "balls_left": [balls_left],
            "wickets": [wickets],
            "total_runs_x": [target],
            "crr": [crr],
            "rrr": [rrr],
        }
    )
    # st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + ":" + str(round(win * 100)) + "%")
    st.header(bowling_team + ":" + str(round(loss * 100)) + "%")
