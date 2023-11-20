import streamlit as st
import pandas as pd

from models.model import predict_price
from utils.constant import *

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
st.title('💱 CheckDXY')

# Setup model page
tab1, tab2, tab3 = st.tabs(["News Text", "Excel File", "Excel File Template"])

with tab1:
    st.header("Predict Forex Price using Single News")
    
    user_input = st.text_area('Enter your news here (Please enter at least 300 character): ', height = 200)
    if st.button('Predict', key="predict_single"):
        if len(user_input) > 300:
            st.header("Prediction Result")
            df_predict, average, percentage = predict_price(user_input)
            st.write('')

            if average == "Bullish":
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction for DXY is Bullish
                    </div>
                ''', unsafe_allow_html=True)
                st.markdown(f'''
                    <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        %Bullish : {percentage}%
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction for DXY  is Bearish
                    </div>
                ''', unsafe_allow_html=True)
                st.markdown(f'''
                    <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        %Bearish : {percentage}%
                    </div>
                ''', unsafe_allow_html=True)

            st.write('')
            
            st.dataframe(df_predict)
        else:
            st.error("Please enter at least 300 characters")

with tab2:
    st.header("Predict Forex Price using Multiple News")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        if st.button('Predict', key="predict_df"):
            st.header("Prediction Result")
            df_predict, average, percentage = predict_price(df)
            st.write('')

            if average == "Bullish":
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction for DXY  is Bullish
                    </div>
                ''', unsafe_allow_html=True)
                st.markdown(f'''
                    <div style="height: 60px; width: 100%; background-color: #52a447; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        %Bullish : {percentage}%
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown('''
                    <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        Model's today prediction for DXY is Bearish
                    </div>
                ''', unsafe_allow_html=True)
                st.markdown(f'''
                    <div style="height: 60px; width: 100%; background-color: #e74c3c; border-radius: 10px; display: flex; justify-content: flex-start; align-items: center; color: white; font-size: 24px; padding-left: 20px; margin: 10px;">
                        %Bearish : {percentage}%
                    </div>
                ''', unsafe_allow_html=True)

            st.write('')
            
            st.dataframe(df_predict)

            df_predict.to_excel(PREDICTION_OUTPUT_PATH, index=False)

            with open(PREDICTION_OUTPUT_PATH, "rb") as template_file:
                template_byte = template_file.read()
            st.download_button(
                label="Click to Download Prediction Result",
                data=template_byte,
                file_name="prediction_result.xlsx",
                mime='application/octet-stream'
            )


    

with tab3:
    st.header("Excel File Template for Prediction")
        
    df = pd.read_excel(DATA_EXAMPLE_PATH)   
    st.dataframe(df)
    
    with open(DATA_EXAMPLE_PATH, "rb") as template_file:
            template_byte = template_file.read()
    st.download_button(
        label="Click to Download Template File",
        data=template_byte,
        file_name="template.xlsx",
        mime='application/octet-stream'
    )
