import random

def generar_lista_compra():
   electrodomesticos = {
    "refrigerador": 250000,
    "lavadora": 180000,
    "microondas": 75000,
    "televisor": 300000,
    "licuadora": 35000,
    "cafetera": 42000,
    "plancha": 25000,
    "aspiradora": 95000,
    "horno electrico": 105000,
    "ventilador": 20000,
    "secadora": 220000,
    "extractor de jugo": 48000,
    "batidora": 60000,
    "freidora de aire": 85000,
    "parrilla electrica": 70000,
    "lavavajillas": 280000,
    "deshumidificador": 120000,
    "calentador de agua": 65000,
    "maquina de hacer pan": 90000,
    "dispensador de agua": 55000,
    "tostadora": 30000,
    "procesador de alimentos": 110000,
    "humidificador": 45000,
    "radiador electrico": 65000
}
   seleccion = random.sample(list(electrodomesticos.items()),k=5)  #k  Selecciona l acantidad de electrodomesticos aleatorios
   return seleccion



def guardar_lista_compras(lista_compras, nombre_archivo="lista_compras.txt"):
    try:
    # Operaciones con el archivo
        with open(nombre_archivo, 'w') as archivo:
            for producto, precio in lista_compras:
                archivo.write(f"{producto}:{precio}\n")
        print(f"Lista de compras guardada en '{nombre_archivo}'.")
    except Exception as e: # Captura cualquier excepción
        print(f"Error al trabajar con el archivo: {e}")
    finally:
        if archivo:
            archivo.close()