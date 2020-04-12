# 1. INTRODUCCIÓN
En este repositorio se podrá encontrar un archivo de código Python  Dataset_Machine_Learning_Repository.py que realiza un Web Scrapping de una página web (en este caso, la URL se corresponde con el repositorio de Machine Learning de UCI http://archive.ics.uci.edu/ml/datasets.php).

# 2. FINALIDAD
La creación de un dataset que permita la clasificación y categorización de las bases de datos existentes en el repositorio de UCI.

# 3. FUNCIONAMIENTO DEL CÓDIGO
El código Python permite la recuperación y creación de un dataset en formato CSV. Se utilizan las librerías Python Requests, Pandas y BeautifulSoup. Estas librerías nos permiten realizar la recuperación del contenido web y su posterior extracción del contenido para la creación del dataset. A mayores se comprueba el fichero robots.txt, de la web UCI, para conocer sus restricciones dentro del mismo código. Posteriormente se y se modifica el user-agent predeterminado, empleado en la recuperación del código HTML, para evitar bloqueos.

# 4. REQUISITOS
Para poder ejecutar el script Python es necesario instalar la siguientes librerías:

* Pandas
* Requests
* unicodedata
* beautifulsoup
* robotparser

# 5. MIEMBROS DEL EQUIPO
La actividad ha sido realizada de manera grupal por Alberto Lendínez Gutiérrez y David López de la Fuente.

# 6. LICENCIA
La licencia escogida para la publicación de este proyecto ha sido Released Under CC0: Licencia de Dominio Publico.
