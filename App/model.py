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
    catalog['UniqueSongs'] = lt.newList('ARRAY_LIST')
    catalog['UniqueAuthors'] = lt.newList('ARRAY_LIST')

# Funciones para agregar informacion al catalogo








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
