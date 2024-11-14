# estadisticas.py
def media(datos):
    return sum(datos) / len (datos)

def mediana(datos):
    datos_ord = sorted(datos)
    n = len(datos_ord)
    med = n // 2
    if n % 2 == 0:
        return ((datos_ord[med-1] + datos_ord[med + 1] / 2.0))
    else:
        return(datos_ord[med])
        