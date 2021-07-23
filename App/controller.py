"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import tracemalloc
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog():
    """
    Llama la función de inicialización del catalogo del modelo
    """
    catalog = model.NewCatalog()
    return catalog

def loadData(catalog): 

    songsfile = cf.data_dir + 'Small/context_content_features-small.csv'
    input_file = csv.DictReader(open(songsfile, encoding="utf-8"),
                                delimiter=",")
    model.addBinaryVariable(catalog)
    model.addGenreMap(catalog)
    i=0
    for song in input_file: 

        structure = model.playStructure(song)
        model.addSong(catalog, structure)
        porcentaje = (i/4966703)*100
        i += 1
        print(round(porcentaje,3))
    return catalog




# Funciones para la carga de datos


def addNewGenre(catalog, genre, lim):
    
    model.addNewGenre(catalog, genre, lim)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def primeraEntrega(catalog):
    
    return model.primeraEntrega(catalog)

def Req1(catalog, cat1, lo1, hi1, cat2, lo2, hi2):



    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    result = model.Req1(catalog, cat1, lo1, hi1, cat2, lo2, hi2)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return result, delta_time, delta_memory


def getReq2(catalog, limLive, limSpeech):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    retorno = model.getReq2(catalog, limLive, limSpeech)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return retorno, delta_time, delta_memory


def Req3(catalog, loVal, hiVal, loTempo, hiTempo):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    result = model.Req3(catalog, loVal, hiVal, loTempo, hiTempo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return result, delta_time, delta_memory

def getReq4(catalog, genreList):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    retorno = model.getReq4(catalog, genreList)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return retorno, delta_time, delta_memory

# Funciones para medir tiempo y memoria


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

