import tkinter as tk
from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox as MessageBox
from tkinter import ttk
import tkinter.font as tkFont


import pandas as pd
import csv
import os
import time
import webbrowser
from PIL import ImageTk,Image
#import psycopg2 
#from sqlalchemy import create_engine
import io

#-------------------- Sacar el exe usando pyinstaller
#pyinstaller -w Estadillo_app.pyw

#------------- Crea y customiza los elementos de la raiz ------------


raiz=Tk()

raiz.title("Estadillo")

raiz.resizable(1,1) #Ancho, alto; true lo puedes cambiar, false no

#raiz.iconbitmap("C:/aerotools.ico")
raiz.geometry("850x650") #ancho y alto

raiz.state('zoomed')

#raiz.iconify()

raiz.config(bg="blue")  #cambia el color de fondo

#--------------- Crea y customiza los elementos del frame ------------

miFrame=Frame(raiz) #crea lo de dentro de la raiz

miFrame.pack(fill="both",expand=True) #se redimensiona entero

miFrame.config(bg="tomato") #cambia el color del frame

miFrame.config(width="950", height = "400")

miFrame.config(bd=35) #cuanto borde le das

#-----------------Funciones
global localtime
localtime = time.localtime(time.time())
#Inicializa variables

lista_empresa = []
lista_empresa_unicos = []

lista_trabajo = []
lista_trabajo_unicos = []

lista_piloto = []
lista_piloto_unicos = []

contador = 1

def hora_boton():
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

def hora_boton_fin():
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

def fecha_boton():
    localtime = time.localtime(time.time())
    fechaEntry.delete(0,'end')
    if localtime[2]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+'0'+str(localtime[2]))    
    elif localtime[1]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+str(localtime[2]))
    elif localtime[1]<10 and localtime[2]<10:
        fechaEntry.insert(0,str(localtime[0])+':'+'0'+str(localtime[1])+':'+'0'+str(localtime[2]))
    else:
        fechaEntry.insert(0,str(localtime[0])+':'+str(localtime[1])+':'+str(localtime[2]))
    
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
    rec.set(0)
    RGB.set(0)
    Multy1.set(0)
    Multy2.set(0)
    vuelo_abortado.set(0)
    


