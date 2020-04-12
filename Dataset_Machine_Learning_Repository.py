# -*- coding: utf-8 -*-
__author__ = 'davlop@uoc.edu'
__author__ = 'alendinez@uoc.edu'

from bs4 import BeautifulSoup
from pandas import DataFrame
import requests
import robotparser
import unicodedata

# URL base de la que realizaremos la extracción de los datos
URL_BASE = "http://archive.ics.uci.edu/ml/datasets.php"
# Numero máximo de paginas
MAX_PAGES = 13

# Inicializamos los datos
name = []
datatype = []
defaulttask = []
attributes = []
instances = []
numberatributes = []
year = []


# Comprobamos el fichero robots.txt
rp = robotparser.RobotFileParser()
rp.set_url("http://archive.ics.uci.edu/robots.txt")
rp.read()


# Si devuelve True si el agente de usuario puede obtener la URL de acuerdo con las reglas contenidas en el robots.txt archivo analizado .
resultadoFicheroRobots = rp.can_fetch("*", URL_BASE)
if (resultadoFicheroRobots == True):
    # Realizamos la petición a la web
    # se modifica el user-agent predeterminado para evitar bloqueos por default
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    print(URL_BASE)
    req = requests.get(URL_BASE, headers=headers)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "lxml")
        tabla = html.find_all("table")

        print("Empezamos")
        i=0
        #print(tabla[5])
        tabla = tabla[5]

        tabla = tabla.find_all("tr")

        for c in tabla:
            if(i % 2):
                print (str(i)+ ":")
                elementos = c.find_all(class_='normal')
                name.append(unicodedata.normalize("NFKD",elementos[0].text))
                datatype.append(unicodedata.normalize("NFKD",elementos[1].text))
                defaulttask.append(unicodedata.normalize("NFKD",elementos[2].text))
                attributes.append(unicodedata.normalize("NFKD",elementos[3].text))
                instances.append(unicodedata.normalize("NFKD",elementos[4].text))
                numberatributes.append(unicodedata.normalize("NFKD",elementos[5].text))
                year.append(unicodedata.normalize("NFKD",elementos[6].text))
            i = i + 1
    else:
        print ("La pagina no está disponible")
else:
    print ("No se puede obtener la información")
# Si extraemos los datos de manera correcta generamos el csv
if ((name != []) or (datatype != []) or (defaulttask != []) or (attributes != []) or (instances != []) or (numberatributes != []) or (year != [])):
    # Guardamos los datos recogidos en el dataset.csv
    datosCarreras = {'Nombre': name, 'Tipo de dato': datatype, 'Default Task': defaulttask, 'Atributos': attributes, 'Instancias': instances,'Numero de atributos': numberatributes, 'Año': year,}
    df = DataFrame(datosCarreras, columns=['Nombre', 'Tipo de dato','Default Task', 'Atributos', 'Instancias', 'Numero de atributos'])
    export_csv = df.to_csv(r'C:\Users\Repositorio_Dataset_UCI.csv', encoding='utf-8', index=None, header=True)
  #  print (df)
#else:
#    print ("Fallo al extraer la información de la web")
