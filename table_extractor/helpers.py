import os 
import unicodedata
import re

def get_last_directory(url: str) -> str:
    """
    Retorna el ultimo directorio de una direccion o url.

    Argumentos:
    url -> URL o direccion a reducir
    """
    pieces = url.split('/')
    if pieces[-1] == '':
        pieces.pop(-1)

    normalized_name = unicodedata.normalize('NFKD', pieces[-1])
    normalized_name = re.sub(r'[^a-zA-Z0-9 ]', '', normalized_name)
    normalized_name = normalized_name.replace(' ', '_')
    normalized_name = normalized_name.lower()
    
    return normalized_name

def make_dir(base: str, dir: str):
    """
    Genera un directorio en una direccion base.

    Argumentos:
    base -> Direccion base del directorio a crear
    dir -> Nombre del directorio nuevo
    """
    name = f'{base}/{dir}'
    if not os.path.exists(name):
        os.mkdir(name)