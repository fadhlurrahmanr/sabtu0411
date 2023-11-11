import streamlit as st

# Ini heading aplikasi
st.title("Kuliah 09")
st.write("Halo dek")
st.write('# Heading 1')
st.write('#### Heading 4')

# Kinerja unit
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)
st.metric("Kurs", 100,20)

# Pilihan
pilih1 = st.checkbox("Yes")
pilih2 = st.checkbox("No")

st.write(pilih1)
st.write(pilih2)

'''Ini komentar
'''

st.radio('Pilih makanan', ['Bakso','Nasgor','Mie'])

Minum = st.selectbox('Pilih minuman', ['Teh','Jeruk', 'Susu'])
st.write(Minum)

st.multiselect('Cara bayar:', ['Cash', 'Gopay','Ovo'])
