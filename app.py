import streamlit as st
from recommend import get_recommendations

# Add your name in top-left using markdown/HTML
st.markdown("""
    <h4 style='text-align: left; margin-top:0;'>By : SK ARIF AHMED</h4>
""", unsafe_allow_html=True)

st.title("Movie Recommendation System")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name:
        results = get_recommendations(movie_name)
        if results:
            st.subheader("Recommended Movies:")
            for m in results:
                st.write(m)
        else:
            st.error("Movie not found in dataset.")
    else:
        st.warning("Please enter a movie name.")

