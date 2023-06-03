import streamlit as st
import tempfile
import shutil
import os
from pdf2docx import Converter

import subprocess

# Run the shell command to install libgl1-mesa-dev
subprocess.run(['sudo', 'apt-get', 'install', 'libgl1-mesa-dev'])



st.header("Pdf to Word")

pdf_file = st.file_uploader("Upload pdf file here.." , type='pdf')

temp_dirw  = tempfile.mkdtemp()

if pdf_file:
    if st.button("Convert"):
        pdf_name = pdf_file.name
        temp_file_path_w = os.path.join(temp_dirw , pdf_name)
        with open(temp_file_path_w, 'wb') as temp_file:
            shutil.copyfileobj(pdf_file, temp_file)

        doc_file_path = temp_dirw
        c = Converter(temp_file_path_w)
        c.convert(doc_file_path+ "/sample.docx")
        c.close()

        file_path_after_convert = f'{doc_file_path}' + "/sample.docx"
        name = f'{pdf_name}'.split('.')[0]

        st.download_button(
            label = "download",
            data = open(file_path_after_convert,'rb').read(),
            file_name=f'NΦcoverter-{name}.docx',
            mime='docx'
        )
        temp_file.close()

