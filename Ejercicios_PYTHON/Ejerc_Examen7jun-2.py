#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:   ANDRÉS R. PHILIPPS BENÍTEZ                     Octubre/2021
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:  CÁLCULO RECTÁNGULO                VERSIÓN:              
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

def calculo_rectangulo(a, b):
    per = 2*(a+b)
    area = a*b 
    diag = (a**2 + b**2)**0.5
    return per, area, diag

#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:       
    print("""
    --- CÁLCULO DE DATOS DE UN RECTÁNGULO ---
    """)
    while True:
        x = float(input("Escriba la anchura del rectángulo: "))          
        y = float(input("Escriba la altura del rectángulo: "))
        if (x<0.1 or y<0.1):
            print(""" 
            ¡SÓLO NÚMEROS POSITIVOS (>= 1)!
            """)
        else:
            p, a, d = calculo_rectangulo(x, y)
            print(f"""
            - Área del rectángulo: {round(a, 2)}
            - Perímetro del rectángulo: {round(p, 2)}
            - Diagonal del rectángulo: {round(d, 3)}
            """)

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")
except:
    print("error inesperado")
finally:
    """
    CERRAMOS RECURSOS ABIERTOS
    """
