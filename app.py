import streamlit as st

from soan.whatsapp import emoji, general, helper, sentiment, tf_idf, topic, wordcloud
from utils_streamlit import build_stats


#in english
def main():

    # List of supported languages
    LANGUAGES = ["English", "Spanish", "French coming", "German coming"]

    # Set page title and favicon
    st.set_page_config(layout="wide", page_title="Analyzing whatsapp chats", )

    # Set page header and image
    st.write("## We are going to analyze your whatsapp chat")
    st.write(
        "Try uploading an whatsapp chat, you can export one from you mobile and import here to watch magically some insights."
    )
    st.write(" if you don't know how to download the file is > Go to WhatsApp > tap More options > Settings > Chats > Chat backup > BACK UP")
    st.sidebar.write("## Upload and pick language :gear:")

    uploaded_file = st.sidebar.file_uploader("Upload the chat", type=["txt"],accept_multiple_files = False)
    language = st.sidebar.selectbox("Select language of your whatsapp chat", LANGUAGES)
    button=st.sidebar.button("Show me the magic")

    # st.image("https://cdn.pixabay.com/photo/2016/03/31/20/51/folder-1294924_960_720.png", width=100)

    # Display image and file uploader in the same row
    col1, col2 = st.columns(2)

    if button and uploaded_file:
        # Load data
        df = helper.import_data(uploaded_file,file_from_streamlit=True)
        df = helper.preprocess_data(df)

        users = set(df.User)

        general.install_fonts()

        general_fig=general.plot_messages(df, colors=None, trendline=True, savefig=False, dpi=100)
        try:
            st.plotly_chart(general_fig)
        except:
            st.write("Sorry, I can't show you the general stats")
        #print moments
        build_stats(df)

    elif button and not uploaded_file:
        st.markdown("<h3 style='font-size: 18px;'>Please upload a file</h3>", unsafe_allow_html=True)





if __name__ == '__main__':
    main()
