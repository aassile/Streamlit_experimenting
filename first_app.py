import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
            This is my first app with :rainbow[Streamlit].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)