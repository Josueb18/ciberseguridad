#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from matematicas_modulos import suma_modulo,resta_modulo,multiplicacion_modulo,division_modulo,potencia_modulo,raiz_modulo


seleccion=int(input("selecciona una operacion: 1.suma 2.resta 3.multiplicacion 4.division 5.potencia 6.raiz"))

if seleccion==1:
    
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
    print("el resultado de la suma es:",suma(num1, num2))
elif seleccion==2:
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
    print("el resultado de la resta es:",resta(num1, num2))

elif seleccion==3:
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
    print("el resultado de la multiplicacion es:",multiplicacion(num1, num2))
    
elif seleccion==4:
    
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
    print("el resultado de la division es:",division(num1, num2))
    
    
elif seleccion==5:
    
    num1=int(input("primer numero el que quieres que se eleve: "))
    num2=int(input("segundo numero por el que quieres elevarlo: "))
    print("el resultado de la potencia es:",potencia(num1, num2))
    
elif seleccion==6:
    
    num1=int(input("A que numero le quieres sacar su raiz: "))
    print("el resultado de la raiz cuadrada de:",num1," es: ",raiz(num1))
    


# In[ ]:




