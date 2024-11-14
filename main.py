# Proyecto: Compras Electrodomesticos
# Estudiante: Andres Morales Jimenez
# Fecha de Inicio: 2024/11/13
# Fecha de Entrega: 2024/11/13
# Descripción: Este proyecto controla las compras de electrodomesticos.
# Version 0.0

from analisis_datos import *

#Generar una lista de compras aleatoria y escribir esta lista en un archivo
lista_compras = generar_lista_compras()
guardar_lista_compras(lista_compras)
precios = [precio for _, precio in lista_compras]
media = media(precios)
mediana = mediana(precios)
print(f"Media de precios: ¢{media:.2f}")
print(f"Mediana de precios: ¢{mediana:.2f}")