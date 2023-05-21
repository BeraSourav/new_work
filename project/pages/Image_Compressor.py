import streamlit as st
from pathlib import Path
import tempfile
from PIL import Image
st.header("Image compressor")
temp_dir  = tempfile.mkdtemp()


file_img = st.file_uploader("Upload Image" , type=['jpeg','png','jpg','gif'])
if file_img is not None:
    image = Image.open(file_img)
    name = file_img.name
    st.image(image , width = 100, caption=f"{name}")
    qual_img = st.slider("Compress Percentage (%)", min_value=0, max_value=95)
    temp_f_path = temp_dir + f"/{name.split('.')[0]}compress.{name.split('.')[1]}"
    st.write(f"image size = {round(file_img.size / (1024*1024) , 3)} MB")
    image.save(temp_f_path , optimize=True,quality= qual_img)
    file_size1 = Path(temp_f_path).stat().st_size
    st.write(f"compressed image size = {round(file_size1 / (1024*1024) , 3)} MB" )
    st.download_button(
                label = "download compreess image" ,
                data = open(temp_f_path,'rb').read(),
                file_name = f"NΦCompressor-{name.split('.')[0]}.{name.split('.')[1]}",
                mime='image'
            )
    tempfile.close()
