from fastapi import FastAPI, Query
from statistics import mode
import pandas as pd

app = FastAPI()


@app.get("/gcp/")
async def get_count_platform(platform):
    """
    Obtiene el número de títulos por plataforma.
    
    Parameters
    ----------
    platform : string
        Identificador de la plataforma de streaming {'ama','dis','hul','net'}.
    
    Returns
    -------
    int
        Número de títulos de la plataforma
    """
    if platform == 'ama':
        p_id = 'as'
    elif platform == 'dis':
        p_id = 'ds'
    elif platform == 'hul':
        p_id = 'hs'
    else:
        p_id = 'ns'
    df_plat = pd.read_csv('platforms_titles.csv')
    df_plat = df_plat.loc[df_plat['id'].str.contains(p_id)]

    return {'Número de títulos' : len(df_plat)}


@app.get("/gmd/")
async def get_max_duration(platform, duration_type, year : int = Query(gt=1919, lt=2023)):
    """
    Obtiene el título de mayor duración de acuerdo a la plataforma, tipo y año.
    
    Parameters
    ----------
    platform : string
        Identificador de la plataforma de streaming {'ama','dis','hul','net'}..
    duration_type : string
        tipo de duración, {'min', 'season}.
    year : int
        Año de lanzamiento.
    
    Returns
    -------
    str
        Nombre de la película/serie de mayor duración.
    """
    if platform == 'ama':
        p_id = 'as'
    elif platform == 'dis':
        p_id = 'ds'
    elif platform == 'hul':
        p_id = 'hs'
    else:
        p_id = 'ns'
    df_plat = pd.read_csv('platforms_titles.csv')
    df_plat = df_plat.loc[(df_plat['id'].str.contains(p_id)) & 
                          (df_plat['release_year'] == year)  &
                          (df_plat['duration_type'] == duration_type)]
    if len(df_plat) == 0:
        return {'Resp.' : 'No hay títulos para la plataforma-tipo-año solicitados'}
    
    max_dur = df_plat['duration_int'].max()
    df_tit = df_plat.loc[df_plat['duration_int'] == max_dur]
    title = str(df_tit['title'].values[0])

    return {'Titulo de mayor duración' : title}


@app.get("/gsc/")
async def get_score_count(platform, year : int = Query(gt=1919, lt=2023), scored: float = Query(gt=0, lt=5)):
    """
    Obtiene la cantidad de títulos por plataforma con un puntaje mayor a XX en determinado año.
    
    Parameters
    ----------
    platform : string
        Identificador de la plataforma de streaming {'ama','dis','hul','net'}.
    scored : float
        puntaje registrado.
      year : int
        Año de lanzamiento.

    Returns
    -------
    int
        Número de títulos.
    """
    if platform == 'ama':
        p_id = 'as'
    elif platform == 'dis':
        p_id = 'ds'
    elif platform == 'hul':
        p_id = 'hs'
    else:
        p_id = 'ns'
    df_plat = pd.read_csv('platforms_titles_ratings_m.csv')
    df_plat = df_plat[(df_plat['id'].str.contains(p_id)) & 
                      (df_plat['release_year'] == year)  & 
                      (df_plat['score'] > scored)]
    
    return {'Número de títulos' : len(df_plat)}


@app.get("/ga/")
async def get_actor(platform, year : int = Query(gt=1919, lt=2023)):
    """
    Obtiene el actor que más se repite por plataforma y año.
    
    Parameters
    ----------
    platform : string
        Identificador de la plataforma de streaming {'ama','dis','hul','net'}.
    year : int
        Año de lanzamiento.

    Returns
    -------
    string
        Actor que más se repite.
    """
    if platform == 'ama':
        p_id = 'as'
    elif platform == 'dis':
        p_id = 'ds'
    elif platform == 'hul':
        p_id = 'hs'
    else:
        p_id = 'ns'
    df_plat = pd.read_csv('platforms_titles.csv')
    df_plat = df_plat[(df_plat['id'].str.contains(p_id)) & 
                      (df_plat['release_year'] == year)]
    if len(df_plat) == 0:
        return {'Resp.' : 'No hay títulos para la plataforma-año solicitados'}
    
    df_cast = df_plat['cast']
    actors = []
    for i in range(0, len(df_cast)):
        cast_tit = df_cast.iloc[i].split(',')
        for j in range(0, len(cast_tit)):
            actors.append(cast_tit[j].strip())
            
    return {'Actor más repetido' : mode(actors)}