def guardar():
    directorio = os.path.join(os.getcwd(),str(fecha.get()).split(':')[0]+'_'+str(fecha.get()).split(':')[1]+'_'+str(fecha.get()).split(':')[2]+'_form.csv')
    if lista_desplegable_tipo_trabajo.get() == 'Photovoltaic':

        #---------------- Si los siguientes campos no están rellenos no te deja guardar
        if (len(lista_desplegable_country.get()) != 0 and len(lista_desplegable_empresa.get()) != 0 and len(lista_desplegable_trabajo.get()) != 0 and len(fecha.get()) != 0 and len(lista_desplegable_piloto.get()) != 0 and len(lista_desplegable_equipo.get()) != 0 #and len(str(vueloEntry.get())) != 0
            and len(hora.get()) != 0 and len(pb.get()) != 0 and len(v.get()) != 0 and len(lista_desplegable_desplazado.get()) != 0 and len(lista_desplegable_velvuelo.get()) != 0 and len(alt.get()) != 0
            and len(bat.get()) != 0 and len(lista_desplegable_tipologia.get())!=0 and len(volt_inicial.get()) != 0 and len(hora_fin.get()) != 0
            and rec.get()==1 and RGB.get()==1) or vuelo_abortado.get()==1 :
              

        #------------Crea el DF donde se guarda el estadillo
            
            df = (pd.DataFrame(columns=['Country','Enterprise', 'Project', 'Date','Pilot','Flight_equipment','Pitch', 'Initial_hour','Final_hour', 'PB','Flight','Displaced',
                'Flight_speed','Flight_height','Air_speed','Air_temp','Clouds','Radiation','Flight_time','Dist_Travelled','Set_Bat_1','Set_Bat_2','Set_Bat_3','Initial_volt',
                'Final_volt','GB1/','GB2/','Annotations','REC','RGB','Initial_Cali','Final_Cali','Typology','Flight_aborted']))

            df = (df.append({'Country':lista_desplegable_country.get(),'Enterprise': lista_desplegable_empresa.get(), 'Project':lista_desplegable_trabajo.get(), 'Date':fecha.get(),'Pilot': lista_desplegable_piloto.get(),'Flight_equipment':lista_desplegable_equipo.get(),
                'Pitch':pitch.get(),'Initial_hour': hora.get(),'Final_hour': hora_fin.get(),'PB': pb.get(),'Flight':v.get(), 'Displaced': lista_desplegable_desplazado.get(),
                'Flight_speed':lista_desplegable_velvuelo.get(),'Flight_height': alt.get(),'Air_speed': lista_desplegable_velaire.get(), 'Air_temp': lista_desplegable_temp.get(), 'Clouds':lista_desplegable_nubes.get(),
                 'Radiation': lista_desplegable_rad.get(),'Flight_time': tiempo.get(),'Dist_Travelled': distancia.get(),'Set_Bat_1': bat.get(),'Set_Bat_2': bat2.get(),'Set_Bat_3':bat3.get(),
                 'Initial_volt':volt_inicial.get(),'Final_volt': volt_final.get(),'GB1/': gb1.get(),'GB2/':gb2.get(),'Annotations': textoComentario.get("1.0",'end-1c'),'REC':rec.get(),'RGB':RGB.get(),
                 'Initial_Cali': Multy1.get(),'Final_Cali':Multy2.get(),'Typology': lista_desplegable_tipologia.get(),'Flight_aborted': vuelo_abortado.get()},ignore_index=True))
            
            #----- Cambia punto por coma a voltaje inicial, final y pitch

            for i in df['Initial_volt']:
                k=i.replace('.',',')
                df["Initial_volt"].replace({i: k}, inplace=True)
                
            for j in df['Final_volt']:
                volt_coma=j.replace('.',',')
                df["Final_volt"].replace({j: volt_coma}, inplace=True)

            for k in df['Pitch']:
                pitch_coma=k.replace('.',',')
                df["Pitch"].replace({k: pitch_coma}, inplace=True)
                

            #---------- Pasa el DF a CSV    

            df.to_csv(directorio, index=None, mode="a", header=not os.path.isfile(directorio),sep=';')

            #---------- Mira a ver qué elementos se repiten en empresa y trabajo
            
            # global opciones_empresa
            # lista_empresa.append(lista_desplegable_empresa.get())
            # for i in lista_empresa:
            #     if i not in lista_empresa_unicos:
            #         lista_empresa_unicos.append(i)
            # if len(lista_empresa_unicos) == 0:
            #     opciones_empresa = 'Write something'
            # else:
            #     opciones_empresa  = lista_empresa_unicos
            
            # lista_desplegable_empresa['values']=opciones_empresa
            
            # global opciones_trabajo
            # lista_trabajo.append(lista_desplegable_trabajo.get())
            # for i in lista_trabajo:
            #     if i not in lista_trabajo_unicos:
            #         lista_trabajo_unicos.append(i)
            # if len(lista_trabajo_unicos) == 0:
            #     opciones_trabajo = 'Write something'
            # else:
            #     opciones_trabajo  = lista_trabajo_unicos
            
            # lista_desplegable_trabajo['values']=opciones_trabajo

            global opciones_piloto
            lista_piloto.append(lista_desplegable_piloto.get())
            for i in lista_piloto:
                if i not in lista_piloto_unicos:
                    lista_piloto_unicos.append(i)
            if len(lista_piloto_unicos) == 0:
                opciones_piloto = 'Write something'
            else:
                opciones_piloto  = lista_piloto_unicos
            
            lista_desplegable_piloto['values']=opciones_piloto

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
            MessageBox.showerror("Error", "Not all required parameters have been filled in.")
        



def vuelo_autorrelleno():
    global contador
    contador += 1
    return contador
       
