import streamlit as st

st.title('mohit')

col1,col2 = st.columns(2)

with col1:
    st.image('aa.jpg')

with col2:
    st.write('nk ii i ikgig rbosghg viuehgu bvueh u buvj dujfn ubvjeiuerh vbuvejveuv jk ji ni k')


st.header('courses offered')
st.subheader('data science and ML')
st.subheader('data analysis')

st.subheader('python')
st.subheader('sql')
st.subheader('dsa')

st.sidebar.title('meanu')
st.sidebar.markdown("""
- home
- about
- contact
- login
- carrer
""")
