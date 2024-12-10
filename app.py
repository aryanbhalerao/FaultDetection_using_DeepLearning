import streamlit as st
from PIL import Image

# Set the title of the app
st.title("Fault Detection for Tennesse Eastmann using LSTM")

# Add a button
if st.button("Run Model"):
    # Load and display the image
    image = Image.open("result.png")  # Replace 'example.jpg' with your image path
    st.image(image, caption="Result after training with LSTM model", use_column_width=True)
else:
    st.write("Run LSTM Model")
