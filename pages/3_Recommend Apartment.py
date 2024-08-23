import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

st.set_page_config(page_title ="Recommend Apartments")

location_df = pickle.load(open('datasets/location_df.pkl','rb'))

cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl','rb'))

def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# Test the recommender function using a property name
recommend_properties_with_scores('Ireo Victory Valley')



st.title('Select Location And Radius')

selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in km')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values().to_dict()

    for key, value in result_ser.items():
        st.text(str(key)+" "+str(round(value/1000))+'kms')

st.title('Recommend Appartments')
selected_appartment = st.selectbox("Selecte Apartment", sorted(location_df.index.to_list()))

if st.button('Recommend '):
    recommendation_df =recommend_properties_with_scores(selected_appartment)

    st.dataframe(recommendation_df)
