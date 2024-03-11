# atom-estadillo
El estadillo digital es la aplicación de atom que se utiliza para guardar información sobre los vuelos realizados cuando se hace una inspección. Cada vez que se realiza un vuelo se añade una nueva linea al estadillo del día en curso. Este estadillo es un archivo .csv el cual se puede emplear posteriormente para facilitar el análisis de los vuelos.

La aplicación puede ser utilizada internamente por los pilotos de Aerotools o por personas ajenas a la empresa a las que se subcontrata la realización de vuelos.

Esta carpeta contiene los códigos más actualizados para utilizar el estadillo electrónico. Está organizado con la siguiente estructura:

-atom-estadillo ->  |-estadillo.py
                    |-CSV_baseDatos.py
                    |-CSV_baseDatos ->  |-Empresas.csv
                    |                   |-Pilotos.csv
                    |                   |-...
                    |-atom1.png
                    |-atom.ico
                    |-fecha_estadillo.csv (i.e. 2022_01_27_estadillo.csv)
                    |-pyInstallerManualWeb.txt
                    |
                    |-Otros archivos o carpetas relacionados con github y archivos o carpetas antiguos...
                    |

Esta es la estructura del código python. Empleando PYInstaller se puede crear un ejecutable (.exe) para poderlo ejecutar desde cualquier ordenador sin necesidad de ningún archivo más que los contenidos en la siguiente carpeta:
Dropbox (AEROTOOLS-UAV)/AEROTOOLS-UAV/Software/..AEROTOOLS/Estadillo_Digital/2022_02_23_ejecutable_estadillo_digital

El nombre del ejecutable es 'estadillo.exe'. Para poder ejecutarlo solo es necesario disponer de la carpeta CSV_baseDatos (con su contenido) y las dos imágenes (atom.ico y atom1.png). En cualquier momento se puede crear un nuevo ejecutable siguiendo las instrucciones de la sección 'Sacar el exe usando pyinstaller' descritas al comienzo del archivo 'estadillo.py'.

## estadillo.py
Es el script principal de python de atom-estadillo. Utiliza como base para crear el entorno gráfico la librería 'tkinter'. Por otro lado, utiliza el módulo creado para el estadillo (y el gestor de estadillos) 'CSV_baseDatos.py', que contiene funciones para gestionar las bases de datos de Empresas (y sus trabajos correspondientes) así como la lista de pilotos. La información guardada en ambas bases de datos serán las que se desplieguen al pinchar en los botones desplegables del estadillo. Esos mismos deplegables pueden ser rellenados manualmente y al guardar el csv estadillo se guardará la nueva empresa, trabajo o/y piloto en las bases de datos.

Se puede dividir en las siguientes secciones:

-Variables configuración entorno de visualización
-Lectura datos csv bases de datos
-Crea y customiza los elementos de la raiz / Crea y customiza los elementos del frame
-Inicializa variables
-Funciones
-Imagen Atom
-Crea el estilo para los combobox
-Fuentes
-Variables que no cambian
-Crea las líneas de separación
-Variables que cambian


### Variables configuración entorno de visualización
En esta sección del estadillo se definen los 2 colores base que se emplearán para el fondo de la aplicación (colorGrisFondo) y para los botones de la aplicación (colorGrisBotones).

### Lectura datos csv bases de datos
En esta sección se leen de la base de datos las Empresas (Trabajos) empleando la funcion 'leer_CSV_empresas_trabajos()' y se leen los pilotos empleando la función 'leer_CSV_pilotos()'.

Estás funciones se describen con más detalle en la sección del README.md dedicada al módulo 'CSV_baseDatos.py'.

### Crea y customiza los elementos de la raiz / Crea y customiza los elementos del frame
En estás dos secciones se definen los elementos básicos de la raíz y frame (tkinter).

El elemento más facilmente modificable de esta sección es el icono 'atom.ico'. Que será el que aparezca en la parte superior izquierda y en la barra de tareas al ejecutar el script (estadillo.py) o el ejecutable (estadillo.exe).

### Inicializa variables
En esta sección se inicializan algunas variables que se utilizarán al ejecutar el script.

