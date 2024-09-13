import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import streamlit as st

st.title('E-commerce Reviews')
st.text('This is a list of reviews from a certain e-commerce and the impacts of distance and delivery time\nto customer satisfaction')

all_df = pd.read_csv('all_data.csv')

st.subheader('Reviews')
sample = all_df.sample(n=10)
st.dataframe(sample[[
    'review_id',
    'review_score',
    'review_comment_title',
    'review_comment_message'
]])

if st.button("Refresh Reviews"):
    sample = all_df.sample(n=10)
    st.success("refreshed")
else:
    sample = all_df.sample(n=10)
    
    
st.subheader('Distance vs Delivery Time')
st.text('This is the plot for distance vs delivery time. The sample is only 1000 data\nfor visual purposes or else it will be too much')

fig, ax = plt.subplots()
sns.scatterplot(x='distance_km',y='delivery_time', hue='seller_zip_code_prefix', data=all_df[0:1000], palette='inferno',ax=ax)

st.pyplot(fig)

st.text('The plot is differed by the sellers zipcode')


st.subheader('Delivery Time vs Rating')
st.text('This is the plot for delivery time vs rating or review score.')

fig2, ax = plt.subplots()
sns.lineplot(x='review_score', y='delivery_time', hue='order_status', data=all_df, palette='Set2')
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))

st.pyplot(fig2)