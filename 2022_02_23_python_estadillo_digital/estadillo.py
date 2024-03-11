import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk,Image

import pandas as pd
import os
import time
import webbrowser

# Modulo para lectura csv bases de datos
from CSV_baseDatos import leer_CSV_empresas_trabajos, guardar_CSV_empresas_trabajos, leer_CSV_pilotos, guardar_CSV_pilotos

#Paquete para la conexion con la base de datos (PostGreSQL)
#from sqlalchemy import create_engine

#-------------------- Links interesantes sobre pyinstaller --------------------
# Enlace web al manual de pyinstaller
# https://pyinstaller.readthedocs.io/en/stable/

# Enlace web using PYInstaller
# https://pyinstaller.readthedocs.io/en/stable/usage.html#options



#-------------------- Sacar el exe usando pyinstaller 
# Estas instrucciones están pensadas empleando la terminal, se deberá estar dentro del directorio donde está contenido el script del que se quiere ssacar el .exe
#
# OPCION 0:
# pyinstaller yourProgram.py
# Esto genera una carpeta 'dist' que contiene otra carpeta nombrada con el nombre del programa .py 'yourProgram'.
# En esa carpeta esta contenido todo, incluido el ejecutable .exe con unas carpetas y ficheros asociados a él.
# La imagen 'atom1.png' hay que moverla manualmente dentro de la carpeta donde esta situadoo el .exe, pyinstaller no lo hace
#
# OPCION 1:
# Ejecutando: pyinstaller --onefile -w --icon=miicono.ico yourProgram.py . Se crea una carpeta dist, que contiene un ejecutable con toda la información.
# - La opción --onefile hace que se genere un solo archivo ejecutable exe. 
# - La opción -w hace que no se abra una consola terminal al ejecutar el .exe
# - La opción --icon=miicono.ico hace que al ejecutable se le ponga de icono la imagen 'miicono.ico'
# - yourProgram.py es el programa de python del que quieres crear el archivo ejecutable.
#
# OPCION 2:
# Ejecutando: pyinstaller -w --icon=miicono.ico --add-data mydata.png;. --ad-data mydata.ico;. yourProgram.py . Esto genera una carpeta 'dist' que contiene 
#otra carpeta nombrada con el nombre del programa .py 'yourProgram'. En esa carpeta esta contenido todo, incluido el ejecutable .exe con unas carpetas 
# y ficheros asociados a él.
# - La opción -w hace que no se abra una consola terminal al ejecutar el .exe
# - La opción --icon=miicono.ico hace que al ejecutable se le ponga de icono la imagen 'miicono.ico'
# - La opción --add-data mydata.png;. añade a la carpeta 'yourProgram' la imagen mydata.png
# - La opción --add-data mydata.ico;. añade a la carpeta 'yourProgram' la imagen mydata.ico
# - yourProgram.py es el programa de python del que quieres crear el archivo ejecutable.
#
# Ejemplo practico: pyinstaller --onefile -w --icon=atom.ico estadillo.py
#
# ----COSAS A HACER ANTES DE EJECUTAR EL .EXE OBTENIDO SI UTILIZAS LA OPCION 1----
# Para que el programa funcione, hay que mover manualmente a la carpeta dist la imagen atom1.png y el icono atom.ico.
#Tambien se debe mover la carpeta CSV_baseDatos a la carpeta dist.
# ----  ----
#
#Original #pyinstaller -w Estadillo_app.pyw

#------------- Variables configuración entorno de visualización

colorGrisFondo = '#A7A7A7' #A7A7A7 es la notación hex del color rgb (167, 167, 167) [Gris]
colorGrisBotones = '#C1C1C1' #C1C1C1 es la notación hex del color rgb (193, 193, 193) [Gris claro]

#------------- Lectura datos csv bases de datos
# Leemos el csv de las empresas y sus respectivos trabajos

opciones_empresa, matriz_opciones_trabajos = leer_CSV_empresas_trabajos() 
#print('opciones de empresa es: ',opciones_empresa)

# Leemos el csv de los pilotos
opciones_piloto = leer_CSV_pilotos()

#------------- Crea y customiza los elementos de la raiz ------------

raiz=Tk()
raiz.title("Estadillo")
raiz.resizable(1,1) #Ancho, alto; true lo puedes cambiar, false no
raiz.iconbitmap('atom.ico') # Añadimos un icono para que salga en la esquina izquierda superior y en la barra de tareas cuando se ejecuta la aplicación.
raiz.geometry("850x650") #ancho y alto
raiz.state('zoomed')
raiz.config(bg="blue")  #cambia el color de fondo

#--------------- Crea y customiza los elementos del frame ------------

miFrame=Frame(raiz) #crea lo de dentro de la raiz
miFrame.pack(fill="both",expand=True) #se redimensiona entero
miFrame.config(bg=colorGrisFondo) #cambia el color del frame. 
#miFrame.config(bg='#F9711E') #cambia el color del frame. #F9711E es la notación hex del color rgb (249, 113, 30) [Naranja]
#miFrame.config(bg="tomato") #cambia el color del frame
miFrame.config(width="950", height = "400")
miFrame.config(bd=35) #cuanto borde le das

#-----------------Inicializa variables

# Variables para guardas lista de empresas
lista_empresa = []
lista_empresa_unicos = []

# Variables para guardas lista de trabajos
lista_trabajos = []
lista_trabajos_unicos = []

# Variables para guardas lista de pilotos
lista_piloto = []
lista_piloto_unicos = []

global localtime
localtime = time.localtime(time.time())

#-----------------Funciones

def hora_boton():
    localtime = time.localtime(time.time())
    horaEntry.delete(0,'end')

    # --Modificacion--
    hora = str(localtime[3]).zfill(2) #Obtenemos la hora de tal modo que siempre tenga dos digitos
    minutos = str(localtime[4]).zfill(2) #Obtenemos los minutos de tal modo que siempre tenga dos digitos
    segundos = str(localtime[5]).zfill(2) #Obtenemos los segundos de tal modo que siempre tenga dos digitos
    
    # Introducimos en la casilla el valor obtenido
    horaEntry.insert(0,':'.join([hora,minutos,segundos]))
    # --  --

    # Original
    # if localtime[3]<10 and localtime[4]<10 and localtime[5]<10:
    #     horaEntry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[3]<10 and localtime[4]<10:
    #     horaEntry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[3]<10 and localtime[5]<10:
    #     horaEntry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[4]<10 and localtime[5]<10:
    #     horaEntry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[3]<10:
    #     horaEntry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[4]<10:
    #     horaEntry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[5]<10:
    #     horaEntry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # else:
    #     horaEntry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))

def hora_boton_fin():
    localtime = time.localtime(time.time())
    hora_fin_Entry.delete(0,'end')

    # --Modificacion--
    hora = str(localtime[3]).zfill(2) #Obtenemos la hora de tal modo que siempre tenga dos digitos
    minutos = str(localtime[4]).zfill(2) #Obtenemos los minutos de tal modo que siempre tenga dos digitos
    segundos = str(localtime[5]).zfill(2) #Obtenemos los segundos de tal modo que siempre tenga dos digitos
    
    # Introducimos en la casilla el valor obtenido
    hora_fin_Entry.insert(0,':'.join([hora,minutos,segundos]))
    # --  --

    # Original
    # if localtime[3]<10 and localtime[4]<10 and localtime[5]<10:
    #     hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[3]<10 and localtime[4]<10:
    #     hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[3]<10 and localtime[5]<10:
    #     hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[4]<10 and localtime[5]<10:
    #     hora_fin_Entry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # elif localtime[3]<10:
    #     hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[4]<10:
    #     hora_fin_Entry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    # elif localtime[5]<10:
    #     hora_fin_Entry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    # else:
    #     hora_fin_Entry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))

