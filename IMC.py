#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calcular_el_imc():
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
 
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("Estas en la categoria tas flaco")
    elif 18.5 <= imc < 25:
        print("Estas en la categoría 'tas bien'")
    elif 25 <= imc < 30:
        print("Estas en la categoria 'tas gordo'")
    else:
        print("Estas en la categoria 'Fat boy'")

calcular_el_imc()


# In[ ]:





# In[ ]:




