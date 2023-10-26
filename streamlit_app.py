import streamlit as st
import pandas as pd

from models.model import predict_price

# Setup Page
st.set_page_config(
    page_title="Forex Price Prediction using News Sentiment Analysis",
    page_icon="💱",
    menu_items={
        'About': "# This is a webapp to help you predict future forex price market.",
        'Get help':  "https://www.linkedin.com/in/rio-audino/"
    },
    layout="wide"
)
st.title('💱 Forex Price Prediction')
col_capt_1, col_capt_2 = st.columns([1,1])
with col_capt_1:
    st.caption('by: Rio Audino')
with col_capt_2:
    st.caption('Find more about me here: linkedin.com/in/rio-audino/')

# Setup Session State
if "run_process" not in st.session_state:
    st.session_state["run_process"] = False
    st.session_state["download-csv"] = False
    st.session_state["config"] = ""

def run_process():
    st.session_state["run_process"] = True

# Setup model page
tab1, tab2 = st.tabs(["News Text", "Excel File"])

with tab1:
    st.header("Predict Forex Price using Single News")
    
    user_input = st.text_area('Enter your string here:', height = 200)
    if st.button('Predict', key="predict_single"):
        st.header("Prediction Result")
        df_predict, average = predict_price(user_input)
        st.write('')

        if average == "Bullish":
            st.markdown('''
                <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                    Model's today prediction is Bullish
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
                <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                    Model's today prediction is Bearish
                </div>
            ''', unsafe_allow_html=True)

        st.write('')
        
        st.dataframe(df_predict)

with tab2:
    st.header("Predict Forex Price using Multiple News")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        if st.button('Predict', key="predict_df"):
            st.header("Prediction Result")
            df_predict, average = predict_price(df)
            st.write('')

            if average == "Bullish":
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction is Bullish
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction is Bearish
                    </div>
                ''', unsafe_allow_html=True)

            st.write('')
            
            st.dataframe(df_predict)

