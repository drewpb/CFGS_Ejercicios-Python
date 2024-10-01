#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:   ANDRÉS R. PHILIPPS BENÍTEZ                     Octubre/2021
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: CONVERTIDOR A LIBRAS, CHELINES,              Versión Python:   3.10
//                 CORONAS Y PENIQUES   VERSIÓN:                                          
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

def calculo_divisas(peniques):
    libra = (peniques/12)/20
    chelin = peniques/12
    corona = peniques/5
    return libra, chelin, corona

#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:    
    print("""
    --- CONVERTIDOR DE PENIQUES A LIBRAS, CHELINES, CORONAS ---
     """)
    while True:      
        cant_peniq = int(input("Escriba la cantidad de peniques: "))
        libra, chelin, corona = calculo_divisas(cant_peniq)
        print(f"""{cant_peniq} peniques equivale a:
        - {libra} LIBRAS
        - {chelin} CHELINES
        - {corona} CORONAS
        """)

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")
except:
    print("error inesperado")
finally:
    """
    CERRAMOS RECURSOS ABIERTOS
    """
