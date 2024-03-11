'''-------------------------------------------------------------------------------
 Nombre:     ESTADILLO ELECTRONICO
 Proposito:  Funciones utilizadas en el estadilllo electrónico
 Autor:      
 Creado:     dd/mm/2021
 Copyright:  (c) 2021. All rights reserved. Aerotools-UAV
 Licencia:     
 Interprete: Python 3.8
 
 Versiones:   v1(18/10/2021):
                - Creado un script solo apra las funciones
-------------------------------------------------------------------------------'''

import pandas as pd
import os
import time
import webbrowser

#-----------------Funciones
global localtime
localtime = time.localtime(time.time())
#Inicializa variables

lista_empresa = []
lista_empresa_unicos = []

lista_trabajo = []
lista_trabajo_unicos = []

contador = 1

def hora_boton(horaEntry):
    """
    Funcion para tomar la hora actual del ordenador
    """
    localtime = time.localtime(time.time())
    horaEntry.delete(0,'end')
    if localtime[3]<10 and localtime[4]<10 and localtime[5]<10:
        horaEntry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[3]<10 and localtime[4]<10:
        horaEntry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[3]<10 and localtime[5]<10:
        horaEntry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[4]<10 and localtime[5]<10:
        horaEntry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[3]<10:
        horaEntry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[4]<10:
        horaEntry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[5]<10:
        horaEntry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    else:
        horaEntry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))

def hora_boton_fin(hora_fin_Entry):
    """
    Funcion para tomar la hora final del ordenador
    """
    localtime = time.localtime(time.time())
    hora_fin_Entry.delete(0,'end')
    if localtime[3]<10 and localtime[4]<10 and localtime[5]<10:
        hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[3]<10 and localtime[4]<10:
        hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[3]<10 and localtime[5]<10:
        hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[4]<10 and localtime[5]<10:
        hora_fin_Entry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+'0'+str(localtime[5]))
    elif localtime[3]<10:
        hora_fin_Entry.insert(0,'0'+str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[4]<10:
        hora_fin_Entry.insert(0,str(localtime[3])+':'+'0'+str(localtime[4])+':'+str(localtime[5]))
    elif localtime[5]<10:
        hora_fin_Entry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+'0'+str(localtime[5]))
    else:
        hora_fin_Entry.insert(0,str(localtime[3])+':'+str(localtime[4])+':'+str(localtime[5]))

def fecha_boton(fechaEntry):
    """
    Funcion para tomar la fecha actual del ordenador
    """
    localtime = time.localtime(time.time())
    fechaEntry.delete(0,'end')
    if localtime[1]<10 and localtime[2]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+'0'+str(localtime[2]))
    elif localtime[2]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+'0'+str(localtime[2]))    
    elif localtime[1]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+str(localtime[2]))    
    else:
        fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+str(localtime[2]))
    
def reinicio_variables():
    """
    Poner en 0 o vaciar todas las variables
    """
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
    rec.set(0)
    RGB.set(0)
    Multy1.set(0)
    Multy2.set(0)
    vuelo_abortado.set(0)

      
def opciones_desplazado():
    """
    Devuelve la lista de opciones de desplazamiento en funcion de la tipología seleccionada
    """
    if lista_desplegable_tipologia.get() == 'Fijo':
        opciones_desplazado = ['1 N','C','1 S']
    elif lista_desplegable_tipologia.get() == 'Seguidores N-S' or lista_desplegable_tipologia.get() == 'Seguidores polares':
        opciones_desplazado = ['2 E','1 E','0.5 E','C','0.5 O','1 O','2 O']
    else:
        opciones_desplazado = ['Todavía nada']

    lista_desplegable_desplazado['values'] = opciones_desplazado
    return(lista_desplegable_desplazado)

def desplazamiento_y():
    """
    Calcula el desplazamiento (Y) en metros en funcion de la opcion de desplazamiento seleccionada
    """
    if lista_desplegable_desplazado.get() == '1 N':
        desp_y = -1 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '1 S':
        desp_y = pitch.get()
    elif lista_desplegable_desplazado.get() == 'C':
        desp_y = 0
    else:
        desp_y = 0
    return(desp_y)
    
def desplazamiento_x():
    """
    Calcula el desplazamiento (X) en metros en funcion de la opcion de desplazamiento seleccionada
    """ 
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

    return(desp_x)

def ocultar_mostrar():
    """
    Mostrar inputs, labels y otras opciones en funcion del tipo de trabajo seleccionado
    """    
    if lista_desplegable_tipo_trabajo.get() == 'Agricultura':
        pitchLabel.place_forget()
        pitchEntry.place_forget()
        tipologiaLabel.place_forget()
        lista_desplegable_tipologia.place_forget()
        Multylabel.place(x=0,y=435)
        casilla_Multy1.place(x=90,y=440)
        casilla_Multy2.place(x=120,y=440)
        gb1Label.place(x=0,y=520)
        gb1Entry.place(x=180,y=520)
        gb2Label.place(x=0,y=580)
        gb2Entry.place(x=215,y=580)

    elif lista_desplegable_tipo_trabajo.get() == 'Fotovoltaica':
        pitchLabel.place(x=1200,y=65)
        pitchEntry.place(x=1300,y=65)
        tipologiaLabel.place(x=1020,y=110)
        lista_desplegable_tipologia.place(x=1250,y=110)
        Multylabel.place_forget()
        casilla_Multy1.place_forget()
        casilla_Multy2.place_forget()
        gb1Label.place_forget()
        gb1Entry.place_forget()
        gb2Label.place_forget()
        gb2Entry.place_forget()

