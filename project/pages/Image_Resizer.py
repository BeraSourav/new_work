import streamlit as st
from pathlib import Path
import tempfile
from PIL import Image
temp_dir  = tempfile.mkdtemp()


st.header("Image Resizer")

file_img = st.file_uploader("Upload Image" , type=['jpeg','png','jpg','gif'])
if file_img is not None:
    image = Image.open(file_img)
    name = file_img.name
    st.image(image , width = 100, caption=f"{name}")
    st.write(f"Height = {image.size[1]} px and Width  = {image.size[0]} px")
    new_height = st.slider("Select Height in pixels", min_value = 10,max_value=image.size[1])
    new_width = st.slider("Select Width in pixels", min_value = 10,max_value=image.size[0])
    #some important function
    def correct_size(image,width,height):
        resized_image = image.resize((width,height))
        return resized_image

    temp_f_path = temp_dir + f"/{name.split('.')[0]}compress.{name.split('.')[1]}"
    resize = correct_size(image,new_width,new_height)
    resize.save(temp_f_path)
    st.download_button(
        label = "download resize image" ,
        data = open(temp_f_path,'rb').read(),
        file_name = f"NΦResizer-{name.split('.')[0]}.{name.split('.')[1]}",
        mime='image'
    )