def opciones_desplazado(opciones_tipologia):

    if lista_desplegable_tipologia.get() == 'Fixed':
        opciones_desplazado = ['1 N','C','1 S']

    elif lista_desplegable_tipologia.get() == 'Trackers N-S' or lista_desplegable_tipologia.get() == 'Polar trackers':
        opciones_desplazado = ['2 E','1 E','0.5 E','C','0.5 W','1 W','2 W']

    else:
        opciones_desplazado = ['Nothing yet']

    lista_desplegable_desplazado['values']=opciones_desplazado
    #return lista_desplegable_desplazado

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
    if lista_desplegable_desplazado.get() == '2 W':
        desp_x = 2 * float(pitch.get())
    elif lista_desplegable_desplazado.get() == '1 W':
        desp_x = pitch.get()
    elif lista_desplegable_desplazado.get() == '0.5 W':
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
    if lista_desplegable_tipo_trabajo.get() == 'Agriculture':
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

    elif lista_desplegable_tipo_trabajo.get() == 'Photovoltaic':
        pitchLabel.place(x=1190,y=65)
        pitchEntry.place(x=1320,y=65)
        tipologiaLabel.place(x=1120,y=110)
        lista_desplegable_tipologia.place(x=1250,y=110)
        Multylabel.place_forget()
        casilla_Multy1.place_forget()
        casilla_Multy2.place_forget()
        gb1Label.place_forget()
        gb1Entry.place_forget()
        gb2Label.place_forget()
        gb2Entry.place_forget()


'''

def displayontowindow():
    win = tk.Toplevel()

    frame = Frame(win, width=600, height=310, bg="light grey")

    frame = ttk.Frame(win, width=300, height=250)

    # Canvas creation with double scrollbar
    hscrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    sizegrip = ttk.Sizegrip(frame)
    canvas = tk.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set,
                            xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)

    # Add controls here
    subframe = ttk.Frame(canvas)

    # open file
    with open("export_dataframe.csv", newline="") as file:
        reader = csv.reader(file)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                label = tk.Label(subframe, width=10, height=2,
                                      text=row, relief=tk.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    # Packing everything
    subframe.pack(fill=tk.BOTH, expand=tk.TRUE)
    hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    sizegrip.pack(in_=hscrollbar, side=BOTTOM, anchor="se")
    canvas.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=tk.TRUE)
    frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

    canvas.create_window(0, 0, window=subframe)
    raiz.update_idletasks()  # update geometry
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)
'''
def open_csv():
    webbrowser.open(os.path.join(os.getcwd(),str(fecha.get()).split(':')[0]+'_'+str(fecha.get()).split(':')[1]+'_'+str(fecha.get()).split(':')[2]+'_form.csv'))



#------------------- Imagen
 
canvas = Canvas(miFrame, width = 250, height = 90)  
canvas.place(x=550,y=-40)  
img = ImageTk.PhotoImage(Image.open("atom.png").resize((250,90))) #1733x625 
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
piloto = StringVar()
equipo_de_vuelo = StringVar()
pitch = StringVar()
country = StringVar()


