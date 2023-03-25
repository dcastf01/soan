import streamlit as st

from soan.whatsapp import emoji, general, helper, sentiment, tf_idf, topic, wordcloud
from utils_streamlit import build_stats


#in english
def main():

    # List of supported languages
    LANGUAGES = ["English", "Spanish", "French coming", "German coming"]

    # Set page title and favicon
    st.set_page_config(layout="wide", page_title="Analyzing whatsapp chats", )
    st.write(
        "Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/) by David Castellano (https://www.linkedin.com/in/davidcastellanofalcon/)"
    )
    # Set page header and image
    st.write("## We are going to analyze your whatsapp chat")
    st.write(
        "Try uploading an whatsapp chat, you can export one from you mobile and import here to watch magically some insights."
    )
    text_with_explanation="if you don't know how to download the file is > Go to WhatsApp > to the chat that you want > Settings > More > Export chat (without media)"
    #I want a button with the name explain with image please and if the do click in the button appear the cols with the images
    show_explanation = st.session_state.get("show_text", False)


    col11, col12 = st.columns((4,2))
    with col11:
        st.write(text_with_explanation)
    with col12:
        # explanation_button=st.button("Explain with images please")
        # print(type(explanation_button))
        if st.button("Explain with images please"):
            show_explanation = not show_explanation
            st.session_state["show_text"] = show_explanation


    #write three columns using streamlit
    if show_explanation:
        col21,col22,col23=st.columns(3)
        col21.image("assets/example_to_download_1.jpg",)# width=250)
        col22.image("assets/example_to_download_2.jpg",)# width=250)
        col23.image("assets/example_to_download_3.jpg",)# width=250)


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

        #print moments
        build_stats(df)

        try:
            st.plotly_chart(general_fig)
        except:
            st.write("Sorry, I have a error with your txt and I can't show you the general stats, please feel free to contact me by Linkedin and I will solve it")

    elif button and not uploaded_file:
        st.markdown("<h3 style='font-size: 18px;'>Please upload a file</h3>", unsafe_allow_html=True)



    #footer
    #write that is they want to know more about the project or feedback or contact me for any type project feel free to write me by Linkedin
    st.write("## Contact Me ")
    st.write('If you want to know more about the project or give me feedback or contact me for any type of project feel free to write me by [Linkedin](https://www.linkedin.com/in/davidcastellanofalcon/)')

if __name__ == '__main__':
    main()