def fecha_boton():
    localtime = time.localtime(time.time())
    fechaEntry.delete(0,'end')

    # --Modificacion--
    anno = str(localtime[0]) #Obtenemos el anno
    mes = str(localtime[1]).zfill(2) #Obtenemos el mes de tal modo que siempre tenga dos digitos
    dia = str(localtime[2]).zfill(2) #Obtenemos el dia de tal modo que siempre tenga dos digitos

    # Introducimos en la casilla el valor obtenido
    fechaEntry.insert(0,':'.join([anno,mes,dia]))
    # --  --

    # Original
    # if localtime[1]<10 and localtime[2]<10:
    #     fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+'0'+str(localtime[2]))
    # elif localtime[2]<10:
    #     fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+'0'+str(localtime[2]))    
    # elif localtime[1]<10:
    #     fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+str(localtime[2]))    
    # else:
    #     fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+str(localtime[2]))
    
def reinicio_variables():
    horaEntry.delete(0,'end')
    hora_fin_Entry.delete(0,'end')
    pbEntry.delete(0,'end')
    vEntry.delete(0,'end')
    distanciaEntry.delete(0,'end')
    tiempoEntry.delete(0,'end')
    voltinicialEntry.delete(0,'end')
    voltfinalEntry.delete(0,'end')
    textoComentario.delete('1.0','end') #Sintaxis para borrar text widgets
    lista_desplegable_desplazado.set('')
    batEntry.delete(0,'end')
    bat2Entry.delete(0,'end')
    bat3Entry.delete(0,'end')
    #rec.set(0)
    termica.set(0) #Termica es la variable para controlar el check button de grabacion de cámara térmica
    RGB.set(0)
    Multy1.set(0)
    Multy2.set(0)
    gb1Entry.delete(0,'end')
    gb2Entry.delete(0,'end')
    vuelo_abortado.set(0)
    
