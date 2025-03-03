import yfinance as yf
import streamlit as st

st.write(
    """
        # Building stock market app

        Learn stock market using streamlit
    """
)

col1, col2 = st.columns(2)

import datetime

with col1:
    start_date = st.date_input("Please enter Starting Date",
                  datetime.date(2019,1,1))

with col2:
    end_date = st.date_input("Please enter Starting Date",
                  datetime.date(2022,12,31))

ticker_symbol = st.text_input("Enter Stock Symbol",
                              "AAPL",
                              key="placeholder")
ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period="1d", start=f"{start_date}",
                                end=f"{end_date}")

st.dataframe(ticker_df)

st.write(
    """
       ## Daily Closing Price Chart
    """
)
st.line_chart(ticker_df.Close)

st.write(
    """
        ## Volume of Shares Traded Each Day
    """
)
st.line_chart(ticker_df.Volume)