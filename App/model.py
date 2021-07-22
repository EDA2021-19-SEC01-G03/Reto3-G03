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

    catalog['VariablesMap'] = {}
    catalog['SongsPlays'] = lt.newList('ARRAY_LIST')
    catalog['UniqueSongs'] = mp.newMap(maptype='PROBING')
    catalog['UniqueAuthors'] = mp.newMap(maptype='PROBING')
    catalog['GenreMap'] = mp.newMap(maptype= 'PROBING')
    
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
        
        value = newVariable(name)
        catalog['VariablesMap'][name] = value


def addSong(catalog, song): 

    #Add song

    lt.addLast(catalog['SongsPlays'], song)

    #Add unique song. 

    if not mp.contains(catalog['UniqueSongs'], song['track_id']):
        mp.put(catalog['UniqueSongs'],song['track_id'],song)

    #Add author

    if not mp.contains(catalog['UniqueAuthors'], song['artist_id']):
        mp.put(catalog['UniqueAuthors'],song['artist_id'], song)
        
    #Add in index

    lst_key = catalog['VariablesMap'].keys()


    for key in lst_key:
        omap = (catalog['VariablesMap'].get(key))['binary']
        updateVariableIndex(omap, song, key)

def updateVariableIndex(map, song, variable):

    valorbinary = round(float(song[variable]),3)

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


def addGenreMap(catalog):
    map = catalog['GenreMap']
    mp.put(map, 'Reggae', [60,90])
    mp.put(map, 'Down-tempo', [70,100])
    mp.put(map, 'Chill-out', [90,120])
    mp.put(map, 'Hip-hop', [85,115])
    mp.put(map, 'Jazz and Funk', [120,125])
    mp.put(map, 'Pop', [100,130])
    mp.put(map, 'R&B', [60,80])
    mp.put(map, 'Rock', [110,140])
    mp.put(map, 'Metal', [100,160])


def addNewGenre(catalog, genre, lim):
    map = catalog['GenreMap']
    mp.put(map, genre, lim)
# Funciones para creacion de datos

# Funciones de consulta

def primeraEntrega(catalog):
    diccionario = catalog["VariablesMap"]
    keys = diccionario.keys()
    print(keys)
    retorno = lt.newList("ARRAY_LIST")
    for key in keys:
        tree = diccionario.get(key)['binary']
        tree_size = om.size(tree)
        tree_height = om.height(tree)
        list_entry = {"variable": key, "size": tree_size, "height": tree_height}
        lt.addLast(retorno, list_entry)
    return retorno


def getReq4(catalog, genreList):
    tree = catalog['VariablesMap']['tempo']['binary']
    hasht = catalog['GenreMap']
    cont = 0
    entryList = lt.newList('ARRAY_LIST')
    for genre in lt.iterator(genreList):
        entry = Req4Iterator(tree,hasht, genre)
        cont += entry['eventSize']
        lt.addLast(entryList, entry)
    return cont, entryList


def getGenreBPM(hasht, genre):
    genrepair = mp.get(hasht, genre)
    if genrepair:
        lim = me.getValue(genrepair)
        return lim
    else:
        print('error')
        return None


def Req4Iterator(tree, hasht, genre):
    lim = getGenreBPM(hasht, genre)
    nodeList = om.values(tree, lim[0], lim[1])
    eventCont = 0
    artistList = lt.newList('ARRAY_LIST')
    artistCont = 0
    artistHash = mp.newMap(maptype='PROBING')
    for node in lt.iterator(nodeList):
        for event in lt.iterator(node['lstsongs']):
            eventCont +=1
            if not mp.contains(artistHash, event['artist_id']):
                mp.put(artistHash, event['artist_id'],1)
                if artistCont != 10:
                    lt.addLast(artistList, event['artist_id'])
                    artistCont += 1
    artistSize = mp.size(artistHash)
    retorno = newReq4Entry(genre,eventCont, artistSize, artistList)
    return retorno


def newReq4Entry(genre, eventCont, artistSize, artistList):
    retorno = {}
    retorno['genre'] = genre
    retorno['eventSize'] = eventCont
    retorno['artistSize'] = artistSize
    retorno['artistList'] = artistList
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
    if (rep1 == rep2):
        return 0
    elif (rep1 > rep2):
        return 1
    else:
        return -1


def compareTrackid(rep1, rep2):
    """
    Compara el id de cancion de dos eventos de reproduccion
    """
    if (rep1 == rep2):
        return 0
    elif (rep1 == rep2):
        return 1
    else:
        return -1


# Funciones de ordenamiento
