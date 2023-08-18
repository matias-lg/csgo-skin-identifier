# Clasificador de imágenes de skins de Counter-Strike: Global Offensive con Deep Learning

Para ejecutar correctamente el Jupyter Notebook, se deben instalar las dependencias del proyecto:
    
```bash
pip install -r requirements.txt
```
De todas formas, estas se instalan al ejecutar el Jupyter Notebook.

El dataset utilizado para el proyecto se encuentra en el siguiente enlace: [https://drive.google.com/file/d/1Hqe8nS2gGVTZELCC5eW-hsHOyWtFULD0/view?usp=drive_link](https://drive.google.com/file/d/1Hqe8nS2gGVTZELCC5eW-hsHOyWtFULD0/view?usp=drive_link), al ejecutar el Jupyter Notebook este se descargará automáticamente.


Si quiere construir su propio dataset, puede utilizar los scripts dentro de la carpeta `dataset_builder`:

```bash
python dataset_builder/search_and_download.py
```
descargará las imágenes de las skins de CS:GO a la carpeta `downloaded_images`, notar que algunas imágenes no serán relevantes para su categoría, por lo que se recomienda revisarlas manualmente, luego:

```bash
python dataset_builder/format_files.py
```
asignará nombres únicos a cada imagen, ajustará su tamaño a 300x300 y generará el archivo `labels.csv` con la etiqueta de cada imagen, estos resultados quedarán en la carpeta `dataset`.