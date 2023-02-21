
# Proyecto Individual ML Ops

Recolección, tratamiento de datos de plataformas de streaming, generación de API de servicios de consulta e implementación de un sistema de recomendación de contenido para usuarios mediante un modelo de Machine Learning.

## Transformaciones

#### Archivos de puntuaciones
Realice la integración de los archivos de puntuaciones `9.csv` y transformación de sus datos como fueron solicitados implementando una función para procesar los que se encuentren en una carpeta determinada.  
Generé el archivo transformado `ratings_fixed.csv`

#### Archivos de plataformas
Realice integración de los archivos de plataformas `xxx-titles.csv` y transformación de sus datos como fueron solicitados implementando una función para este propósito.  
Generé los archivos transformados `platforms_titles_ratings.csv` y `platforms_titles_ratings_m.csv` para uso de las operaciones de consulta de la API.
## API Reference

Con los archivos generados mencionados en el apartado de transformaciones como fuente de datos, generé las funciones de consulta solicitadas `main.py` implementadas mediante el framework `FastAPI`en un repositorio inicialmente para ejecución local, que posteriormente use para desplegarlas en Deta-Space.

url: https://ppfastapi-2-s1897519.deta.app/

#### Get count platform

```http
  GET /gcp/?{platform}
```
Obtiene la cantidad de títulos por plataforma.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `platform`| `string` | **Requerido**. Id de la plataforma. {ama,dis,hul,net} |

#### Get max duration

```http
  GET /gmd/?{platform}&{duration_type}&{year}
```
Obtiene el título con la duración máxima por plataforma y año de lanzamiento.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `platform`      | `string` | **Requerido**. Id de la platforma. {ama,dis,hul,net}  |
| `duration_type` | `string` | **Requerido**. Id del tipo de duración. {min,seasons} |
| `year`          | `int`    | **Requerido**. Año de lanzamiento. {aaaa} |

#### Get score count

```http
  GET /gsc/?{platform}&{year}&{scored}
```

Obtiene el número de títulos por plataforma y año de lanzamiento con el score mayor al indicado.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `platform` | `string` | **Requerido**. Id de la platforma. {ama,dis,hul,net}  |
| `year`     | `int`    | **Requerido**. Año de lanzamiento. {aaaa} |
| `scored`   | `float`  | **Requerido**. Puntaje. {9.9} |

#### Get actor

```http
  GET /ga/?{platform}&{year}
```

Obtiene el actor que más aparece por plataforma y año de lanzamiento.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `platform` | `string` | **Requerido**. Id de la platforma. {ama,dis,hul,net}  |
| `year`     | `int`    | **Requerido**. Año de lanzamiento. {9.9} |


## EDA

#### Archivos de plataformas-puntuaciones
Realice la exploración y preprocesamiento de los datos del archivo resultante `platforms_titles_ratings.csv` de la etapa de transformaciones. 
- identificación y eliminación de duplicados.
- Visualización de valores nulos.
- Eliminación de columnas irrelevantes.
- Imputación de valores faltantes.
## Sistema de recomendación

Realice la selección de los atributos relevantes (usuario, titulo, score) para el modelo de recomendación del archivo resultante `platforms_titles_ratings_f.csv` de la etapa EDA, implementando la librería scikit-surprise.  
Incorporé también el framework Gradio para generar una interfase gráfica para determinar si un título se recomienda o no a un usuario.  
Finalmente desplegué esta aplicación en huggingface para acceder a ella desde internet.

url: https://huggingface.co/spaces/racevedog/PP-recmod

user_id : {99999}  
title_id : {xx9999}
## Autor

- [@racevedog](https://www.github.com/racevedog)


