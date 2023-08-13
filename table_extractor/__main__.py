from table_extractor.arguments import make_arguments
from table_extractor.extractor import TableExtractor
from table_extractor.helpers import get_last_directory, make_dir

def main():
    # Generar el parser de los argumentos
    parser = make_arguments()

    # Extrae el Namespace del parser donde estan los argumentos
    args = parser.parse_args()

    # Instancia el extractor de tablas
    print('checking compatible browsers')
    table_extractor = TableExtractor()

    # Extrae las tablas encontradas en la url
    print('searching on ', args.web[0])
    tables = table_extractor.extract_tables(args.web[0])
    print('generated tables: ', len(tables))

    # Escribe las tablas en el directorio y formato especificado en args
    directory_name = get_last_directory(args.web[0])
    base = args.path[0]
    make_dir(base, directory_name)
    for i, dataframe in enumerate(tables):
        if args.format[0] == 'csv':
            dataframe.to_csv(f'{base}/{directory_name}/table_{i}.csv', index=False)
        if args.format[0] == 'xlsx':
            dataframe.to_excel(f'{base}/{directory_name}/table_{i}.xlsx', index=False)
    print('saved in', f'{base}/{directory_name}')

if __name__ == '__main__':
    main()