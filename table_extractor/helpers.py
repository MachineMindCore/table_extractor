import os 

def get_last_directory(url: str) -> str:
    """
    Retorna el ultimo directorio de una direccion o url.

    Argumentos:
    url -> URL o direccion a reducir
    """
    pieces = url.split('/')
    if pieces[-1] == '':
        pieces.pop(-1)
    
    return pieces[-1]

def make_dir(base: str, dir: str):
    """
    Genera un directorio en una direccion base.

    Argumentos:
    base -> Direccion base del directorio a crear
    dir -> Nombre del directorio nuevo
    """
    os.mkdir(f'{base}/{dir}')