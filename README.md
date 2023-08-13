# table_extractor

Herramienta CLI para extraer tablas de paginas web, en primera instancia se pretendia hacerlo para Wikipedia con la finalidad de completar el requisito del ejercicio, pero funciona para muchas mas paginas web.

# Argumentos

--web: Pagina web a la cual se va a extraer las tablas

--path: Direccion donde se guardara el directorio de la extraccion de tablas

--format: Formato de las tablas extraidas (csv, xlsx)

# Instalacion

Para instalar el paquete primero obtenga el repositorio:

```bash
git clone https://github.com/MachineMindCore/table_extractor
```

Luego instale el paquete:
```bash
pip install -e .
```

# Uso

El paquete se usa desde la terminal con el comando de entrada 'table_extractor':

```bash
table_extractor --web <URL> --path [Optional] <DIR_PATH> --format [Optional] <FORMAT>
```
## Ejemplos

Algunos ejemplos pueden ser encontrados en la carperta 'examples', dichos ejemplos se extrajeron con los comandos:

```bash
table_extractor --web https://es.wikipedia.org/wiki/Anexo:Ganadores_del_Premio_Nobel
table_extractor --web https://es.wikipedia.org/wiki/Anexo:Canales_de_YouTube_m%C3%A1s_vistos
table_extractor --web https://www.xataka.com/moviles/xiaomi-redmi-10-caracteristicas-precio-ficha-tecnica
```