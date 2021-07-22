﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp 
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Crear catalogo")
    print("2- Cargar información al catalogo")
    print("3- (Primera entrega) Mostrar información del arbol usado como indice")
    print("4- (Primer Requerimiento) Encontrar reproducciones según rango de dos caracteristicas de contenido")
    print("5- (Segundo Requerimiento) Encontrar música según rango de Liveness y Speechness")
    print("6- (Tercer Requerimiento) Encontrar música según rango de Valencia y Tempo")
    print("7- (Cuarto Requerimiento) Encontrar canciones a partir del género musical")
    print("0- Salir")

catalog = None


def printInformaciónCarga(catalog):
    eventos_size = lt.size(catalog['SongsPlays'])
    canciones_size = mp.size(catalog['UniqueSongs'])
    autores_size = mp.size(catalog['UniqueAuthors'])
    sub_list1 = lt.subList(catalog['SongsPlays'], 1, 5)
    sub_list2 = lt.subList(catalog['SongsPlays'], (eventos_size-5), 5)
    
    print("El Total de registros de eventos de escucha cargados son: " + str(eventos_size))
    print("El total de artistas unicos cargados es de: " + str(autores_size))
    print("El total de pistas de audio unicas cargadas es de: "+ str(canciones_size))
    print("los primeros 5 eventos de escucha cargados: ")
    print('********************')
    for evento in lt.iterator(sub_list1):
        print(evento)
        print('********************')
    print("\nLos últimos 5 eventos de escucha cargados: ")
    print('********************')
    for evento in lt.iterator(sub_list2):
        print(evento)
        print('********************')


def printPrimeraEntrega(lst):
    for entry in lt.iterator(lst):
        print("Arbol Indice de la caracteristica: "+ entry["variable"])
        print("Numero de elementos del arbol: " + str(entry["size"]) + " Altura del Arbol: " + str(entry["height"]))


def printReq1(tuple): 


    size = tuple[0]
    plays = tuple[1]

    print('Total of reproduction: ' + str(size))
    print('Total of unique artists: ' + str(plays))


def printReq3(tuple): 

    size = tuple[1]
    print('Total of unique tracks in events: ' + str(size))
    lst = tuple[0]
    l = 1
    for s in lt.iterator(lst): 
        track = s['track_id']
        val = s['valence']
        tem = s['tempo']

        print('Track ' + str(l) + ': ' + str(track) + ' with valence ' + str(val) + ' and tempo of ' + str(tem))

        l += 1


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Creando el catalogo ....")
        
        catalog = controller.initCatalog()

        print("Catalogo ha sido creado")
    elif int(inputs[0]) == 2:
        print("Cargando información al catalogo")
        
        controller.loadData(catalog)
        print("La información se ha cargado al catalogo de manera exitosa")
        
        printInformaciónCarga(catalog)

    elif int(inputs[0]) == 3:

        cat1 = input("Ingrese la característica de contenido 1: ").strip().lower()
        lo1 = round(float(input("Ingrese rango inferior (categoría 1): ")), 2)
        hi1 = round(float(input("Ingrese rango superior (categoría 1): ")), 2)
        print("\n")
        cat2 = input("Ingrese la característica de contenido 2: ").strip().lower()
        lo2 = round(float(input("Ingrese rango inferior (categoría 2): ")), 2)
        hi2 = round(float(input("Ingrese rango superior (categoría 2): ")), 2)

        Req1 = controller.Req1(catalog, cat1, lo1, hi1, cat2, lo2, hi2)

        print("\n")
        print(cat1.title() + ' is between ' + str(lo1) + ' and ' + str(hi1) +
              ' and ' + cat2.title() + ' is between ' + str(lo2) + ' and ' + str(hi2))

        printReq1(Req1[0])
        print("\n")
        print("Tiempo [ms]: ", f"{Req1[1]:.3f}", "    ||  ", "Memoria [kB]: ", f"{Req1[2]:.3f}")
        print("\n")

    elif int(inputs[0]) == 6:

        loVal = round(float(input("Ingrese el rango inferior para la valencia: ")), 2)
        hiVal = round(float(input("Ingrese el rango superior para la valencia: ")), 2)
        print("\n")
        loTempo = round(float(input("Ingrese el rango inferior para el Tempo: ")), 2)
        hiTempo = round(float(input("Ingrese el rango superior para el Tempo: ")), 2)

        print('Valence is between ' + str(loVal)+ ' and ' + str(hiVal))
        print('Tempo is between ' + str(loTempo) + ' and ' + str(hiTempo))

        Req3 = controller.Req3(catalog, loVal, hiVal, loTempo, hiTempo)
        printReq3(Req3[0])
        print("\n")
        print("Tiempo [ms]: ", f"{Req3[1]:.3f}", "    ||  ", "Memoria [kB]: ", f"{Req3[2]:.3f}")
        print("\n")

    elif int(inputs[0]) == 9: 

        lst_primeraEntrega = controller.primeraEntrega(catalog)
        printPrimeraEntrega(lst_primeraEntrega)

    else:
        sys.exit(0)
sys.exit(0)
