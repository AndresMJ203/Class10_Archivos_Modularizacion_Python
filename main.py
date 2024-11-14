# Proyecto: Compras Electrodomesticos
# Estudiante: Andres Morales Jimenez
# Fecha de Inicio: 2024/11/13
# Fecha de Entrega: 2024/11/13
# Descripción: Este proyecto controla las compras de electrodomesticos.
# Version 0.0

from analisis_datos.carga_datos import generar_lista_compra , guardar_lista_compras

lista_compras = generar_lista_compra()
guardar_lista_compras(lista_compras)

precios = [precio for _, precio in lista_compras]
print(lista_compras)
print(precios)