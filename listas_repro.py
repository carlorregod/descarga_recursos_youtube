import pytube
import os

'''
#se necesita instalar pytube con 
pip install pytube 
python -m pip install --upgrade pytube
o con
pip install pytube==10.8.2
'''

url = str(input('ingresar url de la lista de reproducción: '))
#url= 'https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU'
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
        yt = pytube.YouTube(video_url)
        print(f"Titulo .........: {yt.title}")
        print(f"Duracion (seg)..: {yt.length}")
        print(f"Descripcion.....: {yt.description}")
        stream = yt.streams.first()
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

