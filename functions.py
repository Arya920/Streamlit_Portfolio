import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import norm
import pandas as pd
import streamlit as st
from PIL import Image
import sys
import plotly.graph_objects as go


class layout():
    #####################
    # Custom function for printing text
    def head(a, b):
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown(a)
        with col2:
            st.image(Image.open(b))

    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a, unsafe_allow_html=True)
        with col2:
            st.markdown(b, unsafe_allow_html=True)

    def txt2(a, b, c):
        col1, col2, col3 = st.columns([1,5,6])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

    def txt3(a, b):
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

class DonutChart():

    
    # Function to determine the color based on the percentage
    @staticmethod
    def get_color(percentage):
        if 0 <= percentage <= 60:
            return 'orange'       # Bad
        elif 60 < percentage <= 80:
            return 'blue'    # Good
        elif percentage > 90:
            return 'green'     # Best fit
        
    # Streamlit app
    @staticmethod
    def doughnut_plot(percentage):
        
        # Input for percentage value
        #percentage = st.slider("Select a percentage:", 0, 100, 70)
        
        # Determine the color based on the percentage
        color = DonutChart.get_color(percentage)
        
        # Create the donut chart using Plotly
        fig = go.Figure(go.Pie(
            values=[percentage, 100 - percentage],
            hole=0.7,
            marker=dict(colors=[color, 'lightgrey']),
            textinfo='none',
            hoverinfo='skip'
        ))
        
        # Update layout for the chart
        fig.update_layout(
            showlegend=False,
            annotations=[dict(text=f"{percentage}%", x=0.5, y=0.5, font_size=30, showarrow=False)],
            margin=dict(t=0, b=0, l=0, r=0),
            height=200,
            width=200
        )
        
        # Display the chart
        st.plotly_chart(fig)






