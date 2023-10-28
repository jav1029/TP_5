import Modulos.Modulos_TP5
from Modulos import Modulos_TP5
import datetime
import random
import time

Inicio=time.time()

#1)Escriba una función redondear() que permita redondear un número
#  decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#  entero siguiente

# print(Modulos.Modulos_TP5.redondear(1.50))



#2)Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#  módulo que esté fuera de ese paquete, cree una función de suma de
#  decimales que redondee el resultado haciendo uso de la función
#  redondear() del paquete recién creado.

# def Suma_decimales(Dec1,Dec2):
#     return  (Modulos_TP5.redondear(Dec1))+(Modulos_TP5.redondear(Dec2))

# print(Suma_decimales(2.2,3.5))



#3)Usando el módulo datetime, escribe un programa que muestre la fecha
#  y hora actuales del sistema.

# Fecha=datetime.datetime.now()
# print(Fecha)



#4)Escriba un programa que devuelva un número par al azar entre 2 y 10

# for i in range(0,15):
#     Numero=random.randrange(2,11,2)
#     print(Numero)
#     time.sleep(1)


#5)Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#  para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#  ante una pregunta del usuario, la bola responde con una de 8 posibles
#  respuestas

# Respuestas=["Es seguro que si","Las chances son buenas","Puedes contar con ello","Preguntame de nuevo mas tarde","Concetrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
# Valida=False
# while True:
#     Pregunta=input("Haz tu pregunta:")
#     for i in Pregunta:
#         if i == "?":   
#             Valida=True
#     if Valida==True:
#         print(random.choice(Respuestas))
#         break
#     else:    
#         print("No reconozco la pregunta")



#6)Encuentre el tiempo de ejecución de los programas de los ejercicios
#  anteriores

Fin=time.time()
Tiempo= (Fin-Inicio)//1
print(f"El programa a tardado:{Tiempo} seg en ejecutarse")
