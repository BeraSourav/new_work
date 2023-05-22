import streamlit as st
import tempfile
from PIL import Image
from pathlib import Path


st.set_page_config(
    page_title="Nphi TOOLS",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/sourav-bera-85a184218/',
        'About': "This is an *extremely* cool app!"
    }
)

st.markdown(
    """
    <div class="footer">
        Made with ❤️ by <a href="https://www.linkedin.com/in/sourav-bera-85a184218/" target="_blank">Sourav</a>
    </div>

    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: black;
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: red; font-style:italic;'>NΦ TOOLS</h1>", unsafe_allow_html=True)

st.markdown("<a style='color:brown; font-style:italic; font-size:25px;' href='/Image_Compressor' target='_self'>Image Compressor</a>", unsafe_allow_html=True)


st.write("The **NΦ** Image Compressor is a user-friendly tool designed to reduce the file size of images without compromising their quality. It provides a simple and intuitive interface for users to compress their images quickly and efficiently.The application supports various image formats such as JPEG, PNG, and GIF, ensuring compatibility with a wide range of image files.")

st.markdown("<a style='color:brown; font-style:italic; font-size:25px;' href='/Image_Resizer' target='_self'>Image Resizer</a>", unsafe_allow_html=True)

st.write('The **NΦ** Image Resizer is a powerful tool designed to resize images effortlessly. It provides a user-friendly interface that allows users to resize their images to specific dimensions or scale them proportionally while maintaining the image aspect ratio.Upon accessing the application, users are greeted with an intuitive interface that enables them to easily upload their images for resizing. The application supports various image formats, including JPEG, PNG, and GIF, ensuring compatibility with a wide range of image files.')

st.markdown("<a style='color:brown; font-style:italic; font-size:25px;' href='/PDF_Compressor' target='_self'>PDF Compressor</a>", unsafe_allow_html=True)

st.write("The **NΦ** PDF Compressor is a user-friendly tool designed to reduce the file size of PDF documents without compromising their content or quality. It provides a convenient and efficient way for users to compress PDF files, making them more manageable for storage, sharing, and online distribution.\n *Once the PDF document is uploaded, the application processes the file using advanced compression algorithms specifically designed for PDF files. These algorithms analyze the document's structure and content to identify opportunities for reducing file size while preserving the integrity of the document.*")