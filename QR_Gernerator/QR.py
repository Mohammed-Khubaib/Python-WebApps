import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
  
st.title("QR code Generator")

# Get user input
a = st.text_input("Enter the input for QR code")

if a:
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4,) 
    qr.add_data(a) 
    qr.make(fit=True)

    # Get color input from user
    fill_color = st.text_input("Enter the color for QR code")
    if fill_color !="":
        # Create image
        img = qr.make_image(fill_color=fill_color, back_color="white")
        
        # Save image as JPEG
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        image_bytes = buffer.getvalue()

        # Display image
        st.image(Image.open(BytesIO(image_bytes)), caption="QR code", use_column_width=True)

        # Download button for image
        st.download_button(label="Download QR code", data=image_bytes, file_name="QR code.jpeg", mime="image/jpeg")
