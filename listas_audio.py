import pytube
import os
import re
from pytube.cli import on_progress

'''
#se necesita instalar pytube con 
pip install pytube 
python -m pip install --upgrade pytube
o con
pip install pytube==10.8.2
'''

#url = str(input('ingresar url de la lista de reproducción de canciones: '))
url= 'https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU'
try:
    playlist= pytube.Playlist(url)
    my_routes = os.path.dirname(os.path.realpath(__file__))
    carpeta= re.sub("[^0-9a-zA-ZáéíóúÁÉÍÓÚ ]","",playlist.title)
    route =  my_routes+"\\"+carpeta if os.name == 'nt' else my_routes+"/"+carpeta
    try:
        os.mkdir(route)    
        print(f'Se descargará en: {route}')
    except Exception as e:
        print(f'Ya existe la ruta: {my_routes+"/"+carpeta}')
    contador =1
    print('Número de videos en lista: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        yt = pytube.YouTube(video_url, on_progress_callback=on_progress)
        print(f"Titulo .........: {yt.title}")
        print(f"Duracion (seg)..: {yt.length}")
        print(f"Descripcion.....: {yt.description}")
        t = yt.streams.filter(only_audio=True).all()
        t[0].download(route)
        print('OK canción {} de {}'.format(contador,len(playlist.video_urls)))
        contador +=1

    ### Otra forma ###
    '''
    for video in playlist.videos:
        print(video.streams)
        strim =video.streams.filter(only_audio=True).all()
        strim[0].download(route)
    '''

    print('Finalizado')
    ###### ANTIGUOS METODOS, DAN ERRORES AHORA ###
    #playlist.download_all(route) # da error---

except Exception as e:
    print('Hubo un error: {}'.format(e))

