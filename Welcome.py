import streamlit as st

st.set_page_config(page_title="Cars Explorer", page_icon="🚘")



#TITLE
st.title("Welcome to Cars Explorer 👋")
st.subheader('About this App')
st.write("""With the help of this app, you should be able to find the car that best suits your needs in terms of both price and other factors. This is quite similar to other car listing websites. The distinction is that we have added some visuals in this instance so that you can explore the unseen potential of the deal you might not aware of. 

This app's data is sourced from Kaggle.com. Data is static and was taken from the market in India. As a result, certain brands may be unfamiliar to you and other regions of the world may have different price points. 

Enjoy finding your dream car!""")

st.subheader("How to Use This App")
st.markdown(
    """1. Navigate to the Explore tab to see all potential cars that might fit into your preferences. This process will open your eyes towards the brands that you might not aware of and the positioning of its brand. You might also grasp the bigger picture of car market so you will be making better decision towards your purchase.
2. Navigate to the Find Your Car tab to see cars that fit your preferences. Note one or two that you fancy most.
3. Contact your local distributor of the car you pick and purchase if the car fit your budget.
4. Drive the brand new car of yours 😎
""")

st.markdown("**Background of this Project**")
st.write(
    """This project is part of my data portfolio. I am learning to create data apps that are usable by the end user while also applying certain technical skills. If you are interested to discover more about the back end of this project please visit this Medium page."""
)
