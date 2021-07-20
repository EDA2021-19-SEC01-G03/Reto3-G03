"""
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
    print("4- (Primer Requerimiento)")
    print("5- (Segundo Requerimiento)")
    print("6- (Tercer Requerimiento)")
    print("7- (Cuarto Requerimiento)")
    print("0- Salir")

catalog = None


def printPrimeraEntrega(lst):
    for entry in lt.iterator(lst):
        print("Arbol Indice de la caracteristica: "+ entry["caracteristica"])
        print("Numero de elementos del arbol: " + entry["size"] + "     Altura del Arbol: " + entry["height"])
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Creando el catalogo ....")

        print("Catalogo ha sido creado")
    elif int(inputs[0]) == 2:
        print("Cargando información al catalogo")

        print("La información se ha cargado al catalogo de manera exitosa")
    elif int(inputs[0]) == 3:
        print("Cargando información del arbol...")
        
        lst_primeraEntrega = controller.primeraEntrega(catalog)
        printPrimeraEntrega(lst_primeraEntrega)
        
    else:
        sys.exit(0)
sys.exit(0)
