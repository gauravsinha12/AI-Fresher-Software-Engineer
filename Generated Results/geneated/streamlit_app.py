import streamlit as st
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd

# Streamlit UI
st.title("Suzlon Energy Analysis")

# Input for code execution
code_input = st.text_area("Enter your code to run:", height=150)

if st.button("Run Code"):
    # Send code to Jupyter backend via API
    response = requests.post('http://localhost:5000/execute', json={'code': code_input})
    output = response.json().get('output', 'No output returned')

    # Display output
    st.write("Code Output:")
    st.write(output)
    
    # Display plots
    # Check if the output contains URLs to plots
    if 'plot' in output:
        st.image(BytesIO(requests.get(output['plot']).content), caption='Plot', use_column_width=True)