def open_csv(fecha):
    """
    Abre un estadillo generado previamente
    """
    nombre_estadillo = str(fecha.get()).replace(':','_')+'_estadillo.csv'
    webbrowser.open(os.path.join(os.getcwd(), nombre_estadillo))

def guardar():
    """
    Funcion que se ejecuta al pulsar el boton de guardar.


    """
    nombre_estadillo = str(fecha.get()).replace(':','_')+'_estadillo.csv'
    directorio = os.path.join(os.getcwd(),nombre_estadillo)
    if lista_desplegable_tipo_trabajo.get() == 'Fotovoltaica':

        #---------------- Si los siguientes campos no están rellenos no te deja guardar
        if (len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
            and len(hora.get()) != 0 and len(pb.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_desplazado.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0
            and len(bat.get()) != 0 and len(lista_desplegable_tipologia.get())!=0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0
            and rec.get()==1 and RGB.get()==1) or vuelo_abortado.get()==1 :
              

        #------------Crea el DF donde se guarda el estadillo
            
            df = (pd.DataFrame(columns=['Empresa', 'Trabajo', 'Fecha','Piloto','Equipo_de_vuelo','Pitch','Hora_de_inicio','Hora_final', 'PB','Vuelo','Desplazado', #'Vuelo_del_dia',
                'Vel_vuelo','Alt_vuelo','Vel_de_aire','Temp_aire','Nubes','Radiacion','Tiempo_vuelo','Dist_Recorrida','Set_Bat_1','Set_Bat_2','Set_Bat_3','Volt_inicial',
                'Volt_final','GB1/','GB2/','Anotaciones','REC','RGB','Cali_Ini','Cali_Final','Tipologia','Vuelo_abortado']))

            df = (df.append({'Empresa': lista_desplegable_empresa.get(), 'Trabajo':lista_desplegable_trabajo.get(), 'Fecha':fecha.get(),'Piloto': lista_desplegable_piloto.get(),'Equipo_de_vuelo':lista_desplegable_equipo.get(),
                'Pitch':pitch.get(),'Hora_de_inicio': hora.get(),'Hora_final': hora_fin.get(),'PB': pb.get(),'Vuelo':v.get(), 'Desplazado': lista_desplegable_desplazado.get(), #'Vuelo_del_dia': vueloEntry.get(),
                'Vel_vuelo':lista_desplegable_velvuelo.get(),'Alt_vuelo': alt.get(),'Vel_de_aire': lista_desplegable_velaire.get(), 'Temp_aire': lista_desplegable_temp.get(), 'Nubes':lista_desplegable_nubes.get(),
                 'Radiacion': lista_desplegable_rad.get(),'Tiempo_vuelo': tiempo.get(),'Dist_Recorrida': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
                 'Volt_inicial':volt_inicial.get(),'Volt_final': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Anotaciones': textoComentario.get("1.0",'end-1c'),'REC':rec.get(),'RGB':RGB.get(),
                 'Cali_Ini': Multy1.get(),'Cali_Final':Multy2.get(),'Tipologia': lista_desplegable_tipologia.get(),'Vuelo_abortado': vuelo_abortado.get()},ignore_index=True))
            
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

            #---------- Mira a ver qué elementos se repiten en empresa y trabajo
            
            global opciones_empresa
            lista_empresa.append(lista_desplegable_empresa.get())
            
            for i in lista_empresa:
                if i not in lista_empresa_unicos:
                    lista_empresa_unicos.append(i)
            if len(lista_empresa_unicos) == 0:
                opciones_empresa = 'Escribe alguna empresa'
            else:
                opciones_empresa  = lista_empresa_unicos
            
            lista_desplegable_empresa['values']=opciones_empresa
            
            global opciones_trabajo
            lista_trabajo.append(lista_desplegable_trabajo.get())
            for i in lista_trabajo:
                if i not in lista_trabajo_unicos:
                    lista_trabajo_unicos.append(i)
            if len(lista_trabajo_unicos) == 0:
                opciones_trabajo = 'Escribe algo'
            else:
                opciones_trabajo  = lista_trabajo_unicos
            
            lista_desplegable_trabajo['values']=opciones_trabajo

            #-------- Conexión con base de datos ( ***** FUTURA IMPLEMENTACION ***** )
            # l = [lista_desplegable_trabajo.get(), '_desp'] #Crea el nombre en funcion de la planta de tal manera que quede así: 'nombrePlanta_desp'
            # nombre_df = ''.join(l)
                        
            # s = (pd.DataFrame(columns=['year','planta','powerblock','vuelo','desp_x','desp_y'])) #Crea el DF que será exportado como tabla a la base de datos
            # s = (s.append({'year':localtime[0] ,'planta':(lista_desplegable_trabajo.get()).upper(),'powerblock':pb.get(),'vuelo':v.get(),
            #     'desp_x':desplazamiento_x(),'desp_y':desplazamiento_y()},ignore_index=True))
            #engine = create_engine('postgresql://atom:Maps2019!@82.223.110.207:5432/atomdb')   #Conexión con la BBDD
            #s.to_sql(str(nombre_df), engine, if_exists='append',index=False)                   #Sube la tabla a la BBDD

            '''#Por si quieres ver el contenido de la tabla registrada en la base de datos
            conn = engine.raw_connection() #If the connection was created successfully, the connect() function returns a new connection object, otherwise, it throws a DatabaseError exception.
            cursor = conn.cursor() #The cursor object is used to execute SELECT statements.
            cursor.execute("""SELECT * FROM nombre_df """)# WHERE table_schema = 'public'""")
            for table in cursor.fetchall():
                print(table)
            '''

            #----------- Reinicia las variables

            reinicio_variables()
        else:
            MessageBox.showerror("Error", "No se han rellenado todos los parámetros necesarios.")
        



