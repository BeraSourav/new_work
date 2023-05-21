import streamlit as st
from pylovepdf.ilovepdf import ILovePdf
import tempfile
from pathlib import Path
import os
import shutil

st.header("PDF Compressor")

temp_dir  = tempfile.mkdtemp()

public_key = 'project_public_3be8d16c4a5fc054f33790a01b480b8f_KNyQc1c1966cf15acd9e6c6ce1dfc75a73b2a'

ilovepdf = ILovePdf(public_key , verify_ssl=True)

task = ilovepdf.new_task('compress')
file = st.file_uploader("Upload PDF File" , type='pdf')

if file is not None:
    pdf_name = file.name
    temp_file_path = os.path.join(temp_dir , pdf_name)
    with open(temp_file_path, 'wb') as temp_file:
        shutil.copyfileobj(file, temp_file)
    st.write(f"Original PDF size : {round(file.size / (1024*1024) , 4)} MB")
    task.add_file(temp_file_path)
    task.set_output_folder(temp_dir+"/hello")
    task.execute()
    task.download()
    

    compress_pdf_path = os.listdir(temp_dir+"/hello")
    file_name = compress_pdf_path[0]  # Get the first element from the list
    file_name = file_name.strip("[]")  # Remove the square brackets from the string
    file_path_after_compression = Path(f'{temp_dir+"/hello"}/{file_name}')

    st.write(f"Compressed PDF size : {round(file_path_after_compression.stat().st_size / (1024*1024) ,4)} MB")

    st.download_button(
        label = "download",
        data = open(file_path_after_compression,'rb').read(),
        file_name=f'NΦCompressed-{pdf_name}.pdf',
        mime='pdf'
    )
    
   



    task.delete_current_task()