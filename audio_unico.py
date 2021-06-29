import os
import pytube
from pytube.cli import on_progress
'''
#se necesita instalar pytube con 
pip install pytube 
python -m pip install --upgrade pytube
o con
pip install pytube==10.8.2
'''
url = str|(input('ingresar url de la canción: '))
#url= 'https://www.youtube.com/watch?v=qk-GWtcdQek' #Ejemplo solamente
try:
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    my_routes = os.path.dirname(os.path.realpath(__file__))
    print(f'Se descargará en: {my_routes}')
    print(f"Titulo .........: {yt.title}")
    print(f"Duracion (seg)..: {yt.length}")
    print(f"Descripcion.....: {yt.description}")
    t = yt.streams.filter(only_audio=True).all()
    t[0].download(my_routes)
    print('Finalizado')
except Exception as e:
    print(f'Huno un error: {e}')
