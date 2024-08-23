import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.set_page_config(page_title =" Vize Demo")

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.header("Enter your inputs")

property_type = st.selectbox('Property Type',['flats','house'])

sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

bedRoom = float(st.selectbox('Number of BedRooms', sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))

balcony= st.selectbox(' Number of Balconies', sorted(df['balcony'].unique().tolist()))

agePossession = st.selectbox(' Property Age ', sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built_up_area'))

servant_room = float(st.selectbox('Servent Room', [0.0,1.0]))

store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    #form a dataframe
    data = [[property_type, sector, bedRoom, bathroom, balcony, agePossession, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # Calculate the base price
    baseprice_array = np.expm1(pipeline.predict(one_df))
    #baseprice = float(baseprice_array)
    baseprice = baseprice_array.item()
    # Calculate the lower and upper bounds
    low = baseprice - 0.22
    heigh = baseprice + 0.22

    # Display the calculated price range using Streamlit
    st.text("The price of the flat is between {} Cr and {}Cr ".format(round(low, 2), round(heigh, 2)))
