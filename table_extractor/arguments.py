from os import getcwd
from argparse import ArgumentParser

DEFAULT_PATH = getcwd()
DEFAULT_FORMAT = 'csv'

def make_arguments() -> ArgumentParser:
    """
    Retorna los argumentos necesarios para la logica de extraccion.
    
    Parsing:
    --web -> Pagina web de donde se extrae la tabla
    --format [Opcional] -> Define el formato del archivo generado ['csv', 'xlsx']
    --path [Opcional] -> Define el directorio destino del archivo generado
    """

    # Parser de argumentos
    parser = ArgumentParser(
        prog = 'table-extractor',
        description = 'Esta es una herramienta cli demo para extraer tablas de wikipedia',
    )

    # Argumento --web
    parser.add_argument(
        '--web',
        nargs = 1,
        type = str,
        required = True,
    )

    # Argumento --format
    parser.add_argument(
        '--format',
        nargs = 1,
        default = [DEFAULT_FORMAT],
        type = str,
        choices = ['csv', 'xlsx'],
        required = False,
    )

    # Argumento --path
    parser.add_argument(
        '--path',
        nargs = 1,
        default = [DEFAULT_PATH],
        type = str,
        required = False,
    )

    return parser