def guardar():

    global opciones_empresa # Hacemos global la variable para poder ser leida de fuera de la funcion
    global opciones_piloto

    # Obtenemos el path al csv del estadillo
    directorio = os.path.join(os.getcwd(),str(fecha.get()).split(':')[0]+'_'+str(fecha.get()).split(':')[1]+'_'+str(fecha.get()).split(':')[2]+'_estadillo.csv')

    if lista_desplegable_tipo_trabajo.get() == 'Fotovoltaica':

        #---------------- Si los siguientes campos no están rellenos no te deja guardar
        if (len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
            and len(hora.get()) != 0 and len(pb.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_desplazado.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0
            and len(bat.get()) != 0 and len(lista_desplegable_tipologia.get())!=0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0
            and termica.get()==1 and RGB.get()==1) or vuelo_abortado.get()==1 :

        # if (len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
        #     and len(hora.get()) != 0 and len(pb.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_desplazado.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0
        #     and len(bat.get()) != 0 and len(lista_desplegable_tipologia.get())!=0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0
        #     and rec.get()==1 and RGB.get()==1) or vuelo_abortado.get()==1 : #Original
              

            #------------Crea el DF donde se guarda el estadillo
            
            df = (pd.DataFrame(columns=['Empresa', 'Trabajo', 'Fecha','Piloto','Equipo_de_vuelo','Pitch','Hora_de_inicio','Hora_final', 'PB','Vuelo','Desplazado', #'Vuelo_del_dia',
                'Vel_vuelo','Alt_vuelo','Vel_de_aire','Temp_aire','Nubes','Radiacion','Tiempo_vuelo','Dist_Recorrida','Set_Bat_1','Set_Bat_2','Set_Bat_3','Volt_inicial',
                'Volt_final','GB1/','GB2/','Anotaciones','Termica','RGB','Cali_Ini','Cali_Final','Tipologia','Vuelo_abortado']))

            df = (df.append({'Empresa': lista_desplegable_empresa.get(), 'Trabajo':lista_desplegable_trabajo.get(), 'Fecha':fecha.get(),'Piloto': lista_desplegable_piloto.get(),'Equipo_de_vuelo':lista_desplegable_equipo.get(),
                'Pitch':pitch.get(),'Hora_de_inicio': hora.get(),'Hora_final': hora_fin.get(),'PB': pb.get(),'Vuelo':v.get(), 'Desplazado': lista_desplegable_desplazado.get(), #'Vuelo_del_dia': vueloEntry.get(),
                'Vel_vuelo':lista_desplegable_velvuelo.get(),'Alt_vuelo': alt.get(),'Vel_de_aire': lista_desplegable_velaire.get(), 'Temp_aire': lista_desplegable_temp.get(), 'Nubes':lista_desplegable_nubes.get(),
                 'Radiacion': lista_desplegable_rad.get(),'Tiempo_vuelo': tiempo.get(),'Dist_Recorrida': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
                 'Volt_inicial':volt_inicial.get(),'Volt_final': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Anotaciones': textoComentario.get("1.0",'end-1c'),'Termica':termica.get(),'RGB':RGB.get(),
                 'Cali_Ini': Multy1.get(),'Cali_Final':Multy2.get(),'Tipologia': lista_desplegable_tipologia.get(),'Vuelo_abortado': vuelo_abortado.get()},ignore_index=True))

            # df = (pd.DataFrame(columns=['Empresa', 'Trabajo', 'Fecha','Piloto','Equipo_de_vuelo','Pitch','Hora_de_inicio','Hora_final', 'PB','Vuelo','Desplazado', #'Vuelo_del_dia',
            #     'Vel_vuelo','Alt_vuelo','Vel_de_aire','Temp_aire','Nubes','Radiacion','Tiempo_vuelo','Dist_Recorrida','Set_Bat_1','Set_Bat_2','Set_Bat_3','Volt_inicial',
            #     'Volt_final','GB1/','GB2/','Anotaciones','REC','RGB','Cali_Ini','Cali_Final','Tipologia','Vuelo_abortado']))

            # df = (df.append({'Empresa': lista_desplegable_empresa.get(), 'Trabajo':lista_desplegable_trabajo.get(), 'Fecha':fecha.get(),'Piloto': lista_desplegable_piloto.get(),'Equipo_de_vuelo':lista_desplegable_equipo.get(),
            #     'Pitch':pitch.get(),'Hora_de_inicio': hora.get(),'Hora_final': hora_fin.get(),'PB': pb.get(),'Vuelo':v.get(), 'Desplazado': lista_desplegable_desplazado.get(), #'Vuelo_del_dia': vueloEntry.get(),
            #     'Vel_vuelo':lista_desplegable_velvuelo.get(),'Alt_vuelo': alt.get(),'Vel_de_aire': lista_desplegable_velaire.get(), 'Temp_aire': lista_desplegable_temp.get(), 'Nubes':lista_desplegable_nubes.get(),
            #      'Radiacion': lista_desplegable_rad.get(),'Tiempo_vuelo': tiempo.get(),'Dist_Recorrida': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
            #      'Volt_inicial':volt_inicial.get(),'Volt_final': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Anotaciones': textoComentario.get("1.0",'end-1c'),'REC':rec.get(),'RGB':RGB.get(),
            #      'Cali_Ini': Multy1.get(),'Cali_Final':Multy2.get(),'Tipologia': lista_desplegable_tipologia.get(),'Vuelo_abortado': vuelo_abortado.get()},ignore_index=True))
            
            #----- Cambia punto por coma a voltaje inicial, final y pitch

            for i in df['Volt_inicial']:
                k=i.replace('.',',')
                df["Volt_inicial"].replace({i: k}, inplace=True)
                
            for j in df['Volt_final']:
                volt_coma=j.replace('.',',')
                df["Volt_final"].replace({j: volt_coma}, inplace=True)

            for k in df['Pitch']:
                pitch_coma=k.replace('.',',')
                df["Pitch"].replace({k: pitch_coma}, inplace=True)
                

            #---------- Pasa el DF a CSV    

            df.to_csv(directorio, index=None, mode="a", header=not os.path.isfile(directorio),sep=';')

            #---------- Mira a ver qué elementos se repiten en la lista de empresas y trabajos
            
            # ---CHECK EMPRESAS---
            #global opciones_empresa # Hacemos global la variable para poder ser leida de fuera de la funcion ¿No necesario?
            # Igualamos la lista_empresa a las empresas leidas del csv
            lista_empresa = opciones_empresa 

            # Annadimos a la lista de empresas la empresa introducidoa en la caja de empresas
            lista_empresa.append(lista_desplegable_empresa.get())

            # Reiniciamos la lista de empresas sin empresas repetidos
            lista_empresa_unicos = []

            # Recorremos en bucle las empresas de la lista para descartarla o annadirla a la lista si ese empresa ya estaba presente en la lista
            for i in lista_empresa:
                if i not in lista_empresa_unicos:
                    lista_empresa_unicos.append(i)

            if len(lista_empresa_unicos) == 0:
                opciones_empresa = 'Escribe algo'
            else:
                opciones_empresa  = lista_empresa_unicos
            
            lista_desplegable_empresa['values']=opciones_empresa

            # ---  ---

            # # Guardamos en el csv las empresas de la lista
            # guardar_CSV_empresas(opciones_empresa)
            
            
            # ---CHECK TRABAJOS---
            # Obtenemos la empresa de la que se va a realizar el trabajo
            empresa = lista_desplegable_empresa.get()

            # En la lista de empresas, localizamos el indice correspondiente a la empresa seleccionada
            indice_empresa = opciones_empresa.index(empresa)

            # Reiniciamos la lista de trabajos sin trabajos repetidos
            lista_trabajos_unicos = []

            # Obtenemos la lista de trabajos original para esa empresa
            # Intentamos acceder a los trabajos de la empresa, accedera si era una empresa guardada ya en la lista de empresas
            try:
                # Los trabajos son aquellos guardados en la matriz de trabajos
                lista_trabajos = matriz_opciones_trabajos[indice_empresa]

            # Si es una nueva empresa...
            except:
                # Le annadimos una lista vacia
                lista_trabajos = []
                # Generamos una nueva fila en la matriz de opciones de trabajo
                matriz_opciones_trabajos.append([])

            # Annadimos a la lista de trabajos el trabajo introducido en la caja de trabajos
            lista_trabajos.append(lista_desplegable_trabajo.get())

            # Recorremos en bucle los trabajos de la lista para descartar annadirlo a la lista si ese trabajo ya estaba presente en la lista
            for i in lista_trabajos:
                # Si el elemento de la lista no esta repetido...
                if i not in lista_trabajos_unicos:
                    # Lo guardamnos en la lista de trabajos unicos
                    lista_trabajos_unicos.append(i)

            # Si no hay ningun trabajo... (al guardar es necesario haber puesto un trabajo)
            if len(lista_trabajos_unicos) == 0: # No deberia entrar aqui nunca
                matriz_opciones_trabajos[indice_empresa] = 'Escribe algo'
            else:
                matriz_opciones_trabajos[indice_empresa] = lista_trabajos_unicos
            
            # Definimos la lista de trabajos que se van a mostrar al pinchar en el desplegable
            lista_desplegable_trabajo['values']=matriz_opciones_trabajos[indice_empresa]

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_empresas_trabajos(opciones_empresa,matriz_opciones_trabajos)

            # --Original--
            # global opciones_trabajo
            # lista_trabajo.append(lista_desplegable_trabajo.get())
            # for i in lista_trabajo:
            #     if i not in lista_trabajo_unicos:
            #         lista_trabajo_unicos.append(i)
            # if len(lista_trabajo_unicos) == 0:
            #     opciones_trabajo = 'Escribe algo'
            # else:
            #     opciones_trabajo  = lista_trabajo_unicos
            
            # lista_desplegable_trabajo['values']=opciones_trabajo
            # --  --
            # ---  ---
            #---------- 

            #---------- Mira a ver qué elementos se repiten en la lista de pilotos
            
            #global opciones_piloto # Hacemos global la variable para poder ser leida de fuera de la funcion
            lista_piloto = opciones_piloto # Igualamos la lista_piloto a los pilotos leidos del csv
            lista_piloto.append(lista_desplegable_piloto.get())

            # Reiniciamos la lista de pilotos no repetidos
            lista_piloto_unicos = []

            for i in lista_piloto:
                if i not in lista_piloto_unicos:
                    lista_piloto_unicos.append(i)
            if len(lista_piloto_unicos) == 0:
                opciones_piloto = 'Escribe algo'
            else:
                opciones_piloto  = lista_piloto_unicos
            
            lista_desplegable_piloto['values']=opciones_piloto

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_pilotos(opciones_piloto)

            #-------- Conexión con base de datos
            
            l = [lista_desplegable_trabajo.get(), '_desp'] #Crea el nombre en funcion de la planta de tal manera que quede así: 'nombrePlanta_desp'
            nombre_df = ''.join(l)
            
            
            s = (pd.DataFrame(columns=['year','planta','powerblock','vuelo','desp_x','desp_y'])) #Crea el DF que será exportado como tabla a la base de datos
            s = (s.append({'year':localtime[0] ,'planta':(lista_desplegable_trabajo.get()).upper(),'powerblock':pb.get(),'vuelo':v.get(),
                'desp_x':desplazamiento_x(),'desp_y':desplazamiento_y()},ignore_index=True))

            
            
            #engine = create_engine('postgresql://atom:Maps2019!@82.223.110.207:5432/atomdb') #Conexión con la BBDD
            #s.to_sql(str(nombre_df), engine, if_exists='append',index=False) #Sube la tabla a la BBDD

            '''#Por si quieres ver el contenido de la tabla registrada en la base de datos
            conn = engine.raw_connection() #If the connection was created successfully, the connect() function returns a new connection object, otherwise, it throws a DatabaseError exception.
            
            cursor = conn.cursor() #The cursor object is used to execute SELECT statements.
            cursor.execute("""SELECT * FROM nombre_df """)# WHERE table_schema = 'public'""")
            for table in cursor.fetchall():
                print(table)
            '''
                
            
            #------ Vuelo autorrelleno

            #vueloEntry.delete(0,'end')
            #vueloEntry.insert(0,vuelo_autorrelleno())

            #----------- Reinicia las variables

            reinicio_variables()
        else:
            MessageBox.showerror("Error", "No se han rellenado todos los parámetros necesarios para completar la inspección fotovoltaica.")

    elif lista_desplegable_tipo_trabajo.get() == 'Agricultura':

        #---------------- Si los siguientes campos no están rellenos no te deja guardar
        if (len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
            and len(hora.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0 and Multy1.get()==1 and Multy2.get()==1 and len(gb1.get()) != 0 and len(gb2.get()) != 0
            and len(bat.get()) != 0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0 and RGB.get()==1) or vuelo_abortado.get()==1:

            #------------Crea el DF donde se guarda el estadillo
            
            df = (pd.DataFrame(columns=['Empresa', 'Trabajo', 'Fecha','Piloto','Equipo_de_vuelo','Pitch','Hora_de_inicio','Hora_final', 'PB','Vuelo','Desplazado', #'Vuelo_del_dia',
                'Vel_vuelo','Alt_vuelo','Vel_de_aire','Temp_aire','Nubes','Radiacion','Tiempo_vuelo','Dist_Recorrida','Set_Bat_1','Set_Bat_2','Set_Bat_3','Volt_inicial',
                'Volt_final','GB1/','GB2/','Anotaciones','Termica','RGB','Cali_Ini','Cali_Final','Tipologia','Vuelo_abortado']))

            df = (df.append({'Empresa': lista_desplegable_empresa.get(), 'Trabajo':lista_desplegable_trabajo.get(), 'Fecha':fecha.get(),'Piloto': lista_desplegable_piloto.get(),'Equipo_de_vuelo':lista_desplegable_equipo.get(),
                'Pitch':pitch.get(),'Hora_de_inicio': hora.get(),'Hora_final': hora_fin.get(),'PB': pb.get(),'Vuelo':v.get(), 'Desplazado': lista_desplegable_desplazado.get(), #'Vuelo_del_dia': vueloEntry.get(),
                'Vel_vuelo':lista_desplegable_velvuelo.get(),'Alt_vuelo': alt.get(),'Vel_de_aire': lista_desplegable_velaire.get(), 'Temp_aire': lista_desplegable_temp.get(), 'Nubes':lista_desplegable_nubes.get(),
                 'Radiacion': lista_desplegable_rad.get(),'Tiempo_vuelo': tiempo.get(),'Dist_Recorrida': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
                 'Volt_inicial':volt_inicial.get(),'Volt_final': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Anotaciones': textoComentario.get("1.0",'end-1c'),'Termica':termica.get(),'RGB':RGB.get(),
                 'Cali_Ini': Multy1.get(),'Cali_Final':Multy2.get(),'Tipologia': lista_desplegable_tipologia.get(),'Vuelo_abortado': vuelo_abortado.get()},ignore_index=True))

            #----- Cambia punto por coma a voltaje inicial, final y pitch

            for i in df['Volt_inicial']:
                k=i.replace('.',',')
                df["Volt_inicial"].replace({i: k}, inplace=True)
                
            for j in df['Volt_final']:
                volt_coma=j.replace('.',',')
                df["Volt_final"].replace({j: volt_coma}, inplace=True)

             #---------- Pasa el DF a CSV    

            df.to_csv(directorio, index=None, mode="a", header=not os.path.isfile(directorio),sep=';')

            #---------- Mira a ver qué elementos se repiten en la lista de empresas y trabajos
            
            # ---CHECK EMPRESAS---
            #global opciones_empresa # Hacemos global la variable para poder ser leida de fuera de la funcion ¿No necesario?
            # Igualamos la lista_empresa a las empresas leidas del csv
            lista_empresa = opciones_empresa 

            # Annadimos a la lista de empresas la empresa introducidoa en la caja de empresas
            lista_empresa.append(lista_desplegable_empresa.get())

            # Reiniciamos la lista de empresas sin empresas repetidos
            lista_empresa_unicos = []

            # Recorremos en bucle las empresas de la lista para descartarla o annadirla a la lista si ese empresa ya estaba presente en la lista
            for i in lista_empresa:
                if i not in lista_empresa_unicos:
                    lista_empresa_unicos.append(i)

            if len(lista_empresa_unicos) == 0:
                opciones_empresa = 'Escribe algo'
            else:
                opciones_empresa  = lista_empresa_unicos
            
            lista_desplegable_empresa['values']=opciones_empresa

            # ---  ---           
            
            # ---CHECK TRABAJOS---
            # Obtenemos la empresa de la que se va a realizar el trabajo
            empresa = lista_desplegable_empresa.get()

            # En la lista de empresas, localizamos el indice correspondiente a la empresa seleccionada
            indice_empresa = opciones_empresa.index(empresa)

            # Reiniciamos la lista de trabajos sin trabajos repetidos
            lista_trabajos_unicos = []

            # Obtenemos la lista de trabajos original para esa empresa
            # Intentamos acceder a los trabajos de la empresa, accedera si era una empresa guardada ya en la lista de empresas
            try:
                # Los trabajos son aquellos guardados en la matriz de trabajos
                lista_trabajos = matriz_opciones_trabajos[indice_empresa]

            # Si es una nueva empresa...
            except:
                # Le annadimos una lista vacia
                lista_trabajos = []
                # Generamos una nueva fila en la matriz de opciones de trabajo
                matriz_opciones_trabajos.append([])

            # Annadimos a la lista de trabajos el trabajo introducido en la caja de trabajos
            lista_trabajos.append(lista_desplegable_trabajo.get())

            # Recorremos en bucle los trabajos de la lista para descartar annadirlo a la lista si ese trabajo ya estaba presente en la lista
            for i in lista_trabajos:
                # Si el elemento de la lista no esta repetido...
                if i not in lista_trabajos_unicos:
                    # Lo guardamnos en la lista de trabajos unicos
                    lista_trabajos_unicos.append(i)

            # Si no hay ningun trabajo... (al guardar es necesario haber puesto un trabajo)
            if len(lista_trabajos_unicos) == 0: # No deberia entrar aqui nunca
                matriz_opciones_trabajos[indice_empresa] = 'Escribe algo'
            else:
                matriz_opciones_trabajos[indice_empresa] = lista_trabajos_unicos
            
            # Definimos la lista de trabajos que se van a mostrar al pinchar en el desplegable
            lista_desplegable_trabajo['values']=matriz_opciones_trabajos[indice_empresa]

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_empresas_trabajos(opciones_empresa,matriz_opciones_trabajos)

            #---------- Mira a ver qué elementos se repiten en la lista de pilotos
            
            #global opciones_piloto # Hacemos global la variable para poder ser leida de fuera de la funcion
            lista_piloto = opciones_piloto # Igualamos la lista_piloto a los pilotos leidos del csv
            lista_piloto.append(lista_desplegable_piloto.get())

            # Reiniciamos la lista de pilotos no repetidos
            lista_piloto_unicos = []

            for i in lista_piloto:
                if i not in lista_piloto_unicos:
                    lista_piloto_unicos.append(i)
            if len(lista_piloto_unicos) == 0:
                opciones_piloto = 'Escribe algo'
            else:
                opciones_piloto  = lista_piloto_unicos
            
            lista_desplegable_piloto['values']=opciones_piloto

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_pilotos(opciones_piloto)

            #----------- Reinicia las variables

            reinicio_variables()

        else:
            MessageBox.showerror("Error", "No se han rellenado todos los parámetros necesarios para completar la inspección de agricultura.")
    
    elif lista_desplegable_tipo_trabajo.get() == 'Eolica' or lista_desplegable_tipo_trabajo.get() == 'Otro':

        #---------------- Si los siguientes campos no están rellenos no te deja guardar
        if (len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
            and len(hora.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0
            and len(bat.get()) != 0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0 and RGB.get()==1) or vuelo_abortado.get()==1:

            #------------Crea el DF donde se guarda el estadillo
            
            df = (pd.DataFrame(columns=['Empresa', 'Trabajo', 'Fecha','Piloto','Equipo_de_vuelo','Pitch','Hora_de_inicio','Hora_final', 'PB','Vuelo','Desplazado', #'Vuelo_del_dia',
                'Vel_vuelo','Alt_vuelo','Vel_de_aire','Temp_aire','Nubes','Radiacion','Tiempo_vuelo','Dist_Recorrida','Set_Bat_1','Set_Bat_2','Set_Bat_3','Volt_inicial',
                'Volt_final','GB1/','GB2/','Anotaciones','Termica','RGB','Cali_Ini','Cali_Final','Tipologia','Vuelo_abortado']))

            df = (df.append({'Empresa': lista_desplegable_empresa.get(), 'Trabajo':lista_desplegable_trabajo.get(), 'Fecha':fecha.get(),'Piloto': lista_desplegable_piloto.get(),'Equipo_de_vuelo':lista_desplegable_equipo.get(),
                'Pitch':pitch.get(),'Hora_de_inicio': hora.get(),'Hora_final': hora_fin.get(),'PB': pb.get(),'Vuelo':v.get(), 'Desplazado': lista_desplegable_desplazado.get(), #'Vuelo_del_dia': vueloEntry.get(),
                'Vel_vuelo':lista_desplegable_velvuelo.get(),'Alt_vuelo': alt.get(),'Vel_de_aire': lista_desplegable_velaire.get(), 'Temp_aire': lista_desplegable_temp.get(), 'Nubes':lista_desplegable_nubes.get(),
                 'Radiacion': lista_desplegable_rad.get(),'Tiempo_vuelo': tiempo.get(),'Dist_Recorrida': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
                 'Volt_inicial':volt_inicial.get(),'Volt_final': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Anotaciones': textoComentario.get("1.0",'end-1c'),'Termica':termica.get(),'RGB':RGB.get(),
                 'Cali_Ini': Multy1.get(),'Cali_Final':Multy2.get(),'Tipologia': lista_desplegable_tipologia.get(),'Vuelo_abortado': vuelo_abortado.get()},ignore_index=True))

            #----- Cambia punto por coma a voltaje inicial, final y pitch

            for i in df['Volt_inicial']:
                k=i.replace('.',',')
                df["Volt_inicial"].replace({i: k}, inplace=True)
                
            for j in df['Volt_final']:
                volt_coma=j.replace('.',',')
                df["Volt_final"].replace({j: volt_coma}, inplace=True)

             #---------- Pasa el DF a CSV    

            df.to_csv(directorio, index=None, mode="a", header=not os.path.isfile(directorio),sep=';')

            #---------- Mira a ver qué elementos se repiten en la lista de empresas y trabajos
            
            # ---CHECK EMPRESAS---
            #global opciones_empresa # Hacemos global la variable para poder ser leida de fuera de la funcion ¿No necesario?
            # Igualamos la lista_empresa a las empresas leidas del csv
            lista_empresa = opciones_empresa 

            # Annadimos a la lista de empresas la empresa introducidoa en la caja de empresas
            lista_empresa.append(lista_desplegable_empresa.get())

            # Reiniciamos la lista de empresas sin empresas repetidos
            lista_empresa_unicos = []

            # Recorremos en bucle las empresas de la lista para descartarla o annadirla a la lista si ese empresa ya estaba presente en la lista
            for i in lista_empresa:
                if i not in lista_empresa_unicos:
                    lista_empresa_unicos.append(i)

            if len(lista_empresa_unicos) == 0:
                opciones_empresa = 'Escribe algo'
            else:
                opciones_empresa  = lista_empresa_unicos
            
            lista_desplegable_empresa['values']=opciones_empresa

            # ---  ---           
            
            # ---CHECK TRABAJOS---
            # Obtenemos la empresa de la que se va a realizar el trabajo
            empresa = lista_desplegable_empresa.get()

            # En la lista de empresas, localizamos el indice correspondiente a la empresa seleccionada
            indice_empresa = opciones_empresa.index(empresa)

            # Reiniciamos la lista de trabajos sin trabajos repetidos
            lista_trabajos_unicos = []

            # Obtenemos la lista de trabajos original para esa empresa
            # Intentamos acceder a los trabajos de la empresa, accedera si era una empresa guardada ya en la lista de empresas
            try:
                # Los trabajos son aquellos guardados en la matriz de trabajos
                lista_trabajos = matriz_opciones_trabajos[indice_empresa]

            # Si es una nueva empresa...
            except:
                # Le annadimos una lista vacia
                lista_trabajos = []
                # Generamos una nueva fila en la matriz de opciones de trabajo
                matriz_opciones_trabajos.append([])

            # Annadimos a la lista de trabajos el trabajo introducido en la caja de trabajos
            lista_trabajos.append(lista_desplegable_trabajo.get())

            # Recorremos en bucle los trabajos de la lista para descartar annadirlo a la lista si ese trabajo ya estaba presente en la lista
            for i in lista_trabajos:
                # Si el elemento de la lista no esta repetido...
                if i not in lista_trabajos_unicos:
                    # Lo guardamnos en la lista de trabajos unicos
                    lista_trabajos_unicos.append(i)

            # Si no hay ningun trabajo... (al guardar es necesario haber puesto un trabajo)
            if len(lista_trabajos_unicos) == 0: # No deberia entrar aqui nunca
                matriz_opciones_trabajos[indice_empresa] = 'Escribe algo'
            else:
                matriz_opciones_trabajos[indice_empresa] = lista_trabajos_unicos
            
            # Definimos la lista de trabajos que se van a mostrar al pinchar en el desplegable
            lista_desplegable_trabajo['values']=matriz_opciones_trabajos[indice_empresa]

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_empresas_trabajos(opciones_empresa,matriz_opciones_trabajos)

            #---------- Mira a ver qué elementos se repiten en la lista de pilotos
            
            #global opciones_piloto # Hacemos global la variable para poder ser leida de fuera de la funcion
            lista_piloto = opciones_piloto # Igualamos la lista_piloto a los pilotos leidos del csv
            lista_piloto.append(lista_desplegable_piloto.get())

            # Reiniciamos la lista de pilotos no repetidos
            lista_piloto_unicos = []

            for i in lista_piloto:
                if i not in lista_piloto_unicos:
                    lista_piloto_unicos.append(i)
            if len(lista_piloto_unicos) == 0:
                opciones_piloto = 'Escribe algo'
            else:
                opciones_piloto  = lista_piloto_unicos
            
            lista_desplegable_piloto['values']=opciones_piloto

            # Guardamos en el csv las empresas de la lista
            guardar_CSV_pilotos(opciones_piloto)

            #----------- Reinicia las variables

            reinicio_variables()

        else:
            MessageBox.showerror("Error", "No se han rellenado todos los parámetros necesarios.")
              
def opciones_desplazado(a): #Modificado# Le añades un parámetro random (a) y la funcion empieza a funcionar

    if lista_desplegable_tipologia.get() == 'Fijo':
        lista_desplegable_desplazado['values'] = ['1 N','C','1 S']
        #opciones_desplazado = ['1 N','C','1 S']#Original

    elif lista_desplegable_tipologia.get() == 'Seguidores N-S' or lista_desplegable_tipologia.get() == 'Seguidores polares':
        lista_desplegable_desplazado['values'] = ['4 E','3 E','2 E','1 E','C','1 O','2 O','3 O','4 O']
        #opciones_desplazado = ['4 E','3 E','2 E','1 E','C','1 O','2 O','3 O','4 O']#Original

    else:
        lista_desplegable_desplazado['values'] = ['Todavía nada']
        #opciones_desplazado = ['Todavía nada']#Original

    #lista_desplegable_desplazado['values']=opciones_desplazado#Original
    #return lista_desplegable_desplazado

# Funcion para seleccionar que opciones de trabajo se van a desplegar en funcion de la empresa seleccionada
def elegir_trabajos_empresa(a): #Modificado# Le añades un parámetro random (a) y la funcion empieza a funcionar

    # Obtenemos la empresa de la que se va a realizar el trabajo
    empresa = lista_desplegable_empresa.get()

    # En la lista de empresas, localizamos el indice correspondiente a la empresa seleccionada
    indice_empresa = opciones_empresa.index(empresa)

    # Definimos las opciones de trabajo para la empresa seleccionada
    lista_desplegable_trabajo['values']= matriz_opciones_trabajos[indice_empresa]



def desplazamiento_y():
    if lista_desplegable_desplazado.get() == '1 N':
        desp_y = -1 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '1 S':
        desp_y = pitch.get()
    elif lista_desplegable_desplazado.get() == 'C':
        desp_y = 0
    else:
        desp_y = 0
    return desp_y
    
def desplazamiento_x():        
    if lista_desplegable_desplazado.get() == '2 O':
        desp_x = 2 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '1 O':
        desp_x = pitch.get()
    elif lista_desplegable_desplazado.get() == '0.5 O':
        desp_x = 0.5 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == 'C':
        desp_x = 0
    elif lista_desplegable_desplazado.get() == '0.5 E':
        desp_x = -0.5 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '1 E':
        desp_x = -1 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '2 E':
        desp_x = -2 * float(pitch.get())
    else:
        desp_x = 0

    return desp_x

def ocultar_mostrar(a):
    if lista_desplegable_tipo_trabajo.get() == 'Agricultura':
        pitchLabel.place_forget()
        pitchEntry.place_forget()
        tipologiaLabel.place_forget()
        lista_desplegable_tipologia.place_forget()
        pbLabel.place_forget()
        pbEntry.place_forget()
        desplazadoLabel.place_forget()
        lista_desplegable_desplazado.place_forget()
        termicalabel.place_forget()
        casilla_termica.place_forget()
        Multylabel.place(x=0,y=435)
        casilla_Multy1.place(x=90,y=440)
        casilla_Multy2.place(x=120,y=440)
        gb1Label.place(x=0,y=520)
        gb1Entry.place(x=180,y=520)
        gb2Label.place(x=0,y=580)
        gb2Entry.place(x=215,y=580)

    elif lista_desplegable_tipo_trabajo.get() == 'Fotovoltaica':
        pitchLabel.place(x=1150,y=65)
        pitchEntry.place(x=1250,y=65)
        tipologiaLabel.place(x=1020,y=110)
        lista_desplegable_tipologia.place(x=1250,y=110)
        pbLabel.place(x=140,y=200)
        pbEntry.place(x=200,y=200)
        desplazadoLabel.place(x=550,y=200)
        lista_desplegable_desplazado.place(x=720,y=200)
        termicalabel.place(x=0,y=365)
        casilla_termica.place(x=90,y=370)
        Multylabel.place_forget()
        casilla_Multy1.place_forget()
        casilla_Multy2.place_forget()
        gb1Label.place_forget()
        gb1Entry.place_forget()
        gb2Label.place_forget()
        gb2Entry.place_forget()

    elif lista_desplegable_tipo_trabajo.get() == 'Eolica' or lista_desplegable_tipo_trabajo.get() == 'Otro':
        pitchLabel.place_forget()
        pitchEntry.place_forget()
        tipologiaLabel.place_forget()
        lista_desplegable_tipologia.place_forget()
        pbLabel.place_forget()
        pbEntry.place_forget()
        desplazadoLabel.place_forget()
        lista_desplegable_desplazado.place_forget()
        termicalabel.place_forget()
        casilla_termica.place_forget()
        Multylabel.place_forget()
        casilla_Multy1.place_forget()
        casilla_Multy2.place_forget()
        gb1Label.place_forget()
        gb1Entry.place_forget()
        gb2Label.place_forget()
        gb2Entry.place_forget()

def open_csv():
    webbrowser.open(os.path.join(os.getcwd(),str(fecha.get()).split(':')[0]+'_'+str(fecha.get()).split(':')[1]+'_'+str(fecha.get()).split(':')[2]+'_estadillo.csv'))

#------------------- Imagen Atom
 
canvas = Canvas(miFrame, width = 250, height = 90, bg=colorGrisFondo, highlightthickness=0)
#canvas = Canvas(miFrame, width = 250, height = 90) #Original
canvas.place(x=550,y=-40)
#canvas.place(x=550,y=-40) #original
img = ImageTk.PhotoImage(Image.open("atom1.png").resize((250,90))) #1733x625 
canvas.create_image(0, 0, anchor=NW, image=img) 

#--------------------- Crea el estilo para los combobox

combostyle = ttk.Style()
combostyle.theme_create('custom.TCombobox',parent='clam', settings = {'custom.TCombobox':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': 'yellow',
                                       #'background': 'green'
                                       }}}
                         )
combostyle.theme_use('custom.TCombobox') 

#------------------------Fuentes
fontStyle = tkFont.Font(family="Lucida Grande", size=17)
font_boton= tkFont.Font(family="Lucida Grande", size=14)

#------------------------- Variables que no cambian
empresa = StringVar()
trabajo = StringVar()
fecha = StringVar()
pitch = StringVar()
piloto = StringVar()
equipo_de_vuelo = StringVar()

empresaLabel = Label(miFrame, text="Empresa: ",font=fontStyle, bg=colorGrisFondo)
empresaLabel.place(x=0,y=70)
lista_desplegable_empresa = ttk.Combobox(miFrame, width=15, font=fontStyle,style="custom.TCombobox")
lista_desplegable_empresa.bind("<<ComboboxSelected>>", elegir_trabajos_empresa)
lista_desplegable_empresa.place(x=120,y=70)
lista_desplegable_empresa['values']=opciones_empresa

trabajoLabel = Label(miFrame, text="Trabajo: ",font=fontStyle, bg=colorGrisFondo)
trabajoLabel.place(x=0, y=110)
lista_desplegable_trabajo = ttk.Combobox(miFrame, width=15, font=fontStyle,style="custom.TCombobox")
lista_desplegable_trabajo.place(x=120,y=110)

boton_fecha = Button(miFrame, text = "Fecha", command=fecha_boton,font=font_boton,bg=colorGrisBotones)
boton_fecha.place(x=770,y=58) #Original (x=780,y=58)
fechaEntry = Entry(miFrame,textvariable=fecha,font=fontStyle,bg='yellow',width=10)
fechaEntry.place(x=850,y=65)

pitchLabel = Label(miFrame, text="Pitch [m]:",font=fontStyle,width=7, bg=colorGrisFondo)
pitchLabel.place(x=1150,y=65)
pitchEntry = Entry(miFrame,textvariable=pitch,font=fontStyle,width=5,bg='yellow')
pitchEntry.place(x=1250,y=65)

pilotoLabel = Label(miFrame, text="Piloto: ",font=fontStyle, bg=colorGrisFondo)
pilotoLabel.place(x=350,y=70)
lista_desplegable_piloto = ttk.Combobox(miFrame, width=16,style="custom.TCombobox",font=fontStyle)
#lista_desplegable_piloto = ttk.Combobox(miFrame, width=7,state='readonly',style="custom.TCombobox",font=fontStyle) #Original. state='readonly' hace que solo se pueda seleccionar las opciones de la lista desplegable
lista_desplegable_piloto.place(x=440,y=70)
#opciones_piloto = ['Alberto Cristóbal','Oscar Álvarez','Operador Extranjero','Foreing Operator']
lista_desplegable_piloto['values']=opciones_piloto

equipoLabel = Label(miFrame, text="Equipo de vuelo: ",font=fontStyle, bg=colorGrisFondo)
equipoLabel.place(x=350, y= 110)
lista_desplegable_equipo = ttk.Combobox(miFrame, width=10,state='readonly',font=fontStyle,style="custom.TCombobox")
lista_desplegable_equipo.place(x=520,y=110)
opciones_equipo = ['AT4-01','AT4-05','AT6-01','AT6-02','DJI M200','DJI M300','Mavic','Mavic Mini2','Mavic 2EA','Phantom3']
lista_desplegable_equipo['values']=opciones_equipo

tipologiaLabel = Label(miFrame, text="Tipologia de la planta: ",font=fontStyle, bg=colorGrisFondo)
tipologiaLabel.place(x=1020,y=110)
lista_desplegable_tipologia = ttk.Combobox(miFrame, width=15,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_tipologia.bind("<<ComboboxSelected>>", opciones_desplazado)
lista_desplegable_tipologia.place(x=1250,y=110)
opciones_tipologia = ['Fijo','Seguidores N-S','Seguidores 2 ejes','Seguidores polares']
lista_desplegable_tipologia['values']=opciones_tipologia
  
tipo_trabajoLabel = Label(miFrame, text="Tipo de trabajo: ",font=fontStyle, bg=colorGrisFondo)
tipo_trabajoLabel.place(x=680,y=110)
lista_desplegable_tipo_trabajo = ttk.Combobox(miFrame, width=10,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_tipo_trabajo.bind("<<ComboboxSelected>>", ocultar_mostrar)
lista_desplegable_tipo_trabajo.place(x=850,y=110)
opciones_tipo_trabajo = ['Fotovoltaica','Agricultura','Eolica','Otro']
lista_desplegable_tipo_trabajo['values']=opciones_tipo_trabajo


#-----------------Crea las líneas de separación

line_style = ttk.Style()
line_style.configure("Line.TSeparator", background="#000000")
#line = ttk.Separator(self.tk, orient=TK.VERTICAL, style="Line.TSeparator")
separator = ttk.Separator(miFrame, orient='horizontal',style="Line.TSeparator")
separator2 = ttk.Separator(miFrame, orient='horizontal',style="Line.TSeparator")

separator.place(x=0,y=160,width=2500)
separator2.place(x=0,y=350,width=2500)


#--------------------- Variables que cambian

vuelo = IntVar()
hora = StringVar()
hora_fin = StringVar()
zona = StringVar()
desplazado = StringVar()
vel_vuelo = StringVar()
alt = StringVar()
vel_aire = StringVar()
temp = StringVar()
nubes = StringVar()
radiacion = StringVar()
tiempo = StringVar()
distancia = StringVar()
bat = StringVar()
bat2 = StringVar()
bat3 = StringVar()
volt_inicial = StringVar()
volt_final = StringVar()
gb1 = StringVar()
gb2 = StringVar()
termica = IntVar()      # 1 si, 0 no
#rec = IntVar()      # 1 si, 0 no
RGB = IntVar()    # 1 si, 0 no
Multy1 = IntVar() # 1 si, 0 no
Multy2 = IntVar() # 1 si, 0 no
vuelo_abortado = IntVar() # 1 si, 0 no
tipologia = StringVar()
pb  =StringVar()
v = StringVar()

termicalabel = Label(miFrame, text='Térmica', font=fontStyle, bg=colorGrisFondo)
termicalabel.place(x=0,y=365)
casilla_termica = Checkbutton(miFrame,variable=termica, onvalue=1, offvalue=0,bg='yellow')
casilla_termica.place(x=90,y=370)

RGBlabel = Label(miFrame, text='RGB', font=fontStyle, bg=colorGrisFondo)
RGBlabel.place(x=0,y=400)
casilla_RGB = Checkbutton(miFrame,variable=RGB, onvalue=1, offvalue=0,bg='yellow')
casilla_RGB.place(x=90,y=405) #Original x=60,y=405

Multylabel = Label(miFrame, text='MULTY', font=fontStyle, bg=colorGrisFondo)
Multylabel.place(x=0,y=435)
casilla_Multy1 = Checkbutton(miFrame,variable=Multy1, onvalue=1, offvalue=0, bg='yellow')
casilla_Multy1.place(x=90,y=440)
casilla_Multy2 = Checkbutton(miFrame,variable=Multy2, onvalue=1, offvalue=0, bg='yellow')
casilla_Multy2.place(x=120,y=440)

boton_print = Button(miFrame, text = "CSV", command=open_csv,font=font_boton,bg=colorGrisBotones)
boton_print.place(x=1300,y=680)

boton_hora = Button(miFrame, text = "Hora de inicio", command=hora_boton,font=font_boton,bg=colorGrisBotones)
boton_hora.place(x=240,y=295) #Original (x=200,y=295)
horaEntry = Entry(miFrame,textvariable=hora,font=fontStyle,width= 8,bg='yellow')
horaEntry.place(x=380,y=300)

boton_hora_fin = Button(miFrame, text = "Hora final", command=hora_boton_fin,font=font_boton,bg=colorGrisBotones)
boton_hora_fin.place(x=240,y=365) #Original (x=200,y=365)
hora_fin_Entry = Entry(miFrame,textvariable=hora_fin,font=fontStyle,width= 8,bg='yellow')
hora_fin_Entry.place(x=380,y=370)

zonaLabel = Label(miFrame, text="Zona volada: ",font=fontStyle, bg=colorGrisFondo)
zonaLabel.place(x=0,y=200)

pbLabel = Label(miFrame, text="PB: ",font=fontStyle,width=5, bg=colorGrisFondo)
pbLabel.place(x=140,y=200) #Original (x=200,y=200)
pbEntry = Entry(miFrame,textvariable=pb,font=fontStyle,width=5,bg='yellow')
pbEntry.place(x=200,y=200) #Original (x=280,y=200)

vLabel = Label(miFrame, text="Vuelo: ",font=fontStyle,width=5, bg=colorGrisFondo)
vLabel.place(x=300,y=200) #Original (x=370,y=200) 
vEntry = Entry(miFrame,textvariable=v,font=fontStyle,width=5,bg='yellow')
vEntry.place(x=380,y=200) #Original (x=450,y=200)

desplazadoLabel = Label(miFrame, text="Desplazado: ",font=fontStyle, bg=colorGrisFondo)
desplazadoLabel.place(x=550,y=200)
lista_desplegable_desplazado = ttk.Combobox(miFrame, width=8,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_desplazado.place(x=720,y=200)

velvueloLabel = Label(miFrame, text="Vel. vuelo [m/s]:",font=fontStyle, bg=colorGrisFondo)
velvueloLabel.place(x=550,y=300)
lista_desplegable_velvuelo = ttk.Combobox(miFrame, width=4,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_velvuelo.place(x=720,y=300)
opciones_velvuelo = ['3','3.5','4','4.5','5','5.5','6']
lista_desplegable_velvuelo['values']=opciones_velvuelo

altLabel = Label(miFrame, text="Alt. Vuelo [m]:",font=fontStyle, bg=colorGrisFondo)
altLabel.place(x=550,y=250)
altEntry = Entry(miFrame,textvariable=alt,font=fontStyle,bg='yellow',width=4)
altEntry.place(x=720,y=250)

velaireLabel = Label(miFrame, text="Vel. de aire [km/h]:",font=fontStyle, bg=colorGrisFondo)
velaireLabel.place(x=1130,y=200)
lista_desplegable_velaire = ttk.Combobox(miFrame, width=9,state='readonly',font=fontStyle)
lista_desplegable_velaire.place(x=1330,y=200)
opciones_velaire = ['De 0 a 5','De 5 a 10','De 10 a 20','De 20 a 30']
lista_desplegable_velaire['values']=opciones_velaire

tempLabel = Label(miFrame, text="Temp. aire [°C]:",font=fontStyle, bg=colorGrisFondo)
tempLabel.place(x=1180,y=250)
lista_desplegable_temp = ttk.Combobox(miFrame, width=6,state='readonly',font=fontStyle)
lista_desplegable_temp.place(x=1350,y=250)
opciones_temp = ['<10','10-15','15-20','20-25','25-30','30-35','35-40','>40']
lista_desplegable_temp['values']=opciones_temp

nubesLabel = Label(miFrame, text="Nubes [Octas]:",font=fontStyle, bg=colorGrisFondo)
nubesLabel.place(x=880,y=200)
lista_desplegable_nubes = ttk.Combobox(miFrame, width=4,state='readonly',font=fontStyle)
lista_desplegable_nubes.place(x=1040,y=200)
opciones_nubes = ['0','1','2','3']
lista_desplegable_nubes['values']=opciones_nubes

radiacionLabel = Label(miFrame, text="Radiacion [W/m^2]:",font=fontStyle, bg=colorGrisFondo)
radiacionLabel.place(x=880,y=250)
lista_desplegable_rad = ttk.Combobox(miFrame, width=4,state='readonly',font=fontStyle)
lista_desplegable_rad.place(x=1090,y=250)
opciones_rad = ['>400','>500','>600','>700','>800','>900']
lista_desplegable_rad['values']=opciones_rad

tiempoLabel = Label(miFrame, text="Tiempo vuelo [s]:",font=fontStyle, bg=colorGrisFondo)
tiempoLabel.place(x=710,y=370)
tiempoEntry = Entry(miFrame,textvariable=tiempo,font=fontStyle,width=5)
tiempoEntry.place(x=885,y=370)

distanciaLabel = Label(miFrame, text="Dist. recorrida [m]:",font=fontStyle, bg=colorGrisFondo)
distanciaLabel.place(x=980,y=370)
distanciaEntry = Entry(miFrame,textvariable=distancia,font=fontStyle,width=5)
distanciaEntry.place(x=1170,y=370)

batLabel = Label(miFrame, text="Set Bat: ",font=fontStyle, bg=colorGrisFondo)
batLabel.place(x=0,y=250)
batEntry = Entry(miFrame,textvariable=bat,font=fontStyle,width=5,bg='yellow')
batEntry.place(x=100,y=250)
bat2Entry = Entry(miFrame,textvariable=bat2,font=fontStyle,width=5)
bat2Entry.place(x=170,y=250)
bat3Entry = Entry(miFrame,textvariable=bat3,font=fontStyle,width=5)
bat3Entry.place(x=240,y=250)

voltinicialLabel = Label(miFrame, text="Volt inicial [V]:",font=fontStyle, bg=colorGrisFondo)
voltinicialLabel.place(x=0,y=300)
voltinicialEntry = Entry(miFrame,textvariable=volt_inicial,font=fontStyle,bg='yellow',width=4)
voltinicialEntry.place(x=150,y=300)

voltfinalLabel = Label(miFrame, text="Volt final [V]:",font=fontStyle, bg=colorGrisFondo)
voltfinalLabel.place(x=510,y=370)
voltfinalEntry = Entry(miFrame,textvariable=volt_final,font=fontStyle,width=4)
voltfinalEntry.place(x=640,y=370)

gb1Label = Label(miFrame, text="GB Antes Vuelo: ",font=fontStyle, bg=colorGrisFondo)
gb1Label.place(x=0,y=520)
gb1Entry = Entry(miFrame,textvariable=gb1,font=fontStyle,bg='yellow',width=10)
gb1Entry.place(x=180,y=520)

gb2Label = Label(miFrame, text="GB Despues Vuelo: ",font=fontStyle, bg=colorGrisFondo)
gb2Label.place(x=0,y=580)
gb2Entry = Entry(miFrame,textvariable=gb2,font=fontStyle,bg='yellow',width=10)
gb2Entry.place(x=215,y=580)

label2=Label(miFrame, text="Anotaciones:", font=fontStyle, bg=colorGrisFondo)        
label2.place(x=350,y=520)

text_frame = tk.Frame(miFrame)
textoComentario=tk.Text(text_frame, width=50, height=5,font=fontStyle)
textoComentario.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
scrollVert=ttk.Scrollbar(text_frame, command=textoComentario.yview)
scrollVert.pack(fill=tk.Y, side=tk.RIGHT)

text_frame.place(x=500,y=520)

textoComentario.config(yscrollcommand=scrollVert.set)

vuelo_abortado_label = Label(miFrame, text='Vuelo abortado', font=fontStyle, bg=colorGrisFondo)
vuelo_abortado_label.place(x=1200,y=580)
casilla_vuelo_abortado = Checkbutton(miFrame,variable=vuelo_abortado, onvalue=1, offvalue=0, bg=colorGrisFondo)
casilla_vuelo_abortado.place(x=1365,y=585)

boton_guardar=Button(miFrame, text = "Guardar", command=guardar,width=10,height=1,font=font_boton,bg=colorGrisBotones)
boton_guardar.place(x=700,y=680)

#--------------------- Anotaciones importantes

notaImportantelabel = Label(miFrame, text='Todos los campos sombreados en color amarillo deberán ser rellenados para poder guardar los datos en el CSV', font=fontStyle, bg='yellow')
notaImportantelabel.place(x=20,y=750)

raiz.mainloop()