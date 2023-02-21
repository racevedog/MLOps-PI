# `ML Ops Streaming`

# Modelo de ML-recomendación usando la librería scikit-surprise y aplicando un filtro colaborativo y 
# los archivos que se generaron previamente en el proceso de preprocesamiento de datos. 

#from fastapi import FastAPI, Query
import sys
import numpy as np
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
import gradio as gr

#app = FastAPI()

#@app.get("/rtu/")
def rec_tit_user(user_id, title_id):
    """
    Responde si un título es recomendado o no para un usuario en particular de acuerdo al modelo de ML-surprise.
    
    Parameters
    ----------
    user_id : int
        Identificador del usuario.
    title_id : string
        Identificador del título de streaming.

    Returns
    -------
    string
        'Se recomienda' , 'No se recomienda'.
    """
    # Carga el archivo de plataformas, títulos y puntuaciones
    dat_types = {'userId' : 'int64',
                 'score' : 'float64'}
    #df_p = pd.read_csv(r'D:\Henry\Repo\PP\datasets\titles\join\platforms_titles_ratings_surp.csv', dtype=dat_types)
    df_p = pd.read_csv('platforms_titles_ratings_surp.csv', dtype=dat_types)

    # Carga el archivo de títulos
    #df_t = pd.read_csv(r'D:\Henry\Repo\PP\datasets\titles\join\titles_surp.csv')
    df_t = pd.read_csv('titles_surp.csv')

    reader = Reader()

    # Lleva el dataset al formato requerido por la librería surprise
    N_filas = 100000
    data = Dataset.load_from_df(df_p[['userId', 'id', 'score']][:N_filas], reader)

    # Separa los datos
    trainset, testset = train_test_split(data, train_size=.25)

    # Usa un modelo de Singular Value Decomposition
    from surprise import SVD
    model = SVD()

    # Entrena el modelo
    model.fit(trainset)

    # Predice
    predictions = model.test(testset)

    # Recomendaciones al usuario
    rec_usuario = df_t.iloc[:4499].copy()

    rec_usuario['Estimate_Score'] = rec_usuario['id'].apply(lambda x: model.predict(user_id, x).est)
    rec_usuario = rec_usuario.sort_values('Estimate_Score', ascending=False)

    if (len(rec_usuario[(rec_usuario['id'] == title_id)])):
        return('Se recomienda.')
    #    return {'Resultado' : 'Se recomienda.'}
    else:
    #    return {'Resultado' : 'No se recomienda.'}
        return('No se recomienda.')
    

# Despliegue en Gradio.

demo = gr.Interface(fn=rec_tit_user, inputs=["text", "text"], outputs="text")

demo.launch()