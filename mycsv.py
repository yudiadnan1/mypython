import streamlit as st
import pandas as pd
import numpy as np
from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

st.title('Hitung Perkalian')

panjang = st.number_input("Masukkan nilai Panjang", 0)
lebar = st.number_input("Masukkan nilai Lebar", 0)
tinggi = st.number_input("Masukkan nilai Tinggi", 0)
hitung = st.button("Hitung")

if hitung:
    hasil = panjang * lebar * tinggi
    #st.write("Hasil nya adalah: ", hasil)
    st.success(f"Volume hasil adalah {hasil}")
    st.balloons()
    row_contents = [32,'Shaun','Java','Tokyo','Morning']
    append_list_as_row('students.csv', row_contents)


