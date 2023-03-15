import streamlit as st

from soan.whatsapp import emoji, general, helper, sentiment, tf_idf, topic, wordcloud


def build_stats(df):

    composition_columns=(0.5, 1.5, 1.5, 1, 2, 0.5)
    row15_spacer1, row15_1, row15_2, row15_3, row15_4, row15_spacer2  = st.columns()
    with row15_1:
        st.subheader(" ")
    with row15_2:
        st.subheader()#name first user
    with row15_3:
       pass
    with row15_4:
        st.subheader()#name second

    row16_spacer1, row16_1, row16_2, row16_3, row16_4, row16_spacer2  = st.columns((0.5, 1.5, 1.5, 1, 2, 0.5))
    with row16_1:
        st.markdown("💬 Number of Messages")
        st.markdown("📝 Number of Words")
        st.markdown("🕒💬 Messages per hour")
        st.markdown("📊💬📝 Avg nr Words per Message")
        st.markdown("📊📝 Avg length of Message")
        st.markdown("🏆📅 Highscore Day per User")
    with row16_2:
        pass
    with row16_4:


        pass
