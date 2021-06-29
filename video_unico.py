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

url = str(input('ingresar url del video: '))
#url= 'https://www.youtube.com/watch?v=qk-GWtcdQek' #Ejemplo solamente
opcion = str(input('Elija Resolución escribiendo número: 1(básica) | 2(la más alta que encuentre) |cualquier otra tecla para salir: '))
if opcion not in ['1','2',1,2]:
    print('No se ingresa resolución dentro de las alternativas 1 o 2, se sale del programa.')
    os._exit(0)
try:
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    my_routes = os.path.dirname(os.path.realpath(__file__))
    print(f'Se descargará en: {my_routes}')
    print(f"Titulo .........: {yt.title}")
    print(f"Duracion (seg)..: {yt.length}")
    print(f"Descripcion.....: {yt.description}")
    if opcion in [1,'1']: #Resolucióne standard
        stream = yt.streams.first()
    else:
        stream = yt.streams.get_highest_resolution()
    finished = stream.download(my_routes)
    print('Finalizado')
except Exception as e:
    print(f'Huno un error: {e}')
