﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def NewCatalog():
    catalog = { 'SongsPlays': None,  'VariablesMap': None, 'UniqueSongs': None, 'UniqueAuthors': None  }

    catalog['VariablesMap'] = mp.newMap(17, maptype='PROBING', loadfactor=0.8)
    catalog['SongsPlays'] = lt.newList('ARRAY_LIST')
    catalog['UniqueSongs'] = lt.newList('ARRAY_LIST', cmpfunction= compareTrackid)
    catalog['UniqueAuthors'] = lt.newList('ARRAY_LIST', cmpfunction= compareArtistid )

    return catalog

# Funciones para agregar informacion al catalogo


def addSong(catalog, song): 

    #Add song

    lt.addLast(catalog['SongsPlays'], song)

    #Add unique song

    present = lt.isPresent(song['track_id'])
    if present == 0 : 
        lt.addLast(catalog['UniqueSongs'], song)

    #Add author

    present = lt.isPresent(song['artist_id'])
    if present == 0 : 
        lt.addLast(catalog['UniqueAuthors'], song)

def addBinaryVariable(catalog, key):
    
    variables = lt.newList('ARRAY_LIST')
    lt.addLast(variables, 'instrumentalness')
    lt.addLast(variables, "liveness")
    lt.addLast(variables, "speechiness")
    lt.addLast(variables, "danceability")
    lt.addLast(variables, "valence")
    lt.addLast(variables, "loudness")
    lt.addLast(variables, "tempo")
    lt.addLast(variables, "acousticness")
    lt.addLast(variables, "energy")

    for name in lt.iterator(variables): 

        key = name
        value = newVariable(name)
        mp.put(catalog['VariablesMap'], key, value)



def newVariable(variable_name): 

    elem = {'variable': '', 'binary':None }

    elem['variable'] = variable_name
    elem['binary'] = om.newMap(omaptype='RBT', comparefunction= compareContentValues)

    return elem


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def compareContentValues(value1, value2):
    """
    Compara dos valores de contenido
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1


# Funciones de ordenamiento
