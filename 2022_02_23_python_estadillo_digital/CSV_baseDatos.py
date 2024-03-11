import csv
import os

def leer_CSV_empresas_trabajos():

    # Path al csv de las empresas 
    path_csv_empresas = os.path.join(os.getcwd(),'CSV_baseDatos\Empresas.csv')

    # Abrimos el CSV con las empresas
    with open(path_csv_empresas,'r') as csv_file:
        # Leemos el CSV con las empresas
        csv_reader = csv.reader(csv_file, delimiter=';')

        empresas_read = []# creamos una lista vacia donde guardar las empresas
        trabajos_read = []# creamos una lista vacia donde guardar los trabajos de cada empresa

        # Saltamos el encabezado
        next(csv_reader, None)  

        # Cada fila del CSV es una empresa diferente
        for empresa in csv_reader:
            empresas_read.append(empresa[0]) # El primer campo es la empresa
            trabajos_read.append(empresa[1:]) # Los siguientes campo son los trabajos de cada empresa

    return empresas_read, trabajos_read

def guardar_CSV_empresas_trabajos(lista_empresas,matriz_trabajos):

    # Path al csv de las empresas  
    path_csv_empresas = os.path.join(os.getcwd(),'CSV_baseDatos\Empresas.csv')

    # Abrimos el CSV con las empresas
    with open(path_csv_empresas,'w') as csv_file:

        # Escribimos el encabezado
        csv_file.write('Empresa;Trabajo1;Trabajo2;Trabajo3;Trabajo4;TrabajoN\n')

        contador = 1 # Contador para chequear cuantas empresas se han guardado, en la última no hay que añadir salto de línea

        # Bucle recorriendo todas las empresas de la lista
        for indice_empresa, empresa in enumerate(lista_empresas):

            # Unimos todos los trabajos separados por ';'
            trabajos = ';'.join(matriz_trabajos[indice_empresa])
            # Generamos la linea a escribir uniendo la empresa y los trabajos separados por ';'
            lineaCSV = ';'.join([empresa,trabajos])

            # Si no es la ultima empresa de la lista escribimos un salto de linea
            if contador < len(lista_empresas):
                # Escribimos en el csv la linea 
                csv_file.write(lineaCSV+'\n')
            # Si es la última empresa de la lista NO escribimos el salto de linea
            else:
                # Escribimos en el csv la linea
                csv_file.write(lineaCSV)

            contador += 1

        # # create the csv writer
        # writer = csv.writer(csv_file)

        # for empresa in lista_empresas:
        #     # write a row to the csv file
        #     writer.writerow(empresa)

def leer_CSV_pilotos():

    # Path al csv de las empresas 
    path_csv_pilotos = os.path.join(os.getcwd(),'CSV_baseDatos\Pilotos.csv')

    # Abrimos el CSV con las empresas
    with open(path_csv_pilotos,'r') as csv_file:
        # Leemos el CSV con las empresas
        csv_reader = csv.reader(csv_file, delimiter=';')

        pilotos_read = []# creamos una lista vacia donde guardar los pilotos

        # Cada fila del CSV es un piloto diferente
        for piloto in csv_reader:
            #print(piloto)
            pilotos_read.append(piloto[0]) # El primer campo es el piloto

    return pilotos_read

def guardar_CSV_pilotos(lista_pilotos):

    # Path al csv de las empresas  
    path_csv_pilotos = os.path.join(os.getcwd(),'CSV_baseDatos\Pilotos.csv')

    # Abrimos el CSV con las empresas
    with open(path_csv_pilotos,'w') as csv_file:

        contador = 1 # Contador para chequear cuantos pilotos se han guardado, en el última no hay que añadir salto de línea
        for piloto in lista_pilotos:

            # Si no es la última empresa de la lista escribimos un salto de línea
            if contador < len(lista_pilotos):
                csv_file.write(piloto+'\n')
            # Si es la última empresa de la lista NO escribimos el salto de línea
            else:
                csv_file.write(piloto)

            contador += 1