### Funciones
En esta sección se definen funciones internas al script:

-hora_boton()
-hora_boton_fin()
-fecha_boton()
-reinicio_variables()
-guardar()
-opciones_desplazado()
-elegir_trabajos_empresa()
-desplazamiento_y()
-desplazamiento_x()
-ocultar_mostrar()
-open_csv()

#### hora_boton()
Esta función se emplea para coger la hora actual del ordenador para autorellenar la casilla de 'Hora de inicio'.

#### hora_boton_fin()
Esta función se emplea para coger la hora actual del ordenador para autorellenar la casilla de 'Hora final'.

#### fecha_boton()
Esta función se emplea para coger la fecha actual del ordenador para autorrellenar la casilla de 'Fecha'.

#### reinicio_variables()
Esta función se emplea para reiniciar los valores de aquellos campos que se quieren reiniciar cada vez que se pulsa el botón 'Guardar', algunos campo se dejarán intactos al pulsar este botón para no tener que ser rellenados de nuevo con cada vuelo.

#### guardar()
Es la función que se ejecuta cuando se pulsa el botón 'Guardar'. Lo primero que hace es obtener el path al archivo csv donde se guardará la información del estadillo digital (fecha_estadillo.csv). Actualmente solo tiene implementada 100% la función para guardar los datos del tipo de inspección 'Fotovoltaica'. Una estructura similar se puede aplicar para los otros tipos de inspecciones.

Cuando se ejecuta el script hay unos campos que están marcados en color amarillo, estos campos son de obligado rellenado para que te permita guardar el csv, si no te aprece una ventana emergente indicandote que no se han rellenado todos los parámetros necesarios.

Campos obligatorios fotovoltaica:
-Empresa
-Trabajo
-Piloto
-Equipo de vuelo
-Fecha
-Tipo de trabajo
-Pitch
-Tipologia de planta
-PB (PowerBlock)
-Vuelo
-Set Bat (Set de Baterías)
-Volt inicial (Voltaje al iniciar el vuelo)
-Hora de inicio ()
-Desplazado (el desplazamiento que se aplica en el vuelo cuando se inspecciona una cierta hilera de placas fotovoltaicas)
-Alt. Vuelo (Altura de vuelo)
-Vel. vuelo (Velocidad de vuelo)
-Termica (casilla para señalar que se han realizado las imágenes térmicas)
-RGB (casilla para señalar que se han realizado las imágenes RGB)
-Hora final

En caso de que la casilla 'Vuelo abortado' sea marcada, no será necesario que estén marcados los anteriores campos.

Campos obligatorios agricultura:
-Empresa
-Trabajo
-Piloto
-Equipo de vuelo
-Fecha
-Tipo de trabajo
-Vuelo
-Set Bat (Set de Baterías)
-Volt inicial (Voltaje al iniciar el vuelo)
-Hora de inicio ()
-Alt. Vuelo (Altura de vuelo)
-Vel. vuelo (Velocidad de vuelo)
-RGB (casilla para señalar que se han realizado las imágenes RGB)
-MULTY (Multy1 y Multy2)
-GB Antes Vuelo
-GB Después Vuelo 
-Hora final

En caso de que la casilla 'Vuelo abortado' sea marcada, no será necesario que estén marcados los anteriores campos.

Campos obligatorios eólica y otros:
-Empresa
-Trabajo
-Piloto
-Equipo de vuelo
-Fecha
-Tipo de trabajo
-Vuelo
-Set Bat (Set de Baterías)
-Volt inicial (Voltaje al iniciar el vuelo)
-Hora de inicio ()
-Alt. Vuelo (Altura de vuelo)
-Vel. vuelo (Velocidad de vuelo)
-RGB (casilla para señalar que se han realizado las imágenes RGB)
-Hora final

En caso de que la casilla 'Vuelo abortado' sea marcada, no será necesario que estén marcados los anteriores campos.

A continuación genera un dataframe de pandas en el que se guardan los campos rellenados, cambia los puntos por comas para algunos de los campos (voltaje inicial, voltaje final y pitch) y finalmente guarda ese dataframe en el csv_estadillo.

