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
    x = 1
    for song in input_file: 
        model.addSong(catalog, song)
        x += 1
        print((x /63339)*100)
    return catalog




# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def primeraEntrega(catalog):
    
    return model.primeraEntrega(catalog)
