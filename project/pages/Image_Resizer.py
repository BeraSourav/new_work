import streamlit as st
from pathlib import Path
import tempfile
from PIL import Image
temp_dir  = tempfile.mkdtemp()


st.header("Image Resizer")

file_img1 = st.file_uploader("Upload Image file" , type=['jpeg','png','jpg','gif'])
if file_img1 is not None:
    image1 = Image.open(file_img1)
    name1 = file_img1.name
    st.image(image1 , width = 100, caption=f"{name1}")
    st.write(f"Height = {image1.size[1]} px and Width  = {image1.size[0]} px")
    new_height = st.slider("Select Height in pixels", min_value = 10,max_value=image1.size[1])
    new_width = st.slider("Select Width in pixels", min_value = 10,max_value=image1.size[0])
    #some important function
    def correct_size(image1,width,height):
        resized_image = image1.resize((width,height))
        return resized_image

    temp_f_path = temp_dir + f"/{name1.split('.')[0]}compress.{name1.split('.')[1]}"
    resize = correct_size(image1,new_width,new_height)
    resize.save(temp_f_path)
    st.download_button(
        label = "download resize image" ,
        data = open(temp_f_path,'rb').read(),
        file_name = f"NΦResizer-{name1.split('.')[0]}.{name1.split('.')[1]}",
        mime='image'
    )