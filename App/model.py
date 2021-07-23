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
import random
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
    catalog = {'SongsPlays': None,  'VariablesMap': None, 'UniqueSongs': None, 'UniqueAuthors': None  }

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



def playStructure(play):

    dict = {"track_id": play["track_id"],
            "artist_id": play["artist_id"],
            "instrumentalness": play["instrumentalness"],
            "liveness": play["liveness"],
            "speechiness": play["speechiness"],
            "danceability": play["danceability"],
            "valence": play["valence"],
            "loudness": play["loudness"],
            "tempo": play["tempo"],
            "acousticness": play["acousticness"],
            "energy": play["energy"]
            }

    return dict

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


def Req1(catalog, cat1, lo1, hi1, cat2, lo2, hi2): 
    dict = catalog['VariablesMap']
    UArtists = mp.newMap(maptype='PROBING')

    entry = dict.get(cat1)

    if entry is not None:

        binaryMap = entry['binary']

        lst_lst = om.values(binaryMap, lo1, hi1)

        cant = 0

        for pair in lt.iterator(lst_lst):

            lst = pair['lstsongs']

            for ele in lt.iterator(lst):

                cat2E = round(float(ele[cat2]), 2)

                if cat2E >= lo2 and cat2E <= hi2:
                    cant += 1

                    if mp.contains(UArtists, ele['artist_id']) is False:

                        mp.put(UArtists, ele['artist_id'], ele['track_id'])

        size = mp.size(UArtists)

        return size, cant


def getReq2(catalog, limLive, limSpeech):
    trackList = lt.newList("ARRAY_LIST")
    trackHash = mp.newMap(maptype="PROBING")
    tree = catalog['VariablesMap']['speechiness']['binary']
    nodeList = om.values(tree, limSpeech[0], limSpeech[1])
    for node in lt.iterator(nodeList):
        for event in lt.iterator(node['lstsongs']):
            liveness = float(event['liveness'])
            if (limLive[0] <= liveness) and (liveness <= limLive[1]):
                if not mp.contains(trackHash, event['track_id']):
                    entry = newReq2Entry(event)
                    mp.put(trackHash, event['track_id'],entry)
    trackSize = mp.size(trackHash)
    trackList1 = mp.valueSet(trackHash)
    n = 0
    posList = []
    cond = True
    while cond:
        rng = random.randint(1, trackSize)
        if rng not in posList:
            posList.append(rng)
            trackEvent = lt.getElement(trackList1, rng )
            lt.addLast(trackList, trackEvent)
            n +=1
            if n == 8 or n == (trackSize):
                cond = False
    retorno = {"trackSize": trackSize, "trackList":trackList}
    
    return retorno


def newReq2Entry(event):
    track_id = event['track_id']
    liveness = event['liveness']
    speechness = event['speechiness']
    entry = {'track_id':track_id, 'liveness':liveness, 'speechness': speechness}
    return entry


def Req3(catalog, loVal, hiVal, loTempo, hiTempo):

    dict = catalog['VariablesMap']
    USongs = mp.newMap(maptype='PROBING')
    lstSongs = lt.newList('ARRAY_LIST')

    binaryMap = dict['valence']['binary']

    lst_lst = om.values(binaryMap, loVal, hiVal)

    

    for pair in lt.iterator(lst_lst):

        lst = pair['lstsongs']

        for ele in lt.iterator(lst):

            valR = round(float(ele['tempo']), 2)

            if valR >= loTempo and valR <= hiTempo:

                song = ValenceTempo(ele)

                if mp.contains(USongs, ele['track_id']) is False:

                    mp.put(USongs, ele['track_id'], ele['track_id'])

                    if lt.size(lstSongs) < 8:
                        lt.addLast(lstSongs, song)

            

    size = mp.size(USongs)

    return lstSongs, size


def ValenceTempo(play):

    dict = {'track_id':None, 'valence': None, 'tempo': None}
    dict['track_id'] = play['track_id']
    dict['valence'] = play['valence']
    dict['tempo'] = play['tempo']
    return dict


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