Finalmente chequea si la empresa, trabajo y pilotos indicados ya están en la lista actual de la base de datos. Si no lo están los agrega empleando las funciones 'guardar_CSV_empresas_trabajos()' y 'guardar_CSV_pilotos'.

Finalmente llama a la función 'reinicio_variables()'.

La sección 'Conexión con base de datos' está pensada para la comunicación con una base de datos en línea, no está aun implementado.

#### opciones_desplazado()
Esta función selecciona en base a la tipología de planta fotovoltaica seleccionada (Fijo, Seguidores N-S o Seguidores polares) las opciones que se van a mostrar en el menú desplegable de 'Desplazado'.

#### elegir_trabajos_empresa()
Esta función selecciona los trabajos a mostrar en el desplegable 'Trabajo' en función de la empresa seleccionada en el desplegable de 'Empresa'.

#### desplazamiento_y() y desplazamiento_x()
Estas funciones seleccionan el desplazamiento que se va a guardar en la base de datos en línea (aún no implementado). NO SE USAN ACTUALMENTE.

#### ocultar_mostrar()
Esta función es llamada cuando se selecciona el 'Tipo de trabajo' y muestra las casillas correspondientes a este tipo de trabajo, ocultando las casillas que no se corresponden con el trabajo.

#### open_csv()
Esta función es llamada cuando se pulsa el botón 'CSV'. Este botón abre el archivo de estadillo.csv creado hasta el momento, si no se ha guardado ningún vuelo todavía no muestra nada. Se puede implementar un try: except: para que muestre una ventana emergente indicando que no hay todavía un estadillo.csv creado.

### Imagen Atom
En esta sección se definen las propiedades de la imagen que se muestra como logo de empresa cuando se abre el estadillo. La imagen utilizada actualmente es la imagen 'atom1.png'.

### Crea el estilo para los combobox
Esta sección define el estilo de combobox (tkinter) que se emplea en la interfaz gráfica.

### Fuentes
Define las dos fuentes de texto que se emplean en la interfaz gráfica.

'fontStyle' se emplea para los textos de los label que acompañan a cada uno de los campos a rellenar.
'font_boton' se emplea para los textos de los botones.

### Variables que no cambian
En esta sección se definen algunas variables (generalmente no utilizadas), así como los distintos elementos de interacción con la interfaz gráfica que una vez escrito o seleccionado el valor que se desea, no serán reseteados cuando se escriban los datos en el estadillo.csv. Estos campos son los siguientes:

-Empresa
-Trabajo
-Fecha
-Pitch
-Piloto
-Equipo de vuelo
-Tipologia de la planta
-Tipo de trabajo

Para definir a que se corresponde cada elemento, se le acompaña un label. Los campos que requieren de unidades, estás son indicadas en el label (i.e. [m]). El codigo esta escrito de tal modo que la definición del label y del campo a rellenar están adyacentes.

### Crea las líneas de separación
En esta sección se crean las 2 líneas de separación que demarcan las 3 zonas de trabajo del estadillo (datos generales, datos al inicio del vuelo y datos al finalizar el vuelo).

### Variables que cambian
En esta sección se definen algunas variables (generalmente no utilizadas), así como los distintos elementos de interacción con la interfaz gráfica que una vez escrito o seleccionado el valor que se desea,  serán reseteados cuando se escriban los datos en el estadillo.csv. Este reseteo se hace al finalizar el proceso de la función 'guardar()', empleando la función 'reinicio_variables()' Estos campos son los siguientes:

-Térmica
-RGB
-MULTY (Multy1 y Multy2)
-CSV (este botón en realidad no tiene un campo a rellenar, es un boton de interacción únicamente)
-Hora de inicio
-Hora final
-Zona volada
-PB (PowerBlock)
-Vuelo
-Desplazado
-Vel. vuelo [m/s]
-Alt. Vuelo [m]
-Vel. de aire [km/h]
-Temp. aire [°C]
-Nubes [Octas]
-Radiacion [W/m^2]
-Tiempo vuelo [s]
-Dist. recorrida [m]
-Set Bat (set de baterias)
-Volt inicial [V]
-Volt final [V]
-GB Antes Vuelo (Gigabytes en la tarjeta SD antes de comenzar el vuelo)
-GB Después Vuelo (Gigabytes en la tarjeta SD despues de terminar el vuelo)
-Anotaciones
-Vuelo abortado
-Guardar (este botón en realidad no tiene un campo a rellenar, es un botón de interacción únicamente)

