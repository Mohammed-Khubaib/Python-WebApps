import streamlit as st
from PIL import Image
import requests
from io import BytesIO


st.title("View & Download any Image from Internet")
# Load the image from a URL
url = st.text_input("Enter the URL")
# url = "https://t2.gstatic.com/licensed-image?q=tbn:ANd9GcQEw4qv6FVQfjFe6SuYJRvk6A6jVRz2fMP-H6QQwvnCZkKKC3dWHRN7yUm_sgCI08fL5dhGrqPYHd17p9A"
if url!="":
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Display the image
    st.image(img, caption='Original Image', use_column_width=True)

    # Create a download button for the image
    data = BytesIO()
    img.save(data, "JPEG")
    data = data.getvalue()
    st.download_button(label="Download Image", data=data, file_name="image.jpg", mime="image/jpeg")
