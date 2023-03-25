import streamlit as st

from soan.whatsapp import emoji, general, helper, sentiment, tf_idf, topic, wordcloud


def build_stats(df):
    stats=general.print_stats(df)
    users=list(stats.keys())
    composition_columns=(0.5, 1.5, 1.5, 1, 2, 0.5)
    row15_spacer1, row15_1, row15_2, row15_3, row15_4, row15_spacer2  = st.columns(composition_columns)
    with row15_1:
        st.subheader(" ")
    with row15_2:
        st.subheader(users[0])#name first user
    with row15_3:
       pass
    with row15_4:
        st.subheader(users[1])#name second

    row16_spacer1, row16_1, row16_2, row16_3, row16_4, row16_spacer2  = st.columns(composition_columns)
    with row16_1:
        st.markdown("💬 Number of Messages")
        st.markdown("📝 Number of Words")
        st.markdown("🕒💬 Messages per hour")
        st.markdown("📊💬📝 Avg nr Words per Message")
        st.markdown("📊📝 Avg length of Message")
        st.markdown("Maximum number of message in a day")
        st.markdown("🏆📅 Day with more number of messages")
    with row16_2:
        st.markdown(f"{stats[users[0]]['nr_messages']}")
        st.markdown(f"{stats[users[0]]['nr_words']}")
        st.markdown(f"{round(stats[users[0]]['messages_per_hour'],3)}")
        st.markdown(f"{round(stats[users[0]]['avg_length_words'],2)}")
        st.markdown(f"{round(stats[users[0]]['avg_length_charac'],2)}")
        st.markdown(f"{stats[users[0]]['highscore_day_messages']}")
        st.markdown(f"{stats[users[0]]['highscore_day']}")
    with row16_4:
        st.markdown(f"{stats[users[1]]['nr_messages']}")
        st.markdown(f"{stats[users[1]]['nr_words']}")
        st.markdown(f"{round(stats[users[1]]['messages_per_hour'],3)}")
        st.markdown(f"{round(stats[users[1]]['avg_length_words'],2)}")
        st.markdown(f"{round(stats[users[1]]['avg_length_charac'],2)}")
        st.markdown(f"{stats[users[1]]['highscore_day_messages']}")
        st.markdown(f"{stats[users[1]]['highscore_day']}")

        pass
