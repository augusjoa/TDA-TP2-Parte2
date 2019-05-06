import sys
import os
from visitante import Visitante

DURACION_MINIMA = 40
DURACION_MAXIMA = 120
SOSPECHOSOS_MINIMO = 5
SOSPECHOSOS_MAXIMO = 10

ARG_ERR = 'Uso:\nsospechosos.py <plantilla de entrada>'


def insertar_salidas_ordenadas(salidas, visitante):
    """Inserta de manera ordenada las salidas de los visitantes"""
    i = 0
    j = len(salidas)
    while i < j:
        medio = (i + j) // 2
        if visitante.get_salida() < salidas[medio].get_salida():
            j = medio
        else:
            i = medio + 1
    salidas.insert(i, visitante)


def cargaDeArchivos(archivo):
    entradas = []
    salidas = []
    with open(archivo, 'r') as arch:
        for linea in arch:
            nombre, entrada, permanencia = linea.rstrip("\n").split(",")
            visitante = Visitante(nombre, entrada, permanencia)
            # suponemos con la plantilla de visitantes esta ordenada
            entradas.append(visitante)
            insertar_salidas_ordenadas(salidas, visitante)
    return entradas, salidas


def guardar_sospechosos(visitas, duracion_robo, archivo):
    aux = ''
    with open(archivo, 'a') as arch:
        for visitante in visitas:
            aux += visitante.get_nombre() + ','
        arch.write("{}{}\n".format(aux, duracion_robo))


def detectar_sospechosos(entradas, salidas, archivo="sospechosos.txt"):
    """Detecta grupos de sospechosos dada una lista de entrada ordenada y
    una de salida ordenada del recinto"""
    if os.path.isfile(archivo):
        os.remove(archivo)

    visitas = []
    contador_entrada = 0
    contador_salida = 0
    entrada_len = len(entradas)
    salida_len = len(salidas)
    for _ in range(entrada_len + salida_len):
        if entrada_len > contador_entrada and (
                salida_len < contador_salida or
                entradas[contador_entrada].get_entrada() <=
                salidas[contador_salida].get_salida()):
            visitas.append(entradas[contador_entrada])
            contador_entrada += 1

        else:
            visitante = salidas[contador_salida]
            duracion_robo = visitante.get_salida() - visitas[0].get_entrada()
            if (DURACION_MINIMA <= duracion_robo <= DURACION_MAXIMA) and (
                    SOSPECHOSOS_MINIMO <= len(visitas) <= SOSPECHOSOS_MAXIMO):
                guardar_sospechosos(visitas, duracion_robo, archivo)
            visitas.remove(visitante)
            contador_salida += 1


def main():
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        entradas, salidas = cargaDeArchivos(archivo)
        detectar_sospechosos(entradas, salidas)
    else:
        print(ARG_ERR)


if __name__ == '__main__':
    main()
