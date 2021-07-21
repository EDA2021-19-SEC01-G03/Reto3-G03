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
    catalog['UniqueAuthors'] = lt.newList('ARRAY_LIST', cmpfunction= compareArtistid)

    return catalog

# Funciones para agregar informacion al catalogo

def addBinaryVariable(catalog):
    
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
        
    #Add in index

    lst_key = mp.keySet(catalog['VariablesMap'])


    for key in lt.iterator(lst_key): 
        pair = mp.get(catalog['VariablesMap'], key)
        omap = me.getValue(pair)

        updateVariableIndex(omap, song, key)

def updateVariableIndex(map, song, variable):

    valorbinary = song[variable]

    entry = om.get(map, valorbinary)

    if entry is None: 
        varentry = newVarEntry(valorbinary, song)
        om.put(map, valorbinary, varentry)
    else: 
        varentry = me.getValue(entry)

    addVariableIndex(varentry, song)

    return map

def addVariableIndex(varentry, song): 
    lst = varentry['lstsongs']
    lt.addLast(lst, song)


def newVarEntry(value, song): 

    entry = {'value':'', 'lstsongs': None}
    entry['value'] = value
    entry['lstsongs'] = lt.newList('ARRAY_LIST')
    return entry


def newVariable(variable_name): 

    elem = {'variable': '', 'binary':None }

    elem['variable'] = variable_name
    elem['binary'] = om.newMap(omaptype='RBT', comparefunction= compareContentValues)

    return elem


# Funciones para creacion de datos

# Funciones de consulta

def primeraEntrega(catalog):
    hashtable = catalog["VariablesMap"]
    keys = mp.keySet(hashtable)
    retorno = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keys):
        pair = mp.get(hashtable, key)
        tree = me.getValue(pair)['binary']
        tree_size = om.size(tree)
        tree_height = om.height(tree)
        list_entry = {"variable": key, "size": tree_size, "height": tree_height}
        lt.addLast(retorno, list_entry)
    return retorno

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


def compareArtistid(rep1, rep2):
    """
    Compara el id de artista de dos eventos de reproducciones
    """
    if (rep1["artist_id"] == rep2["artist_id"]):
        return 0
    elif (rep1["artist_id"] > rep2["artist_id"]):
        return 1
    else:
        return -1


def compareTrackid(rep1, rep2):
    """
    Compara el id de cancion de dos eventos de reproduccion
    """
    if (rep1["track_id"] == rep2["track_id"]):
        return 0
    elif (rep1["track_id"] == rep2["track_id"]):
        return 1
    else:
        return -1


# Funciones de ordenamiento