### Anotaciones importantes
En esta sección se define un texto en la aprte inferior de la ventana que nos indica que los campos sombreados en color amarillo deberán ser rellenados para poder guardar los datos en el CSV.

## CSV_baseDatos.py
Este módulo está compuesto por funciones que sirven para recolectar información de los cvs bases de datos o para guardar información en ellos. Las 4 funciones presentes en este módulo son:

-leer_CSV_empresas_trabajos()
-guardar_CSV_empresas_trabajos()
-leer_CSV_pilotos()
-guardar_CSV_pilotos()

Las 2 primeras funciones interactúyan con el csv de las empresas (trabajos). Son funciones básicas que se explican por si mismas al ser leídas (junto a sus comentarios).

## CSV_baseDatos
Esta carpeta contiene los 2 csv bases de datos donde se guarda la información de empresas (trabajos) y pilotos que se emplean en el estadillo. Los dos archivos que tiene son:

-Empresas.csv
-Pilotos.csv

Estos dos documentos pueden ser modificados de manera manual con un editor de texto para introducir nuevos campos. Otra forma de introducir nuevos campos es directamente empleando la aplicación, esta detecta cuando se han rellenado una empresa, trabajo y/o piloto diferentes a los ya presentes en la base de datos y los añade. Es importante recordar que la aplicación a día de hoy no es capaz de reconocer nombres parecidos, 'Azuer1' es diferente a 'azuer 1'. En este caso los guardaría como 2 trabajos diferentes.

### Empresas.csv
La estructura general de este csv es la siguiente:

Empresa;Trabajo1;Trabajo2;Trabajo3;Trabajo4;TrabajoN
Cobra;Bonete2;Bonete3;Bonete4
Ingeteam;Alarcos;Alcores;Childers;LaCartuja;Perogordo;Poblete;SanPedro1;SanPedro4;SusanRiver;Talarrubias2
Metka;Azuer1;Azuer2;Talasol
TCI-GECOMP;LaCabrita

La primera línea es un cabecero indicando que son los distintos campos. En las líneas posteriores el primer campo se corresponde con la empresa, mientras que los siguientes campos se corresponden con los diferentes trabajos realizados para la empresa.

### Pilotos.csv
La estructura general de este csv es la siguiente:

Alberto Cristobal
Oscar Alvarez
Operador Extranjero
Foreing Operator
Miguel Rosa

Donde cada línea del csv se coresponde con un piloto.

## atom1.png
Es la imagen empleada como logo de empresa cuando se abre el estadillo. Es la imagen que aparece en la parte superior central de la app cuando se ejecuta.

## atom.ico
Este es el icono que será el que aparezca en la parte superior izquierda y en la barra de tareas al ejecutar el script (estadillo.py) o el ejecutable (estadillo.exe).

## fecha_estadillo.csv (i.e. 2022_01_27_estadillo.csv)
Las columnas del estadillo digital son las siguientes:

-Empresa
-Trabajo
-Fecha
-Piloto
-Equipo_de_vuelo
-Pitch
-Hora_de_inicio
-Hora_final
-PB
-Vuelo
-Desplazado
-Vel_vuelo
-Alt_vuelo
-Vel_de_aire
-Temp_aire
-Nubes
-Radiacion
-Tiempo_vuelo
-Dist_Recorrida
-Set_Bat_1
-Set_Bat_2
-Set_Bat_3
-Volt_inicial
-Volt_final
-GB1/
-GB2/
-Anotaciones
-Termica
-RGB
-Cali_Ini
-Cali_Final
-Tipologia
-Vuelo_abortado

## pyInstallerManualWeb.txt
Archivo que contiene 2 enlaces web de interés a la hora de utilizar la herramienta pyinstaller.

## Otros archivos o carpetas relacionados con github y archivos o carpetas antiguos...


