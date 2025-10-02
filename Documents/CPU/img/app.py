# app.py
import streamlit as st
from ColorPaletteGeneration import ColorPaletteGeneration
from PIL import Image
import os

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="🎨 Image Palette Generator",
    page_icon="🖌️",
    layout="wide"
)

# -------------------------------
# Logo
# -------------------------------
logo_path = r"C:\Users\khadi\Documents\CPU\Image_Recolorization\assets\logo.jpg"  # Replace with your logo path
if os.path.exists(logo_path):
    st.image(logo_path, width=80)

# -------------------------------
# Title
# -------------------------------
st.markdown("# 🎨 Image Palette Generator")
st.markdown("Upload an image and generate a color palette automatically!")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Settings")
num_colors = st.sidebar.slider("Number of colors in palette", min_value=2, max_value=10, value=6)
st.sidebar.info(
    "Upload any image and get a color palette automatically generated.\n\n"
    "You can use the palette for design, art, or recoloring purposes."
)

# -------------------------------
# File uploader
# -------------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    # Open the image with PIL
    image = Image.open(uploaded_file)

    # Display uploaded image and palette side by side
    col1, col2 = st.columns(2)
    with col1:
        st.header("Uploaded Image")
        st.image(image, use_container_width=True)

    # Save temporary image
    temp_path = "temp_image.png"
    image.save(temp_path)

    # -------------------------------
    # Generate palette
    # -------------------------------
    palette_generator = ColorPaletteGeneration(temp_path, n_colors=num_colors)
    palette_generator.fittingData()
    palette_generator.plotAndSaveColors()

    # -------------------------------
    # Display palette
    # -------------------------------
    with col2:
        st.header("Generated Palette")
        palette_img = Image.open(palette_generator.save_path)
        st.image(palette_img, use_container_width=True)

        # Show palette as individual color blocks
        # Show palette as individual color blocks with RGB values
        if palette_generator.rgb_palette is not None:
            st.subheader("Palette Colors")
            for color in palette_generator.rgb_palette:
                r, g, b = map(int, color)  # Ensure values are integers
                hex_color = '#%02x%02x%02x' % (r, g, b)
                st.markdown(
                    f"""
                    <div style="display:flex; align-items:center; margin-bottom:6px;">
                        <div style="background-color:{hex_color}; width:60px; height:40px; border-radius:6px; margin-right:10px; border:1px solid #ddd;"></div>
                        <span style="font-size:16px;">RGB: ({r}, {g}, {b})</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Download button
        with open(palette_generator.save_path, "rb") as f:
            st.download_button(
                label="Download Palette",
                data=f,
                file_name="palette.png",
                mime="image/png"
            )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Created with ❤️")
