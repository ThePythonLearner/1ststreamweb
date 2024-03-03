import streamlit as st

st.set_page_config(page_title="About Me", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi, I'm Sreyansh Tammiraju :wave:")
    st.title("Born in Hyderabad. Nov 16, 2011 ૐ")
    st.subheader("I'm passionate to use Python and Streamlit for better apps")
    st.write("[Learn More](https://streamlit.io)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Life")
        st.write("##")
        st.write(
            """My mother tongue is Telugu and I am in 6th class Sem. 2. I live in Lake Stevens, Washington, in a community called "The Alders".
             I study at North Lake Middle School. Our family came to America when I was 4 years old 
             and we had been living here from 8 years . We would sometimes visit India occasionally.""")
