#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

nombre_archivo = "pruebas.txt"

leer_archivo(nombre_archivo)


# In[ ]:


import PyPDF2

def leer_archivo_pdf(nombre_archivo):
    try:
        with open(nombre_archivo, "rb") as archivo:
            pdf_reader = PyPDF2.PdfReader(archivo)  
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                print(page.extract_text())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

nombre_archivo_pdf = "Aquicomio.pdf"
leer_archivo_pdf(nombre_archivo_pdf)