countryLabel = Label(miFrame, text="Country: ",font=fontStyle)
countryLabel.place(x=0,y=0)
lista_desplegable_country = ttk.Combobox(miFrame, width=12,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_country.place(x=120,y=0)
opciones_country = ['Australia','UK','Morocco','Chile','Puerto Rico','Uruguay','Argentina','France','Italy']
lista_desplegable_country['values']=opciones_country

empresaLabel = Label(miFrame, text="PV Enterprise: ",font=fontStyle)
empresaLabel.place(x=0,y=70)
lista_desplegable_empresa = ttk.Combobox(miFrame, width=15,font=fontStyle,style="custom.TCombobox",state='readonly')
lista_desplegable_empresa.place(x=160,y=70)
opciones_empresa = ['Ingeteam']
lista_desplegable_empresa['values']=opciones_empresa

trabajoLabel = Label(miFrame, text="Project: ",font=fontStyle)
trabajoLabel.place(x=0, y=110)
lista_desplegable_trabajo = ttk.Combobox(miFrame, width=15,font=fontStyle,style="custom.TCombobox",state='readonly')
lista_desplegable_trabajo.place(x=120,y=110)
opciones_trabajo = ['Childers','Susan River','Raven Thorpe','Roan Head','Ourzazate','Bougdour','Layoune','Salinas']
lista_desplegable_trabajo['values']=opciones_trabajo

boton_fecha = Button(miFrame, text = "Date", command=fecha_boton,font=fontStyle,bg='green')
boton_fecha.place(x=830,y=58)
fechaEntry = Entry(miFrame,textvariable=fecha,font=fontStyle,bg='yellow',width=10)
fechaEntry.place(x=930,y=65)

pitchLabel = Label(miFrame, text="Pitch (m): ",font=fontStyle,width=8)
pitchLabel.place(x=1190,y=65)
pitchEntry = Entry(miFrame,textvariable=pitch,font=fontStyle,width=5,bg='yellow')
pitchEntry.place(x=1320,y=65)

pilotoLabel = Label(miFrame, text="Drone Enterprise: ",font=fontStyle)
pilotoLabel.place(x=400,y=70)
lista_desplegable_piloto = ttk.Combobox(miFrame, width=11,style="custom.TCombobox",font=fontStyle)
lista_desplegable_piloto.place(x=600,y=70)
#opciones_piloto = ['Oscar','Alberto']
#lista_desplegable_piloto['values']=opciones_piloto

equipoLabel = Label(miFrame, text="Flight equipment: ",font=fontStyle)
equipoLabel.place(x=400, y= 110)
lista_desplegable_equipo = ttk.Combobox(miFrame, width=9,state='readonly',font=fontStyle,style="custom.TCombobox")
lista_desplegable_equipo.place(x=590,y=110)
opciones_equipo = ['AT4-01','AT4-05','AT6','AT6-02','DJI M200','DJI M210','DJI M300']
lista_desplegable_equipo['values']=opciones_equipo

tipologiaLabel = Label(miFrame, text="Typology: ",font=fontStyle)
tipologiaLabel.place(x=1120,y=110)
lista_desplegable_tipologia = ttk.Combobox(miFrame, width=15,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_tipologia.bind("<<ComboboxSelected>>", opciones_desplazado)
lista_desplegable_tipologia.place(x=1250,y=110)
opciones_tipologia = ['Fixed','Trackers N-S','Trackers 2 axis','Polar trackers']
lista_desplegable_tipologia['values']=opciones_tipologia


  
tipo_trabajoLabel = Label(miFrame, text="Project type: ",font=fontStyle)
tipo_trabajoLabel.place(x=780,y=110)
lista_desplegable_tipo_trabajo = ttk.Combobox(miFrame, width=10,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_tipo_trabajo.bind("<<ComboboxSelected>>", ocultar_mostrar)
lista_desplegable_tipo_trabajo.place(x=950,y=110)
opciones_tipo_trabajo = ['Photovoltaic','Agriculture','Eolic']
lista_desplegable_tipo_trabajo['values']=opciones_tipo_trabajo


#-----------------Crea la línea de separación

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
rec = IntVar()      # 1 si, 0 no
RGB = IntVar()    # 1 si, 0 no
Multy1 = IntVar() # 1 si, 0 no
Multy2 = IntVar() # 1 si, 0 no
vuelo_abortado = IntVar() # 1 si, 0 no
tipologia = StringVar()
pb  =StringVar()
v = StringVar()



reclabel = Label(miFrame, text='REC', font=fontStyle)
reclabel.place(x=0,y=365)
casilla_rec = Checkbutton(miFrame,variable=rec, onvalue=1, offvalue=0,bg='yellow')
casilla_rec.place(x=60,y=370)

RGBlabel = Label(miFrame, text='RGB', font=fontStyle)
RGBlabel.place(x=0,y=400)
casilla_RGB = Checkbutton(miFrame,variable=RGB, onvalue=1, offvalue=0,bg='yellow')
casilla_RGB.place(x=60,y=405)

Multylabel = Label(miFrame, text='MULTY', font=fontStyle)
Multylabel.place(x=0,y=435)
casilla_Multy1 = Checkbutton(miFrame,variable=Multy1, onvalue=1, offvalue=0)
casilla_Multy1.place(x=90,y=440)
casilla_Multy2 = Checkbutton(miFrame,variable=Multy2, onvalue=1, offvalue=0)
casilla_Multy2.place(x=120,y=440)



# vueloLabel = Label(miFrame, text="Flight of the day: ",font=fontStyle)
# vueloLabel.place(x=0,y=200)
# #vueloEntry = Entry(miFrame,textvariable=vuelo,font=fontStyle)
# vueloEntry = Entry(miFrame,font=fontStyle,width=5,bg='yellow')
# vueloEntry.insert(0,1)
# vueloEntry.place(x=200,y=200)

boton_print = Button(miFrame, text = "CSV", command=open_csv,font=font_boton,bg='green')
boton_print.place(x=1300,y=680)


boton_hora = Button(miFrame, text = "Initial time", command=hora_boton,font=fontStyle,bg='green')
boton_hora.place(x=200,y=295)
horaEntry = Entry(miFrame,textvariable=hora,font=fontStyle,width= 8,bg='yellow')
horaEntry.place(x=380,y=300)

boton_hora_fin = Button(miFrame, text = "Final time", command=hora_boton_fin,font=fontStyle,bg='green')
boton_hora_fin.place(x=200,y=365)
hora_fin_Entry = Entry(miFrame,textvariable=hora_fin,font=fontStyle,width= 8,bg='yellow')
hora_fin_Entry.place(x=380,y=370)

zonaLabel = Label(miFrame, text="Flown area: ",font=fontStyle)
zonaLabel.place(x=0,y=200)

pbLabel = Label(miFrame, text="PB: ",font=fontStyle,width=5)
pbLabel.place(x=150,y=200)
pbEntry = Entry(miFrame,textvariable=pb,font=fontStyle,width=5,bg='yellow')
pbEntry.place(x=230,y=200)

vLabel = Label(miFrame, text="Flight: ",font=fontStyle,width=5)
vLabel.place(x=320,y=200)
vEntry = Entry(miFrame,textvariable=v,font=fontStyle,width=5,bg='yellow')
vEntry.place(x=400,y=200)

desplazadoLabel = Label(miFrame, text="Displaced: ",font=fontStyle)
desplazadoLabel.place(x=480,y=200)
lista_desplegable_desplazado = ttk.Combobox(miFrame, width=8,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_desplazado.place(x=600,y=200)


velvueloLabel = Label(miFrame, text="Flight speed (m/s): ",font=fontStyle)
velvueloLabel.place(x=770,y=250)
lista_desplegable_velvuelo = ttk.Combobox(miFrame, width=4,state='readonly',style="custom.TCombobox",font=fontStyle)
lista_desplegable_velvuelo.place(x=970,y=250)
opciones_velvuelo = ['3','3.5','4','4.5','5','5.5','6']
lista_desplegable_velvuelo['values']=opciones_velvuelo


altLabel = Label(miFrame, text="Flight height (m): ",font=fontStyle)
altLabel.place(x=510,y=250)
altEntry = Entry(miFrame,textvariable=alt,font=fontStyle,bg='yellow',width=5)
altEntry.place(x=690,y=250)

velaireLabel = Label(miFrame, text="Air speed: ",font=fontStyle)
velaireLabel.place(x=950,y=200)
lista_desplegable_velaire = ttk.Combobox(miFrame, width=9,state='readonly',font=fontStyle)
lista_desplegable_velaire.place(x=1080,y=200)
opciones_velaire = ['0 to 5','5 to 10','10 to 20','20 to 30']
lista_desplegable_velaire['values']=opciones_velaire


tempLabel = Label(miFrame, text="Air temp.: ",font=fontStyle)
tempLabel.place(x=1230,y=200)
#tempEntry = Entry(miFrame,textvariable=temp,font=fontStyle,width=4)
#tempEntry.place(x=1350,y=250)
lista_desplegable_temp = ttk.Combobox(miFrame, width=6,state='readonly',font=fontStyle)
lista_desplegable_temp.place(x=1360,y=200)
opciones_temp = ['<10','10-15','15-20','20-25','25-30','30-35','35-40','>40']
lista_desplegable_temp['values']=opciones_temp

nubesLabel = Label(miFrame, text="Clouds: ",font=fontStyle)
nubesLabel.place(x=750,y=200)
lista_desplegable_nubes = ttk.Combobox(miFrame, width=4,state='readonly',font=fontStyle)
lista_desplegable_nubes.place(x=845,y=200)
opciones_nubes = ['0','1','2','3']
lista_desplegable_nubes['values']=opciones_nubes


radiacionLabel = Label(miFrame, text="Radiation: ",font=fontStyle)
radiacionLabel.place(x=1100,y=250)
#radiacionEntry = Entry(miFrame,textvariable=radiacion,font=fontStyle,width=5)
#radiacionEntry.place(x=1100,y=250)
lista_desplegable_rad = ttk.Combobox(miFrame, width=4,state='readonly',font=fontStyle)
lista_desplegable_rad.place(x=1230,y=250)
opciones_rad = ['>400','>500','>600','>700','>800','>900']
lista_desplegable_rad['values']=opciones_rad

tiempoLabel = Label(miFrame, text="Flight time: ",font=fontStyle)
tiempoLabel.place(x=700,y=370)
tiempoEntry = Entry(miFrame,textvariable=tiempo,font=fontStyle,width=5)
tiempoEntry.place(x=860,y=370)

distanciaLabel = Label(miFrame, text="Dist. travelled: ",font=fontStyle)
distanciaLabel.place(x=960,y=370)
distanciaEntry = Entry(miFrame,textvariable=distancia,font=fontStyle,width=5)
distanciaEntry.place(x=1130,y=370)

batLabel = Label(miFrame, text="Set Bat: ",font=fontStyle)
batLabel.place(x=0,y=250)
batEntry = Entry(miFrame,textvariable=bat,font=fontStyle,width=5,bg='yellow')
batEntry.place(x=100,y=250)
bat2Entry = Entry(miFrame,textvariable=bat2,font=fontStyle,width=5)
bat2Entry.place(x=170,y=250)
bat3Entry = Entry(miFrame,textvariable=bat3,font=fontStyle,width=5)
bat3Entry.place(x=240,y=250)

voltinicialLabel = Label(miFrame, text="Initial volt: ",font=fontStyle)
voltinicialLabel.place(x=330,y=250)
voltinicialEntry = Entry(miFrame,textvariable=volt_inicial,font=fontStyle,bg='yellow',width=4)
voltinicialEntry.place(x=450,y=250)

voltfinalLabel = Label(miFrame, text="Final volt: ",font=fontStyle)
voltfinalLabel.place(x=510,y=370)
voltfinalEntry = Entry(miFrame,textvariable=volt_final,font=fontStyle,width=4)
voltfinalEntry.place(x=620,y=370)

gb1Label = Label(miFrame, text="GB Before flight: ",font=fontStyle)
gb1Label.place(x=0,y=520)
gb1Entry = Entry(miFrame,textvariable=gb1,font=fontStyle,width=10)
gb1Entry.place(x=180,y=520)

gb2Label = Label(miFrame, text="GB After flight: ",font=fontStyle)
gb2Label.place(x=0,y=580)
gb2Entry = Entry(miFrame,textvariable=gb2,font=fontStyle,width=10)
gb2Entry.place(x=215,y=580)



label2=Label(miFrame, text="Annotations:", font=fontStyle)        
label2.place(x=350,y=520)


text_frame = tk.Frame(miFrame)
textoComentario=tk.Text(text_frame, width=50, height=5,font=fontStyle)
textoComentario.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
scrollVert=ttk.Scrollbar(text_frame, command=textoComentario.yview)
scrollVert.pack(fill=tk.Y, side=tk.RIGHT)

text_frame.place(x=500,y=520)#column=1, row=8, sticky="w",pady=5

textoComentario.config(yscrollcommand=scrollVert.set)



vuelo_abortado_label = Label(miFrame, text='Flight aborted', font=fontStyle)
vuelo_abortado_label.place(x=1200,y=580)
casilla_vuelo_abortado = Checkbutton(miFrame,variable=vuelo_abortado, onvalue=1, offvalue=0)
casilla_vuelo_abortado.place(x=1365,y=585)



boton_guardar=Button(miFrame, text = "Save", command=guardar,width=10,height=1,font=font_boton,bg='green')
boton_guardar.place(x=700,y=680)





raiz.mainloop()