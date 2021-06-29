import pytube
import os
from pytube.cli import on_progress

'''
#se necesita instalar pytube con 
pip install pytube 
python -m pip install --upgrade pytube
o con
pip install pytube==10.8.2
'''

url = str(input('ingresar url de la lista de reproducción: '))
#url= 'https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU' #Ejemplo solamente
opcion = str(input('Elija Resolución de los videos para descarga escribiendo número: 1(básica) | 2(la más alta que encuentre) |cualquier otra tecla para salir: '))
if opcion not in ['1','2',1,2]:
    print('No se ingresa resolución dentro de las alternativas 1 o 2, se sale del programa.')
    os._exit(0)
try:
    playlist= pytube.Playlist(url)
    my_routes = os.path.dirname(os.path.realpath(__file__))
    carpeta= playlist.title
    route =  my_routes+"/"+carpeta
    try:
        os.mkdir(my_routes+"/"+carpeta)    
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
        if opcion in [1,'1']: #Resolución estandard
            stream = yt.streams.first()
        else:
            stream = yt.streams.get_highest_resolution() #Resolución máxima
        finished = stream.download(route)
        print('OK video {} de {}'.format(contador,len(playlist.video_urls)))
        contador +=1

    ### Otra forma ###
    '''
    for video in playlist.videos:
        print(video.streams)
        strim =video.streams.first().download(route)
    '''

    print('Finalizado')
    ###### ANTIGUOS METODOS, DAN ERRORES AHORA ###
    #playlist.download_all(route) # da error---

except Exception as e:
    print('Hubo un error: {}'.format(e))

