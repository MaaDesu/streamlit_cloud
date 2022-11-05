import streamlit as st

st.title('Helium Test要画面')

tab1, tab2, tab3, tab4 = st.tabs(['Cat', 'Dog', 'Fox', 'Hamster'])
col11, col12, col13, col14 = st.columns((2, 3, 5, 3))
col21, col22, col23, col24 = st.columns(4)
options1 = ['20歳未満', '20歳～60歳未満', '60歳代', '70歳以上']

with tab1:
    st.header('A cat')
    st.write('🐱')
    col11.text_input('郵便番号')
    col12.text_input('都道府県')
    col13.text_input('市区町村')
    col14.text_input('番地名')
    with col21:
        st.text_input('第１希望')
    with col22:
        st.text_input('第２希望')
    with col23:
        st.text_input('第３希望')
    with col24:
        st.text_input('第４希望')   
    st.radio('性別', options1, horizontal=True)
    st.text_area('ご意見')
with tab2:
    st.header('A dog')
    st.write('🐶')
with tab3:
    st.header('A fox')
    st.write('🦊')
with tab4:
    st.header('A hamster')
    st.write('🐹')
