import streamlit as st

st.title("Kuliah 09")

st.write("Halo dek")
st.write('# Heading 1')
st.write("## Heading 2")
st.write("### Heading 3")

pilih1 = st.checkbox("Yes")
pilih2 = st.checkbox("No")

st.write(pilih1)
st.write(pilih2)

st.radio('Pilih makanan', ['Bakso','Nasgor','Mie'])

Minum = st.selectbox('Pilih minuman', ['Teh','Jeruk', 'Susu'])
st.write(Minum)

st.multiselect('Cara bayar:', ['Cash', 'Gopay','Ovo'])
