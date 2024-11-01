import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
from datetime import datetime
from googletrans import Translator
import os
import csv



def leer_archivos_csv(ruta_directorio):
    dataframes = {}
    rutas_relativas = os.listdir(ruta_directorio)[:-1]

    for archivo in rutas_relativas:
                año = archivo.split('-')[1][:4] if '-' in archivo else None
                if año:  
                    df = pd.read_csv(os.path.join(ruta_directorio, archivo), delimiter=';')
                    if año not in dataframes:
                        dataframes[año] = []
                        dataframes[año].append(df)

    return dataframes

ruta_directorio = '../datos'