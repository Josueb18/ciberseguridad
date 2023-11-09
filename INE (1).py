#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Nombre = input("Ingresa tu nombre: ")
Apellidopa = input("Ingresa tu apellido paterno: ")
Apellidoma = input("Ingresa tu apellido materno: ")
Domicilio = input("Ingresa tu domicilio: ")
Clave_lector = input("Ingresa tu clave de elector:")
Curp = input("Ingresa tu curp:")
Fecha_nac = input("Ingresa tu fecha de nacimiento")


datosdeine = {
    "Nombre": Nombre,
    "Apellido Paterno": Apellidopa,
    "Apellido Materno": Apellidoma,
    "Domicilio": Domicilio,
    "Clave LECTOR": Clave_lector,
    "Curp": Curp,
    "Fecha de nacimiento": Fecha_nac
}


with open('datos.txt', 'w') as archivo:
    for clave, valor in datosdeine.items():
        archivo.write(f"{clave}: {valor}\n")


archivo = open("datos.txt","r")

contenido = archivo.read()
print(contenido)


# In[ ]:





# In[ ]:




