#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:   ANDRÉS R. PHILIPPS BENÍTEZ                     Octubre/2021
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:       CALCULO ÁREAS                VERSIÓN:              
//   Versión Python:   3.10                             
//                
////////////////////////////////////////////////////////////////////////////////////
                     Explicación del programa
////////////////////////////////////////////////////////////////////////////////////
"""
#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
# VARIABLES GLOBALES
#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
# CONFIGURACIÓN PUERTOS GPIO Y RECURSOS A UTILIZAR
#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
# FUNCIONES
#////////////////////////////////////////////////////////////////////////////////////

def areaTriang():
    base = float(input("¿De cuánto es la base?: "))
    alto = float(input("¿Y su altura?: "))
    if (base <= 0 or alto <= 0):
        print("¡SÓLO NÚMEROS POSITIVOS!")
    else:
        area = round(((base*alto)/2), 3)
        print(f"Un triángulo de base {base}(u) y altura {alto}(u) tiene un área de {area}(u^2)")

def areaCirc():
    radio = float(input("Cuánto mide el radio?: "))
    if (radio <= 0):
        print("¡SÓLO NÚMEROS POSITIVOS!")
    else:
        area = round((3.141592*(radio**2)), 3)
        print(f"Un círculo de radio {radio}(u) tiene un área de {area}(u^2)")

#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:
    print("""
    --- CÁLCULOS DE ÁREAS ---
    """)                 
    while True:      #iniciamos un loop infinito
        fig = input("""Elija una figura geométrica:
    a) Triángulo
    b) Círculo

¿Qué figura quiere calcular? |Escriba T o C|  """).upper()
        if (fig == "T"):
            areaTriang()
        elif (fig == "C"):
            areaCirc()
        else:
            print("DEBE PONER UNA - T o C -")
        print()


except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")
except:
    print("error inesperado")
finally:
    """
    CERRAMOS RECURSOS ABIERTOS
    """

