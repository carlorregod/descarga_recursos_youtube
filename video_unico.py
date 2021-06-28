import os
import pytube
'''
#se necesita instalar pytube con 
pip install pytube 
python -m pip install --upgrade pytube
o con
pip install pytube==10.8.2
'''
url = str(input('ingresar url del video: '))
#url= 'https://www.youtube.com/watch?v=qk-GWtcdQek'
try:
    yt = pytube.YouTube(url)
    my_routes = os.path.dirname(os.path.realpath(__file__))
    print(f'Se descargará en: {my_routes}')
    print(f"Titulo .........: {yt.title}")
    print(f"Duracion (seg)..: {yt.length}")
    print(f"Descripcion.....: {yt.description}")
    stream = yt.streams.first()
    finished = stream.download(my_routes)
    print('Finalizado')
except Exception as e:
    print(f'Huno un error: {e}')
